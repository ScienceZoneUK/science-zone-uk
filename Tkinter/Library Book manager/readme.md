
This code builds a **simple Library Book Manager desktop application** using:

* `sqlite3` → for the database
* `tkinter` → for the graphical user interface (GUI)
* `ttk` → for styled widgets like tables and comboboxes

It lets you **add, view, update, delete, and search books** stored in a local database file.

---
# Basic Requirements

```python
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


root.mainloop()

```


# 1️⃣ Database Setup

```python
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
```

* Creates (or opens) a SQLite database file named **library.db**
* `cursor` is used to execute SQL commands

### Table Creation XDo not copy this bit its a breakdown of the code you'll see ahead

```sql
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    status TEXT DEFAULT 'Available'
)
```

This creates a table called `books` with:

| Column   | Purpose                                         |
| -------- | ----------------------------------------------- |
| `id`     | Unique ID (auto-incremented)                    |
| `title`  | Book title (required)                           |
| `author` | Author name (required)                          |
| `year`   | Publication year                                |
| `status` | "Available" or "Borrowed" (default = Available) |

---


```python
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Database Setup ----------
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    status TEXT DEFAULT 'Available'
)
""")
conn.commit()



root.mainloop()

```

# 2️⃣ Core Functions (App Logic)

## ➕ `add_book()`

* Validates that Title and Author are not empty.
* Inserts a new book into the database.
* Refreshes the table.
* Clears input fields.

Uses parameterized SQL:

```python
VALUES (?, ?, ?, ?)
```

This prevents SQL injection.

---

## 👀 `view_books()`

* Clears all rows from the table widget.
* Fetches all records from the database.
* Inserts them into the Treeview.

This keeps the UI synced with the database.

---

## ❌ `delete_book()`

* Gets selected row from the table.
* Deletes it from the database using its ID.
* Refreshes the table.

---

## ✏️ `update_book()`

* Gets selected row ID.
* Updates that record with new values from input fields.
* Refreshes the table.

---

## 🔍 `search_book()`

* Clears the table.
* Searches books where:

  * title contains search text OR
  * author contains search text
* Uses SQL `LIKE` with `%` wildcard.

Example:

```sql
WHERE title LIKE '%text%' OR author LIKE '%text%'
```

---

## 🖱 `select_book(event)`

Triggered when user clicks a row.

* Gets selected row values
* Fills the input fields with that row’s data
* Makes editing easier

---

## 🧹 `clear_fields()`

Resets input fields after adding a book.

---




```python

# ---------- Functions ----------

def add_book():
    if title_var.get() == "" or author_var.get() == "":
        messagebox.showerror("Error", "Title and Author required!")
        return
    
    cursor.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)",
                   (title_var.get(), author_var.get(), year_var.get(), status_var.get()))
    conn.commit()
    view_books()
    clear_fields()

def view_books():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def delete_book():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    cursor.execute("DELETE FROM books WHERE id=?", (values[0],))
    conn.commit()
    view_books()

def update_book():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")

    cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?, status=?
        WHERE id=?
    """, (title_var.get(), author_var.get(), year_var.get(), status_var.get(), values[0]))
    conn.commit()
    view_books()

def search_book():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                   ('%'+search_var.get()+'%', '%'+search_var.get()+'%'))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def select_book(event):
    selected = tree.focus()
    values = tree.item(selected, "values")
    if values:
        title_var.set(values[1])
        author_var.set(values[2])
        year_var.set(values[3])
        status_var.set(values[4])

def clear_fields():
    title_var.set("")
    author_var.set("")
    year_var.set("")
    status_var.set("Available")


```
# 3️⃣ GUI Setup (Tkinter Interface)

## Main Window

```python
root = tk.Tk()
root.title("Library Book Manager")
root.geometry("800x500")
```

Creates the main window.

---

## Tkinter Variables

```python
title_var = tk.StringVar()
```

These store dynamic values connected to input fields.

Why use them?

* Automatically sync between Entry widgets and variables.

---

## Input Fields

```python
tk.Entry(root, textvariable=title_var)
```

* Labels + Entry widgets
* Status uses `ttk.Combobox` with choices:

  * Available
  * Borrowed

---

## Buttons

Each button connects to a function:

```python
tk.Button(root, text="Add Book", command=add_book)
```

When clicked → function runs.

---

## 📊 Table (Treeview)

```python
tree = ttk.Treeview(...)
```

Displays books in a table format.

Columns:

* ID
* Title
* Author
* Year
* Status

```python
tree.bind("<ButtonRelease-1>", select_book)
```

