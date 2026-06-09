from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.routers import cases, sessions, chat, evaluation

app = FastAPI(title="MedRole API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cases.router, prefix="/api", tags=["cases"])
app.include_router(sessions.router, prefix="/api", tags=["sessions"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(evaluation.router, prefix="/api", tags=["evaluation"])


@app.on_event("startup")
def on_startup():
    init_db()
    from app.database import get_db
    with get_db() as conn:
        count = conn.execute("SELECT COUNT(*) FROM cases").fetchone()[0]
        if count == 0:
            from app.prompts.seed_cases import CASES
            for c in CASES:
                conn.execute(
                    """INSERT INTO cases (id, title, department, difficulty, chief_complaint,
                       patient_profile, symptoms_description, physical_exam, emotional_state,
                       rubric, key_questions, red_flags, diagnosis, is_active)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (c["id"], c["title"], c["department"], c["difficulty"],
                     c["chief_complaint"], c["patient_profile"], c["symptoms_description"],
                     c["physical_exam"], c["emotional_state"], c["rubric"],
                     c["key_questions"], c["red_flags"], c["diagnosis"], c["is_active"]),
                )
            print(f"Auto-seeded {len(CASES)} cases.")


@app.get("/api/health")
def health():
    return {"status": "ok"}
