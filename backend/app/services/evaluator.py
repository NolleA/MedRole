import json
import re
from app.database import get_db
from app.prompts.evaluator_system import EVALUATOR_SYSTEM_PROMPT
from app.services.llm_service import chat_json


def evaluate_session(session_id: str) -> dict:
    # Load session + messages
    with get_db() as conn:
        session = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    if not session:
        raise ValueError("Session not found")
    if session["status"] != "completed":
        raise ValueError("Session must be completed before evaluation")

    # Load case
    with get_db() as conn:
        case = conn.execute("SELECT * FROM cases WHERE id = ?", (session["case_id"],)).fetchone()
    if not case:
        raise ValueError("Case not found")

    # Load messages
    with get_db() as conn:
        msgs = conn.execute(
            "SELECT role, content FROM messages WHERE session_id = ? ORDER BY timestamp",
            (session_id,),
        ).fetchall()

    # Build conversation transcript
    transcript_parts = []
    for m in msgs:
        if m["role"] == "student":
            transcript_parts.append(f"学生：{m['content']}")
        elif m["role"] == "patient":
            transcript_parts.append(f"病人：{m['content']}")
    transcript = "\n".join(transcript_parts)

    # Format rubric
    rubric = json.loads(case["rubric"])
    rubric_parts = []
    for item in rubric["items"]:
        rubric_parts.append(f"{item['id']}. [{item['category']}] {item['text']} (权重:{item['weight']})")
    formatted_rubric = "\n".join(rubric_parts)

    # Build evaluation prompt
    system_prompt = EVALUATOR_SYSTEM_PROMPT.format(
        case_title=case["title"],
        diagnosis=case["diagnosis"],
        chief_complaint=case["chief_complaint"],
        formatted_rubric=formatted_rubric,
        conversation_transcript=transcript,
    )

    # Call Claude
    raw = chat_json(
        messages=[{"role": "user", "content": "请对以上对话进行评估，严格按照指定的JSON格式输出结果。"}],
        system=system_prompt,
        max_tokens=3000,
    )

    # Parse JSON - try to extract from markdown code blocks if present
    result = _parse_evaluation_json(raw)

    # Validate
    _validate_evaluation(result)

    # Save to DB
    import uuid
    eval_id = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute(
            """INSERT INTO evaluations
               (id, session_id, overall_score, completeness_score, communication_score,
                clinical_thinking_score, objective_score, detailed_report)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                eval_id,
                session_id,
                result["overall_score"],
                result["dimensions"]["completeness"]["score"],
                result["dimensions"]["communication"]["score"],
                result["dimensions"]["clinical_thinking"]["score"],
                result["dimensions"]["objective"]["score"],
                json.dumps(result, ensure_ascii=False),
            ),
        )

    result["id"] = eval_id
    result["session_id"] = session_id
    return result


def _parse_evaluation_json(raw: str) -> dict:
    """Parse JSON from LLM response, handling markdown code blocks."""
    # Try direct parse first
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Try extract from ```json ... ``` block
    m = re.search(r'```(?:json)?\s*([\s\S]*?)```', raw)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    # Try find first { ... } pair
    m = re.search(r'\{[\s\S]*\}', raw)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass

    raise ValueError(f"Failed to parse evaluation JSON from: {raw[:500]}")


def _validate_evaluation(result: dict):
    """Basic validation of evaluation structure."""
    required = ["overall_score", "dimensions", "summary"]
    for key in required:
        if key not in result:
            raise ValueError(f"Evaluation missing required field: {key}")

    dims = result["dimensions"]
    for dim in ["completeness", "communication", "clinical_thinking", "objective"]:
        if dim not in dims:
            raise ValueError(f"Evaluation missing dimension: {dim}")
        d = dims[dim]
        for field in ["score", "strengths", "improvements", "feedback"]:
            if field not in d:
                raise ValueError(f"Dimension {dim} missing field: {field}")

    for score_field in ["overall_score"] + [f"dimensions.{d}.score" for d in ["completeness", "communication", "clinical_thinking", "objective"]]:
        pass  # scores are checked above
