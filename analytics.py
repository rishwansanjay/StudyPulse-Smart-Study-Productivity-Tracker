import sqlite3
import database

def show_summary():
    conn = sqlite3.connect("studypulse.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(duration) FROM sessions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT subject, SUM(duration) FROM sessions GROUP BY subject")
    subjects = cursor.fetchall()

    conn.close()

    print("\nTotal Study Time:", total if total else 0, "minutes")
    print("\nSubject-wise Breakdown:")

    for s in subjects:
        print(s[0], ":", s[1], "minutes")
