
# 📘 **Notepad**

---

# ⭐ MODULE 1 — Project Setup & Tkinter Basics

### 🎯 Goal:

Create the foundation for your Notepad app.

### 📂 Step 1.1 — Create folder + file

```
notepad/
│── main.py
```

### 🧠 Step 1.2 — Basic Tkinter window

```python
import tkinter as tk

root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

root.mainloop()
```

➡ *This creates the empty application window.*

---

# ⭐ MODULE 2 — Convert App into a Class

### 🎯 Goal:

Put the window into a **Notepad class** for better structure.

### Step 2.1 — Build a basic class

```python
import tkinter as tk

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
```

➡ *We now have an OOP structure.*

---

# ⭐ MODULE 3 — Create the Text Editor Area

### 🎯 Goal:

Add the main text box users type in.

### Step 3.1 — Add Text widget

Add inside the class:

```python
def create_widgets(self):
    self.text = tk.Text(self.root, wrap="word", undo=True)
    self.text.pack(fill="both", expand=True)
```

Call it from `__init__`:

```python
self.create_widgets()
```

➡ *Now you can type text in the window!*

---

# ⭐ MODULE 4 — Add a Scrollbar

### 🎯 Goal:

Make the text scrollable.

### Step 4.1 — Wrap Text + Scrollbar in a Frame

```python
frame = tk.Frame(self.root)
frame.pack(fill="both", expand=True)

self.text = tk.Text(frame, wrap="word", undo=True)
self.text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=self.text.yview)
scrollbar.pack(side="right", fill="y")

self.text.config(yscrollcommand=scrollbar.set)
```

➡ *Now you can scroll through long documents.*

---

# ⭐ MODULE 5 — Build the Menu Bar

### 🎯 Goal:

Add File and Edit menus.

### Step 5.1 — Create the menu structure

Inside class:

```python
def create_menu(self):
    menubar = tk.Menu(self.root)

    # FILE MENU
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=self.new_file)
    file_menu.add_command(label="Open", command=self.open_file)
    file_menu.add_command(label="Save", command=self.save_file)
    file_menu.add_command(label="Save As", command=self.save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # EDIT MENU
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Undo", command=self.text.edit_undo)
    edit_menu.add_command(label="Redo", command=self.text.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate("<<Copy>>"))
    edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate("<<Paste>>"))
    menubar.add_cascade(label="Edit", menu=edit_menu)

    self.root.config(menu=menubar)
```

Call from `__init__`:

```python
self.create_menu()
```

➡ *Menus work — but we must implement New/Open/Save next.*

---

# ⭐ MODULE 6 — File Handling (Open, Save, New)

### 🎯 Goal:

Load and save files like a real Notepad.

### Step 6.1 — Add file path tracking

At the top of the class:

```python
self.file_path = None
```

### Step 6.2 — File functions

```python
from tkinter import filedialog

def new_file(self):
    self.text.delete("1.0", "end")
    self.file_path = None
    self.root.title("Notepad - New File")

def open_file(self):
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not path:
        return

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    self.text.delete("1.0", "end")
    self.text.insert("1.0", content)
    self.file_path = path
    self.root.title(f"Notepad - {path}")

def save_file(self):
    if not self.file_path:
        return self.save_as()

    with open(self.file_path, "w", encoding="utf-8") as file:
        file.write(self.text.get("1.0", "end"))

def save_as(self):
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not path:
        return
    self.file_path = path
    self.save_file()
```

➡ *Your Notepad can now Create, Open, Save, Save As.*

---

# ⭐ MODULE 7 — Keyboard Shortcuts

### 🎯 Goal:

Make the app feel professional like real Notepad.

```python
def bind_shortcuts(self):
    self.root.bind("<Control-n>", lambda e: self.new_file())
    self.root.bind("<Control-o>", lambda e: self.open_file())
    self.root.bind("<Control-s>", lambda e: self.save_file())
    self.root.bind("<Control-S>", lambda e: self.save_as())
    self.root.bind("<Control-q>", lambda e: self.root.quit())

    self.root.bind("<Control-z>", lambda e: self.text.edit_undo())
    self.root.bind("<Control-y>", lambda e: self.text.edit_redo())
```

Call in `__init__`:

```python
self.bind_shortcuts()
```

➡ *You now have shortcuts just like Windows Notepad.*

---

# ⭐ MODULE 8 — Status Bar (Optional but Recommended)

### 🎯 Goal:

Display info like “Saved”, “New File”, etc.

```python
self.status = tk.Label(self.root, text="Ready", anchor="w")
self.status.pack(side="bottom", fill="x")
```

Update status in file functions:

```python
self.status.config(text="Saved file")
```

➡ *Helps users know what's happening.*

---

# 🎉 END OF COURSE — COMPLETE NOTEPAD!

You now have a working, class-based, professional Notepad clone.

---
