import uuid
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_db
from app.services.patient_sim import generate_opening

router = APIRouter()


class SessionCreate(BaseModel):
    case_id: str


class SessionUpdate(BaseModel):
    status: str


def row_to_session(row, include_messages: bool = False) -> dict:
    result = {
        "id": row["id"],
        "case_id": row["case_id"],
        "status": row["status"],
        "started_at": row["started_at"],
        "completed_at": row["completed_at"],
    }
    # Join case title
    with get_db() as conn:
        case = conn.execute("SELECT title FROM cases WHERE id = ?", (row["case_id"],)).fetchone()
    if case:
        result["case_title"] = case["title"]

    if include_messages:
        with get_db() as conn:
            msgs = conn.execute(
                "SELECT * FROM messages WHERE session_id = ? ORDER BY timestamp",
                (row["id"],),
            ).fetchall()
        result["messages"] = [
            {
                "id": m["id"],
                "session_id": m["session_id"],
                "role": m["role"],
                "content": m["content"],
                "timestamp": m["timestamp"],
            }
            for m in msgs
        ]
    return result


@router.post("/sessions")
def create_session(body: SessionCreate):
    # Validate case
    with get_db() as conn:
        case = conn.execute("SELECT id FROM cases WHERE id = ? AND is_active = 1", (body.case_id,)).fetchone()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")

    session_id = str(uuid.uuid4())

    with get_db() as conn:
        conn.execute(
            "INSERT INTO sessions (id, case_id, status) VALUES (?, ?, 'in_progress')",
            (session_id, body.case_id),
        )

    # Generate AI opening line
    try:
        opening = generate_opening(body.case_id)
    except RuntimeError as e:
        # If no API key, use fallback opening
        opening = _fallback_opening(body.case_id)

    # Save opening message
    msg_id = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute(
            "INSERT INTO messages (id, session_id, role, content) VALUES (?, ?, 'patient', ?)",
            (msg_id, session_id, opening),
        )

    # Return session with messages
    with get_db() as conn:
        row = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    result = row_to_session(row)
    result["messages"] = [{
        "id": msg_id,
        "session_id": session_id,
        "role": "patient",
        "content": opening,
        "timestamp": result["started_at"],
    }]
    return result


def _fallback_opening(case_id: str) -> str:
    with get_db() as conn:
        row = conn.execute("SELECT chief_complaint FROM cases WHERE id = ?", (case_id,)).fetchone()
    if row:
        return row["chief_complaint"]
    return "医生你好，我身体不太舒服..."


@router.get("/sessions")
def list_sessions(status: str | None = None):
    query = "SELECT * FROM sessions"
    params: list = []
    if status:
        query += " WHERE status = ?"
        params.append(status)
    query += " ORDER BY started_at DESC LIMIT 50"
    with get_db() as conn:
        rows = conn.execute(query, params).fetchall()
    return [row_to_session(r) for r in rows]


@router.get("/sessions/{session_id}")
def get_session(session_id: str):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Session not found")
    return row_to_session(row, include_messages=True)


@router.patch("/sessions/{session_id}")
def update_session(session_id: str, body: SessionUpdate):
    if body.status not in ("completed", "abandoned"):
        raise HTTPException(status_code=400, detail="Invalid status")
    with get_db() as conn:
        existing = conn.execute("SELECT id FROM sessions WHERE id = ?", (session_id,)).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Session not found")
        now = None
        if body.status == "completed":
            from datetime import datetime
            now = datetime.utcnow().isoformat()
        conn.execute(
            "UPDATE sessions SET status = ?, completed_at = ? WHERE id = ?",
            (body.status, now, session_id),
        )
    with get_db() as conn:
        row = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    return row_to_session(row)
