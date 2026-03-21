
# 📂 `open()` — Opening a File

### 🔹 What it does:

`open()` is used to **open a file so your program can work with it**.

### 🔹 Basic syntax:

```python
file = open("students.txt", "r")
```

### 🔹 Two important parts:

1. **File name** → `"students.txt"`
2. **Mode** → `"r"` (how you want to use the file)

---

## 🔑 Common Modes

| Mode  | Meaning                 |
| ----- | ----------------------- |
| `"r"` | Read (file must exist)  |
| `"w"` | Write (overwrites file) |
| `"a"` | Append (adds to file)   |
| `"x"` | Create new file         |

---

## ✅ Example:

```python
f = open("students.txt", "r")
```

👉 Opens file for reading

---

# 📖 `read()` — Reading from a File

### 🔹 What it does:

Reads the **content of the file**.

---

## 🔹 Example:

```python
f = open("students.txt", "r")
content = f.read()
print(content)
f.close()
```

### 🧠 Output:

If file contains:

```
101,John,A
102,Sara,B
```

You’ll get:

```
101,John,A
102,Sara,B
```

---

## 🔹 Other useful read methods:

### 1. Read one line:

```python
f.readline()
```

### 2. Read all lines as a list:

```python
f.readlines()
```

Example output:

```python
['101,John,A\n', '102,Sara,B\n']
```

---

# ✍️ `write()` — Writing to a File

### 🔹 What it does:

Writes data **into a file**.

---

## 🔹 Example:

```python
f = open("students.txt", "w")
f.write("101,John,A")
f.close()
```

### ⚠️ Important:

* `"w"` mode will **erase everything in the file first**

---

## 🔹 Append instead (safer):

```python
f = open("students.txt", "a")
f.write("\n102,Sara,B")
f.close()
```

👉 This adds new data instead of deleting old data.

---

# 🔁 Best Practice (Very Important)

Use `with open()` instead of manually closing files:

```python
with open("students.txt", "r") as f:
    content = f.read()
    print(content)
```

### ✅ Why?

* Automatically closes file
* Cleaner and safer

---



Think of a file like a notebook 📓:

* `open()` → Opening the notebook
* `read()` → Reading what's written
* `write()` → Writing new notes
* `"a"` mode → Adding notes at the end
* `"w"` mode → Erasing and rewriting everything

---

# ⚡ Quick Summary

```python
# Read
with open("file.txt", "r") as f:
    print(f.read())

# Write (overwrite)
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("\nNew line")
```




# Student Record





```
ID,Name,Grade
```

### Example (`students.txt`)

```
101,John,A
102,Sara,B
103,Ali,C
```

---

# 🧱 Full Python Project Using `.txt`

Here’s a clean working version:

```python
FILE_NAME = "students.txt"

# Add student
def add_student():
    with open(FILE_NAME, "a") as f:
        student_id = input("Enter ID: ")
        name = input("Enter name: ")
        grade = input("Enter grade: ")

        f.write(f"{student_id},{name},{grade}\n")
    
    print("✅ Student added!")
```

```python
# View students
def view_students():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            
            if not lines:
                print("No records found.")
                return

            for line in lines:
                student_id, name, grade = line.strip().split(",")
                print(f"ID: {student_id} | Name: {name} | Grade: {grade}")
    except FileNotFoundError:
        print("File not found.")
```
```python
# Search student
def search_student():
    student_id = input("Enter ID to search: ")

    with open(FILE_NAME, "r") as f:
        for line in f:
            sid, name, grade = line.strip().split(",")
            if sid == student_id:
                print(f"Found: {sid}, {name}, {grade}")
                return

    print("❌ Student not found.")
```
```python
# Delete student
def delete_student():
    student_id = input("Enter ID to delete: ")

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        found = False
        for line in lines:
            sid, name, grade = line.strip().split(",")
            if sid != student_id:
                f.write(line)
            else:
                found = True

    if found:
        print("🗑️ Student deleted.")
    else:
        print("❌ Student not found.")
```
```python
# Menu
def menu():
    while True:
        print("\n--- Student Record System (TXT) ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

menu()
```

---


# ⚠️ Important Limitation of `.txt`

* You must manually:

  * Split data (`split(",")`)
  * Handle errors
* If format breaks → program breaks

---
