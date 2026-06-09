import sqlite3
import os
from contextlib import contextmanager

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_PATH = os.path.join(DB_DIR, "medrole.db")


def get_db_path() -> str:
    os.makedirs(DB_DIR, exist_ok=True)
    return DB_PATH


@contextmanager
def get_db():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS cases (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                department TEXT NOT NULL,
                difficulty TEXT NOT NULL CHECK (difficulty IN ('beginner','intermediate','advanced')),
                chief_complaint TEXT NOT NULL,
                patient_profile TEXT NOT NULL,
                symptoms_description TEXT NOT NULL,
                physical_exam TEXT NOT NULL,
                emotional_state TEXT NOT NULL DEFAULT 'anxious',
                rubric TEXT NOT NULL,
                key_questions TEXT NOT NULL,
                red_flags TEXT NOT NULL,
                diagnosis TEXT NOT NULL,
                is_active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                case_id TEXT NOT NULL REFERENCES cases(id),
                status TEXT NOT NULL DEFAULT 'in_progress'
                    CHECK (status IN ('in_progress','completed','abandoned')),
                started_at TEXT NOT NULL DEFAULT (datetime('now')),
                completed_at TEXT,
                notes TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_sessions_status ON sessions(status);
            CREATE INDEX IF NOT EXISTS idx_sessions_case_id ON sessions(case_id);

            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
                role TEXT NOT NULL CHECK (role IN ('student','patient','system')),
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id, timestamp);

            CREATE TABLE IF NOT EXISTS evaluations (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL UNIQUE REFERENCES sessions(id) ON DELETE CASCADE,
                overall_score REAL NOT NULL,
                completeness_score REAL NOT NULL,
                communication_score REAL NOT NULL,
                clinical_thinking_score REAL NOT NULL,
                objective_score REAL NOT NULL,
                detailed_report TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS feedback (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL REFERENCES sessions(id),
                rating INTEGER CHECK (rating BETWEEN 1 AND 5),
                comment TEXT,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
        """)
