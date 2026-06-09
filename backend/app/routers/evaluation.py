import json
from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.services.evaluator import evaluate_session

router = APIRouter()


@router.post("/sessions/{session_id}/evaluate")
def do_evaluate(session_id: str):
    # Check session exists
    with get_db() as conn:
        session = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Check if evaluation already exists
    with get_db() as conn:
        existing = conn.execute(
            "SELECT * FROM evaluations WHERE session_id = ?", (session_id,)
        ).fetchone()
    if existing:
        return json.loads(existing["detailed_report"])

    if session["status"] != "completed":
        raise HTTPException(status_code=400, detail="Session must be completed first")

    try:
        result = evaluate_session(session_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"LLM API error: {str(e)}")


@router.get("/sessions/{session_id}/evaluation")
def get_evaluation(session_id: str):
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM evaluations WHERE session_id = ?", (session_id,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    return json.loads(row["detailed_report"])
