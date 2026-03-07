
# Simple Python + SQLite To-Do App CLI

## 1. Project Structure

```
todo_app/
│
├── main.py
├── database.py
└── todo.db   (created automatically)
```

---

# 2. Database Layer

**database.py**

```python
import sqlite3

DB_NAME = "todo.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def add_task(title):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()


def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks


def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
```

---

# 3. CLI Interface

**main.py**

```python
import database

database.create_table()

while True:
    print("\nTODO APP")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        tasks = database.get_tasks()
        for task in tasks:
            status = "✓" if task[2] else " "
            print(f"{task[0]}. [{status}] {task[1]}")

    elif choice == "2":
        title = input("Task title: ")
        database.add_task(title)

    elif choice == "3":
        task_id = int(input("Task id: "))
        database.complete_task(task_id)

    elif choice == "4":
        task_id = int(input("Task id: "))
        database.delete_task(task_id)

    elif choice == "5":
        break
```

---

# What You Learn From This

SQLite concepts:

* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`

Python concepts:

* functions
* modules
* CLI menus
* database connections

---

# Example Output

```
TODO APP
1. Show tasks
2. Add task
3. Complete task
4. Delete task
5. Exit

Choose: 1

1. [ ] Learn SQLite
2. [✓] Study Python
```

---

💡 **Next step to improve this project**

Add:

* due dates
* priority levels
* show only incomplete tasks
* colored CLI output

---
