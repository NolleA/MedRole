import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_db
from app.services.patient_sim import generate_response

router = APIRouter()


class MessageCreate(BaseModel):
    content: str


@router.post("/sessions/{session_id}/chat")
def send_message(session_id: str, body: MessageCreate):
    with get_db() as conn:
        session = conn.execute(
            "SELECT id, case_id, status FROM sessions WHERE id = ?",
            (session_id,),
        ).fetchone()

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session["status"] != "in_progress":
        raise HTTPException(status_code=400, detail="Session is not in progress")

    # Save student message
    student_msg_id = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute(
            "INSERT INTO messages (id, session_id, role, content) VALUES (?, ?, 'student', ?)",
            (student_msg_id, session_id, body.content),
        )

    # Build conversation for AI
    with get_db() as conn:
        msgs = conn.execute(
            "SELECT role, content, timestamp FROM messages WHERE session_id = ? ORDER BY timestamp",
            (session_id,),
        ).fetchall()

    conversation = [
        {"role": "user" if m["role"] == "student" else "assistant", "content": m["content"]}
        for m in msgs
    ]

    # Generate AI response
    try:
        ai_content = generate_response(session["case_id"], conversation)
    except RuntimeError:
        ai_content = _fallback_response()

    # Save patient message
    patient_msg_id = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute(
            "INSERT INTO messages (id, session_id, role, content) VALUES (?, ?, 'patient', ?)",
            (patient_msg_id, session_id, ai_content),
        )

    # Return both messages
    student_msg = {
        "id": student_msg_id,
        "session_id": session_id,
        "role": "student",
        "content": body.content,
        "timestamp": msgs[-1]["timestamp"] if msgs else "",
    }
    patient_msg = {
        "id": patient_msg_id,
        "session_id": session_id,
        "role": "patient",
        "content": ai_content,
        "timestamp": "",
    }
    return {"student_message": student_msg, "patient_message": patient_msg}


def _fallback_response() -> str:
    return "嗯…医生，我尽量描述清楚。您再问得具体一点？"
