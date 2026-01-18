# 📝 Task Manager Web App (Flask)

A simple **Task Manager Web Application** built with **Python + Flask**, designed as a **junior-level portfolio project** suitable for platforms like **Upwork**.  
The app focuses on clean backend logic, clear UX, and practical features commonly requested by clients.

---

## 🚀 Features

- ✅ Add new tasks
- ✏️ Edit existing tasks
- 🗑 Delete tasks (with confirmation)
- 🔄 Complete / Undo tasks
- 📅 Optional due date for each task
- 🔥 Highlight overdue tasks (red)
- ↕️ Sorting by completion status and due date
- 🔍 Filters:
  - All / Completed / Incomplete
  - Filter by specific due date
  - Combine status + date filters
- 🔁 Persistent filters (filters remain active after actions)
- 💾 SQLite database
- 🎨 Clean UI with Bootstrap

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **SQLite**
- **Jinja2**
- **Bootstrap 5**

---

## 📂 Project Structure

```
TaskManager/
│
├── app.py
├── tasks.db
├── seed_tasks.py
├── clear_tasks.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── edit_task.html
├── static/
│   └── styles.css
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <repo-url>
cd TaskManager
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install flask
```

### 4️⃣ Run the app
```bash
python app.py
```

Open in browser:
```
http://127.0.0.1:5000/
```

---

## 🗃 Database Helpers

### ➕ Seed demo tasks
Adds ~20 realistic demo tasks (completed, pending, overdue, no due date).

```bash
python seed_tasks.py
```

### 🧹 Clear all tasks (keep table)
Deletes all rows without dropping the table.

```bash
python clear_tasks.py
```

---

## 🧠 Key Implementation Details

- Filters are handled via **query parameters** (`GET` request)
- Empty filter values are ignored in the backend
- URL is the **single source of truth** for filters
- Query parameters are preserved across actions (edit, delete, toggle)
- Safe handling of `NULL` / empty due dates

---

## 🎯 Why This Project?

This project demonstrates:
- Clean Flask routing
- CRUD operations
- SQL filtering & sorting
- UX-focused decisions
- Defensive programming (handling edge cases)

Ideal as a **junior-level Upwork portfolio project**.

---

## 📌 Possible Improvements

- User authentication
- Pagination
- Search by title
- Task categories / tags
- REST API version

---

## 👤 Author

Developed by Alexandru Dumitru 
Junior Python / Flask&Django Developer

---

## 📄 License

This project is for learning and portfolio purposes.

