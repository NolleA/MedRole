import json
from app.database import get_db
from app.prompts.patient_system import build_patient_prompt
from app.services.llm_service import chat


def load_case(case_id: str) -> dict:
    with get_db() as conn:
        row = conn.execute("SELECT * FROM cases WHERE id = ?", (case_id,)).fetchone()
    if not row:
        raise ValueError(f"Case {case_id} not found")
    return {
        "chief_complaint": row["chief_complaint"],
        "patient_profile": json.loads(row["patient_profile"]),
        "symptoms_description": row["symptoms_description"],
        "physical_exam": json.loads(row["physical_exam"]),
        "emotional_state": row["emotional_state"],
    }


def generate_opening(case_id: str) -> str:
    """Generate the AI patient's opening line for a new session."""
    case = load_case(case_id)
    system_prompt = build_patient_prompt(case)
    response = chat(
        messages=[{"role": "user", "content": "（开始问诊，请用你的主诉自然地开始对话）"}],
        system=system_prompt,
        max_tokens=150,
        temperature=0.8,
    )
    return response


def generate_response(case_id: str, conversation: list[dict]) -> str:
    """Generate AI patient's response to the student's latest message."""
    case = load_case(case_id)
    system_prompt = build_patient_prompt(case)
    response = chat(
        messages=conversation,
        system=system_prompt,
        max_tokens=250,
        temperature=0.8,
    )
    return response
