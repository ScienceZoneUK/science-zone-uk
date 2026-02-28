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
