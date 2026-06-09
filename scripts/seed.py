import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.database import get_db, init_db
from app.prompts.seed_cases import CASES

init_db()

with get_db() as conn:
    existing = conn.execute("SELECT COUNT(*) FROM cases").fetchone()[0]
    if existing > 0:
        print(f"DB already has {existing} cases. Dropping and re-seeding...")
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.execute("DELETE FROM feedback")
        conn.execute("DELETE FROM evaluations")
        conn.execute("DELETE FROM messages")
        conn.execute("DELETE FROM sessions")
        conn.execute("DELETE FROM cases")
        conn.execute("PRAGMA foreign_keys=ON")

    for c in CASES:
        conn.execute(
            """INSERT INTO cases (id, title, department, difficulty, chief_complaint,
               patient_profile, symptoms_description, physical_exam, emotional_state,
               rubric, key_questions, red_flags, diagnosis, is_active)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (c["id"], c["title"], c["department"], c["difficulty"],
             c["chief_complaint"], c["patient_profile"], c["symptoms_description"],
             c["physical_exam"], c["emotional_state"], c["rubric"],
             c["key_questions"], c["red_flags"], c["diagnosis"], c["is_active"])
        )

print(f"Seeded {len(CASES)} cases successfully.")
for c in CASES:
    print(f"  - {c['title']} ({c['department']}, {c['difficulty']})")
