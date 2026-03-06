import sqlite3
import json
from datetime import datetime

DB = "runs.db"


def init_db():

    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_run(data):

    conn = sqlite3.connect(DB)

    conn.execute(
        "INSERT INTO runs (timestamp,data) VALUES (?,?)",
        (datetime.now().isoformat(), json.dumps(data))
    )

    conn.commit()
    conn.close()


def list_runs():

    conn = sqlite3.connect(DB)

    rows = conn.execute(
        "SELECT timestamp,data FROM runs ORDER BY id DESC LIMIT 20"
    ).fetchall()

    conn.close()

    runs = []

    for r in rows:

        runs.append({
            "timestamp": r[0],
            "data": json.loads(r[1])
        })

    return runs