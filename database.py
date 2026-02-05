import sqlite3

conn = sqlite3.connect("studypulse.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    duration INTEGER,
    date TEXT
)
""")

conn.commit()
