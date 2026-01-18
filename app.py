import sqlite3

from flask import Flask, render_template
from flask import request, redirect, url_for
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    status = request.args.get("status")
    date_filter = request.args.get("date")
    if not date_filter:
        date_filter = None

    print("STATUS:", status)
    print("DATE:", date_filter)

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if status == "completed":
        query += " AND completed = 1"
    elif status == "pending":
        query += " AND completed = 0"

    if date_filter is not None:
        query += " AND due_date = ?"
        params.append(date_filter)

    query += """
        ORDER BY
            completed ASC,
            due_date ASC
    """

    conn = get_db_connection()
    tasks = conn.execute(query, params).fetchall()
    conn.close()

    from datetime import date
    today = date.today().isoformat()

    return render_template(
        "index.html",
        tasks=tasks,
        today=today
    )




def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            due_date TEXT
        )
    """)
    conn.commit()
    conn.close()
    
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    due_date = request.form.get("due_date")

    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (title, due_date) VALUES (?,?)", (title, due_date))
    conn.commit()
    conn.close()

    return redirect(url_for("index", **request.args))

@app.route("/toggle/<int:id>")
def toggle_task(id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT completed FROM tasks WHERE id = ?",
        (id,)
    ).fetchone()

    new_status = 0 if task["completed"] else 1

    conn.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index", **request.args))


@app.route("/delete/<int:id>")
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index", **request.args))
    
    
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    conn = get_db_connection()

    if request.method == "POST":
        title = request.form["title"]
        due_date = request.form.get("due_date")
        
        conn.execute(
            "UPDATE tasks SET title = ?, due_date = ? WHERE id = ?",
            (title, due_date, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index", **request.args))

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()

    return render_template("edit_task.html", task=task)



if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    
    