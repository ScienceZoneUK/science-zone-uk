# 🧾 Project: Personal Notes Manager (File Save & Read)

This project lets you:

* Write notes and save them to a file
* Read saved notes later
* Keep everything stored locally

---

## 💡 What you’ll learn

* `open()` function
* Writing to files (`"w"` and `"a"` modes)
* Reading files (`"r"` mode)
* Basic user input

---

## Step 1 🧑‍💻 Code

```python
def write_note():
    note = input("Write your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("✅ Note saved!\n")
```


```python

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            print("\n📒 Your Notes:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("⚠️ No notes found yet.\n")

```

```python
def main():
    while True:
        print("=== Notes Manager ===")
        print("1. Add a note")
        print("2. View notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            write_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.\n")


main()
```

---

## ▶️ How it works

* `"a"` mode → adds new notes without deleting old ones
* `"r"` mode → reads saved notes
* File (`notes.txt`) is created automatically if it doesn’t exist

---

## Step 2

Once this works, you can level it up:

* Add **timestamps** to notes
  
* Delete a specific note

* Build a **GUI app** using `tkinter`
