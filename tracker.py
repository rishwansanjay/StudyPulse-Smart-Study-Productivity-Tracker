import sqlite3
import database

def add_session(subject, duration, date):
    conn = sqlite3.connect("studypulse.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions (subject, duration, date) VALUES (?, ?, ?)",
        (subject, duration, date)
    )
    conn.commit()
    conn.close()

def view_sessions():
    conn = sqlite3.connect("studypulse.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, duration, date FROM sessions")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No sessions found")
        return

    for r in rows:
        print(f"{r[0]} | {r[1]} mins | {r[2]}")
