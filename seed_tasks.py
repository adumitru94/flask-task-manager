import sqlite3

tasks = [
    ("Setup project structure", 0, "2026-01-20"),
    ("Create Flask app", 1, "2026-01-15"),
    ("Implement task CRUD", 1, "2026-01-18"),
    ("Add task filtering", 0, "2026-01-22"),
    ("Add due date support", 1, "2026-01-10"),
    ("Highlight overdue tasks", 0, "2026-01-12"),
    ("Implement task sorting", 1, "2026-01-14"),
    ("Fix NoneType bugs", 1, None),
    ("Refactor templates", 0, None),
    ("Improve UI with Bootstrap", 0, "2026-01-25"),
    ("Add confirm delete dialog", 1, None),
    ("Implement edit task", 1, "2026-01-16"),
    ("Add persistent filters", 1, None),
    ("Test edge cases", 0, None),
    ("Prepare demo data", 1, None),
    ("Write README.md", 0, "2026-01-30"),
    ("Prepare Upwork description", 0, None),
    ("Clean code and comments", 0, None),
    ("Final UI polish", 0, "2026-01-28"),
    ("Deploy locally for demo", 0, None),
]

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.executemany(
    "INSERT INTO tasks (title, completed, due_date) VALUES (?, ?, ?)",
    tasks
)

conn.commit()
conn.close()

print("✅ Tasks inserted successfully")