When user clicks a row → `select_book()` runs.

---

# 4️⃣ App Flow

When program starts:

1. Database is created (if not exists)
2. GUI loads
3. `view_books()` runs → displays saved books
4. `root.mainloop()` starts the app event loop

The app stays running until user closes it.

---

# 5️⃣ What This Program Demonstrates

✅ SQLite database integration
✅ CRUD operations (Create, Read, Update, Delete)
✅ Search functionality
✅ Tkinter GUI development
✅ Event-driven programming
✅ Parameterized SQL (secure queries)

---

# 6️⃣ Overall Architecture

```
User Action → Button Click → Function → SQL Query → Refresh Table
```

The GUI and database are tightly connected:

* GUI updates database
* Database updates GUI

---


```python


# ---------- GUI Setup ----------

root = tk.Tk()
root.title("Library Book Manager")
root.geometry("800x500")

title_var = tk.StringVar()
author_var = tk.StringVar()
year_var = tk.StringVar()
status_var = tk.StringVar(value="Available")
search_var = tk.StringVar()

# Labels & Entries
tk.Label(root, text="Title").pack()
tk.Entry(root, textvariable=title_var).pack()

tk.Label(root, text="Author").pack()
tk.Entry(root, textvariable=author_var).pack()

tk.Label(root, text="Year").pack()
tk.Entry(root, textvariable=year_var).pack()

tk.Label(root, text="Status").pack()
ttk.Combobox(root, textvariable=status_var, values=["Available", "Borrowed"]).pack()

# Buttons
tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Update Book", command=update_book).pack(pady=5)
tk.Button(root, text="Delete Book", command=delete_book).pack(pady=5)

tk.Entry(root, textvariable=search_var).pack(pady=5)
tk.Button(root, text="Search", command=search_book).pack(pady=5)

# Table
tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Year", "Status"), show="headings")
for col in ("ID", "Title", "Author", "Year", "Status"):
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", select_book)

view_books()

root.mainloop()

```
#  Possible Improvements

You could enhance it by adding:

* Input validation for year (only numbers)
* Confirmation before deleting
  

<!---
```python
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Database Setup ----------
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    status TEXT DEFAULT 'Available'
)
""")
conn.commit()

# ---------- Functions ----------

def add_book():
    if title_var.get() == "" or author_var.get() == "":
        messagebox.showerror("Error", "Title and Author required!")
        return
    
    cursor.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)",
                   (title_var.get(), author_var.get(), year_var.get(), status_var.get()))
    conn.commit()
    view_books()
    clear_fields()

def view_books():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def delete_book():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    cursor.execute("DELETE FROM books WHERE id=?", (values[0],))
    conn.commit()
    view_books()

def update_book():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")

    cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?, status=?
        WHERE id=?
    """, (title_var.get(), author_var.get(), year_var.get(), status_var.get(), values[0]))
    conn.commit()
    view_books()

def search_book():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                   ('%'+search_var.get()+'%', '%'+search_var.get()+'%'))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def select_book(event):
    selected = tree.focus()
    values = tree.item(selected, "values")
    if values:
        title_var.set(values[1])
        author_var.set(values[2])
        year_var.set(values[3])
        status_var.set(values[4])

def clear_fields():
    title_var.set("")
    author_var.set("")
    year_var.set("")
    status_var.set("Available")

# ---------- GUI Setup ----------

root = tk.Tk()
root.title("Library Book Manager")
root.geometry("800x500")

title_var = tk.StringVar()
author_var = tk.StringVar()
year_var = tk.StringVar()
status_var = tk.StringVar(value="Available")
search_var = tk.StringVar()

# Labels & Entries
tk.Label(root, text="Title").pack()
tk.Entry(root, textvariable=title_var).pack()

tk.Label(root, text="Author").pack()
tk.Entry(root, textvariable=author_var).pack()

tk.Label(root, text="Year").pack()
tk.Entry(root, textvariable=year_var).pack()

tk.Label(root, text="Status").pack()
ttk.Combobox(root, textvariable=status_var, values=["Available", "Borrowed"]).pack()

# Buttons
tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Update Book", command=update_book).pack(pady=5)
tk.Button(root, text="Delete Book", command=delete_book).pack(pady=5)

tk.Entry(root, textvariable=search_var).pack(pady=5)
tk.Button(root, text="Search", command=search_book).pack(pady=5)

# Table
tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Year", "Status"), show="headings")
for col in ("ID", "Title", "Author", "Year", "Status"):
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", select_book)

view_books()

root.mainloop()

```


-->
