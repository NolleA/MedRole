import json
from fastapi import APIRouter, HTTPException, Query
from app.database import get_db

router = APIRouter()


def row_to_case(row) -> dict:
    return {
        "id": row["id"],
        "title": row["title"],
        "department": row["department"],
        "difficulty": row["difficulty"],
        "chief_complaint": row["chief_complaint"],
        "patient_profile": json.loads(row["patient_profile"]),
        "is_active": bool(row["is_active"]),
    }


@router.get("/cases")
def list_cases(
    department: str | None = Query(None),
    difficulty: str | None = Query(None),
):
    query = "SELECT * FROM cases WHERE is_active = 1"
    params: list = []
    if department:
        query += " AND department = ?"
        params.append(department)
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)
    query += " ORDER BY created_at DESC"

    with get_db() as conn:
        rows = conn.execute(query, params).fetchall()
    return [row_to_case(r) for r in rows]


@router.get("/cases/{case_id}")
def get_case(case_id: str):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM cases WHERE id = ?", (case_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Case not found")
    result = row_to_case(row)
    result["symptoms_description"] = row["symptoms_description"]
    result["physical_exam"] = json.loads(row["physical_exam"])
    result["emotional_state"] = row["emotional_state"]
    result["key_questions"] = json.loads(row["key_questions"])
    result["red_flags"] = json.loads(row["red_flags"])
    return result
