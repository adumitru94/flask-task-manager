import sqlite3


conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM tasks where 1=1"
)

conn.commit()
conn.close()

print("✅ Tasks deleted successfully")
