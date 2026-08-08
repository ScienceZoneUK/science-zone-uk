

## 1. Import the libraries

The program starts by importing the tools it needs. 

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import shutil
```

### What each import does

**`tkinter`**

* Python's built-in library for creating graphical interfaces.
* It lets us create the application window.

**`ttk`**

* Provides modern-looking Tkinter widgets such as:

  * Buttons
  * Labels
  * Frames
  * Progress bars
  * Treeviews

**`filedialog`**

* Opens a dialog where the user can select a folder.

**`messagebox`**

* Displays popup messages such as:

  * Warnings
  * Errors
  * Confirmation questions
  * Completion messages

**`Path`**

* Comes from Python's `pathlib`.
* Makes working with files and folders easier.

For example:

```python
folder / "Images"
```

can be used to create a path inside a folder.

**`shutil`**

* Provides file operations.
* This program uses:

```python
shutil.move()
```

to move files.

---

# 2. Create the file categories

The program defines which file extensions belong to which category. 

```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css"],
}
```

This is a **dictionary**.

The structure is:

```text
Category → list of extensions
```

For example:

```python
"Images": [".jpg", ".png", ".gif"]
```

means:

> If a file ends in `.jpg`, `.png`, or `.gif`, classify it as an Image.

Later, the program uses this dictionary to decide where each file should go.

---

# 3. Create the `FileOrganizer` class

The main application is contained inside a class. 

```python
class FileOrganizer:
```

Think of the class as the **blueprint for the entire application**.

Everything related to the application is placed inside it:

* Window setup
* Buttons
* Folder selection
* Scanning
* Organizing
* Clearing
* Progress tracking

---

# 4. Initialize the application

The first method is:

```python
def __init__(self, root):
```

`__init__()` runs automatically when we create a `FileOrganizer` object.

The `root` parameter represents the main Tkinter window.

### Configure the window

```python
self.root = root
self.root.title("File Organizer")
self.root.geometry("850x600")
self.root.minsize(700, 500)
```

This does four things:

1. Saves the window inside the object.
2. Sets the title.
3. Sets the starting size to `850 × 600`.
4. Prevents the window from becoming smaller than `700 × 500`.

---

### Create application variables

```python
self.selected_folder = None
self.files = []
```

Initially:

```python
self.selected_folder = None
```

means:

> The user hasn't selected a folder yet.

And:

```python
self.files = []
```

means:

> We currently have no scanned files.

Then:

```python
self.create_widgets()
```

calls the method responsible for building the interface.

## Your code should look like this
`
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("850x600")
        self.root.minsize(700, 500)

        self.selected_folder = None
        self.files = []

        self.create_widgets()
`

---

# 5. Build the interface

The `create_widgets()` method creates all the visible components of the application. 

The first part creates the header.

```python
header = ttk.Frame(self.root, padding=15)
header.pack(fill="x")
```

A `Frame` is basically a **container**.

You can put widgets inside it.

Then the title is created:

```python
title = ttk.Label(
    header,
    text="📁 File Organizer",
    font=("Arial", 24, "bold")
)
```

This creates a label containing:

```text
📁 File Organizer
```

Then:

```python
title.pack()
```

places it inside the header.

The subtitle works the same way:

```python
subtitle = ttk.Label(
    header,
    text="Organize your files automatically by type"
)
```

---

# 6. Create the folder section

The program creates a labelled container called `"Folder"`. 

```python
folder_frame = ttk.LabelFrame(
    self.root,
    text="Folder",
    padding=10
)
```

Inside it is a label:

```python
self.folder_label = ttk.Label(
    folder_frame,
    text="No folder selected"
)
```

So initially the user sees:

```text
No folder selected
```

Then the Browse button is created:

```python
browse_button = ttk.Button(
    folder_frame,
    text="Browse",
    command=self.select_folder
)
```

The important part is:

```python
command=self.select_folder
```

This means:

> When the user clicks Browse, run `select_folder()`.

Notice there are **no parentheses**:

```python
self.select_folder
```

rather than:

```python
self.select_folder()
```

because we are giving Tkinter the function to call later.

---

# 7. Create the three main buttons

The program creates three buttons. 

### Scan Folder

```python
ttk.Button(
    button_frame,
    text="Scan Folder",
    command=self.scan_folder
)
```

Clicking it calls:

```python
scan_folder()
```

### Organize Files

```python
ttk.Button(
    button_frame,
    text="Organize Files",
    command=self.organize_files
)
```

Clicking it calls:

```python
organize_files()
```

### Clear

```python
ttk.Button(
    button_frame,
    text="Clear",
    command=self.clear
)
```

Clicking it calls:

```python
clear()
```

So the application essentially has three actions:

```text
Browse → Scan → Organize
             ↓
           Clear
```

---

# 8. Create the file list

The program needs somewhere to display the files it finds. 

It creates three columns:

```python
columns = ("File", "Extension", "Category")
```

The Treeview is then created:

```python
self.tree = ttk.Treeview(
    list_frame,
    columns=columns,
    show="headings"
)
```

The columns are given headings:

```python
self.tree.heading("File", text="File Name")
self.tree.heading("Extension", text="Extension")
self.tree.heading("Category", text="Category")
```

So the user sees something like:

| File Name  | Extension | Category  |
| ---------- | --------- | --------- |
| photo.jpg  | .jpg      | Images    |
| report.pdf | .pdf      | Documents |
| song.mp3   | .mp3      | Music     |

---

# 9. Add a scrollbar

The file list may become large, so the program creates a scrollbar. 

```python
scrollbar = ttk.Scrollbar(
    list_frame,
    orient="vertical",
    command=self.tree.yview
)
```

Then the Treeview is connected to it:

```python
self.tree.configure(
    yscrollcommand=scrollbar.set
)
```

This creates the relationship:

```text
Treeview ←→ Scrollbar
```

---

# 10. Create the status label and progress bar

The status label starts with:

```python
text="Ready"
```

This will later change to messages such as:

```text
Folder selected. Click Scan Folder.
```

or:

```text
5 file(s) found.
```

The progress bar is created with:

```python
mode="determinate"
```

That means the program can show actual progress:

```text
[████████████------] 70%
```

---

# 11. Selecting a folder

Now we get to the program's first major function. 

```python
def select_folder(self):
```

It opens the folder-selection dialog:

```python
folder = filedialog.askdirectory(
    title="Select a folder"
)
```

If the user selects a folder:

```python
if folder:
```

the path is converted into a `Path` object:

```python
self.selected_folder = Path(folder)
```

Then the label is updated:

```python
self.folder_label.config(
    text=str(self.selected_folder)
)
```

And the status changes:

```python
self.status_label.config(
    text="Folder selected. Click Scan Folder."
)
```

### Flow

```text
User clicks Browse
        ↓
Folder dialog opens
        ↓
User selects folder
        ↓
Path is stored
        ↓
Folder path appears in GUI
```

---

# 12. Determine a file's category

This method is the heart of the classification system. 

```python
def get_category(self, file_path):
```

First, get the extension:

```python
extension = file_path.suffix.lower()
```

For:

```text
holiday.JPG
```

`.suffix` gives:

```text
.JPG
```

and `.lower()` changes it to:

```text
.jpg
```

This makes the comparison case-insensitive.

Then:

```python
for category, extensions in FILE_CATEGORIES.items():
```

loops through every category.

For example:

```text
Images
Documents
Spreadsheets
Videos
...
```

Then:

```python
if extension in extensions:
```

asks:

> Is this file extension inside the current category's extension list?

If yes:

```python
return category
```

For example:

```python
get_category(photo.jpg)
```

returns:

```text
Images
```

If no category matches:

```python
return "Other"
```

---

# 13. Scan the folder

The scanning process begins here. 

```python
def scan_folder(self):
```

First, it checks whether a folder was selected:

```python
if not self.selected_folder:
```

If not, it displays a warning and stops:

```python
return
```

This is important because the program can't scan a folder if it doesn't know which folder to scan.

---

## Clear previous results

```python
for item in self.tree.get_children():
    self.tree.delete(item)
```

This removes old entries from the file list.

Then:

```python
self.files = []
```

resets the stored file list.

---

## Look through the folder

```python
for item in self.selected_folder.iterdir():
```

`iterdir()` gives the items inside the selected folder.

For example:

```text
Documents
photo.jpg
song.mp3
report.pdf
```

The program checks:

```python
if item.is_file():
```

This is important.

It means:

> Only process files, not folders.

---

# 14. Store and display each file

For every file:

```python
self.files.append(item)
```

stores it in the application's file list.

Then:

```python
category = self.get_category(item)
```

determines its category.

Finally:

```python
self.tree.insert(...)
```

adds it to the GUI.

So one file goes through this process:

```text
photo.jpg
   ↓
get_category()
   ↓
Images
   ↓
Add to Treeview
```

After all files have been processed:

```python
count = len(self.files)
```

counts them.

Then the status becomes something like:

```text
5 file(s) found.
```

---

# 15. Error handling

The scan operation is inside a `try` block.

If the program doesn't have permission to access the folder:

```python
except PermissionError:
```

it displays:

```text
Permission Error
You do not have permission to access this folder.
```

For any other unexpected error:

```python
except Exception as error:
```

the program displays the error message.

This prevents the entire GUI from crashing without explanation.

---

# 16. Organize the files

This is where the actual moving happens. 

```python
def organize_files(self):
```

First it checks:

```python
if not self.selected_folder:
```

Then:

```python
if not self.files:
```

This second check means:

> The user must scan the folder before organizing it.

---

# 17. Ask for confirmation

Before moving anything, the program asks:

```python
answer = messagebox.askyesno(
    "Confirm",
    "Are you sure you want to organize these files?"
)
```

If the user chooses No:

```python
if not answer:
    return
```

The function stops immediately.

This protects the user from accidentally moving files.

---

# 18. Set up progress tracking

The program counts the files:

```python
total = len(self.files)
```

Then creates counters:

```python
moved = 0
errors = 0
```

These track:

```text
Total files
Successfully moved
Files with errors
```

The progress bar is configured:

```python
self.progress["maximum"] = total
self.progress["value"] = 0
```

So if there are 10 files:

```text
Maximum = 10
Current = 0
```

---

# 19. Process every file

The main loop is:

```python
for file_path in self.files:
```

For every file, the program determines its category again:

```python
category = self.get_category(file_path)
```

Then it creates the destination folder:

```python
destination_folder = (
    self.selected_folder / category
)
```

For example:

```text
MyFolder / Images
```

---

# 20. Create the category folder

The program uses:

```python
destination_folder.mkdir(
    exist_ok=True
)
```

This means:

> Create the folder if it doesn't exist.

`exist_ok=True` means the program **doesn't complain if the folder already exists**.

So if:

```text
Images/
```

already exists, it simply uses it.

---

# 21. Create the destination path

The destination is:

```python
destination = destination_folder / file_path.name
```

Suppose the original file is:

```text
C:/Downloads/photo.jpg
```

and its category is:

```text
Images
```

The destination becomes approximately:

```text
C:/Downloads/Images/photo.jpg
```

---

# 22. Prevent overwriting files

Before moving the file, the program checks:

```python
if destination.exists():
```

If a file with the same name already exists, it calls:

```python
destination = self.get_unique_name(destination)
```

So instead of replacing:

```text
photo.jpg
```

it might create:

```text
photo_1.jpg
```

This is an important safety feature.

---

# 23. Move the file

The actual move happens here:

```python
shutil.move(
    str(file_path),
    str(destination)
)
```

This means:

```text
SOURCE
   ↓
photo.jpg

DESTINATION
   ↓
Images/photo.jpg
```

After a successful move:

```python
moved += 1
```

increases the successful-file counter.

---

# 24. Handle errors while moving

If something goes wrong:

```python
except Exception:
    errors += 1
```

The program doesn't stop organizing all the other files.

Instead:

```text
File 1 → moved
File 2 → moved
File 3 → error
File 4 → moved
```

At the end:

```text
Moved: 3
Errors: 1
```

---

# 25. Update the progress bar

After every file:

```python
self.progress["value"] += 1
```

The progress bar moves forward.

Then:

```python
self.root.update_idletasks()
```

tells Tkinter to update the GUI immediately.

Without GUI updates, the progress bar might not visually update until the operation finishes.

---

# 26. Refresh the file list

After all files are processed:

```python
self.scan_folder()
```

is called again.

Why?

Because the files have moved.

The original folder now contains the category folders and potentially no longer contains the files that were just moved.

So scanning again refreshes the displayed list.

---

# 27. Show the final result

The status is updated:

```python
self.status_label.config(
    text=f"Finished: {moved} moved, {errors} errors."
)
```

And a popup displays the results:

```text
Organization complete!

Files moved: 8
Errors: 0
```

---

# 28. Generate unique filenames

The method:

```python
def get_unique_name(self, path):
```

handles duplicate filenames. 

It starts with:

```python
counter = 1
```

Then repeatedly creates a new name:

```python
new_name = (
    f"{path.stem}_{counter}"
    f"{path.suffix}"
)
```

For:

```text
photo.jpg
```

the first attempt is:

```text
photo_1.jpg
```

If that exists, it tries:

```text
photo_2.jpg
```

Then:

```text
photo_3.jpg
```

and continues until it finds an unused name.

The loop:

```python
while True:
```

keeps going until this condition is met:

```python
if not new_path.exists():
    return new_path
```

---

# 29. Clear the application

The `clear()` method resets the program. 

First:

```python
self.selected_folder = None
self.files = []
```

This removes the selected folder and stored files.

Then:

```python
self.folder_label.config(
    text="No folder selected"
)
```

resets the folder display.

The Treeview is cleared:

```python
for item in self.tree.get_children():
    self.tree.delete(item)
```

The progress bar goes back to zero:

```python
self.progress["value"] = 0
```

And finally:

```python
self.status_label.config(
    text="Ready"
)
```

The application is back to its original state.

---

# 30. Start the program

The final section actually launches the application. 

```python
if __name__ == "__main__":
```

This means:

> Only run the following code when this Python file is executed directly.

Then:

```python
root = tk.Tk()
```

creates the main Tkinter window.

The program tries to use the `"clam"` theme:

```python
style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass
```

If that theme isn't available, the program simply continues.

Then:

```python
app = FileOrganizer(root)
```

creates the application.

Finally:

```python
root.mainloop()
```

starts Tkinter's event loop.

This is what keeps the window open and listens for events such as:

```text
Button clicked
Folder selected
Window resized
```

---

# The whole program in one flow

The easiest way to understand the entire code is:

```text
START
  ↓
Create Tkinter window
  ↓
Create FileOrganizer
  ↓
Build GUI
  ↓
User clicks Browse
  ↓
Select folder
  ↓
User clicks Scan Folder
  ↓
Find files
  ↓
Get extension
  ↓
Determine category
  ↓
Display files
  ↓
User clicks Organize Files
  ↓
Ask for confirmation
  ↓
Create category folders
  ↓
Check for duplicate names
  ↓
Move files
  ↓
Update progress
  ↓
Refresh file list
  ↓
Show results
  ↓
END / Wait for another action
```

### The key functions to remember

If you're studying this for coding, focus on these **8 functions** first:

| Function            | Main job                   |
| ------------------- | -------------------------- |
| `__init__()`        | Set up the application     |
| `create_widgets()`  | Build the GUI              |
| `select_folder()`   | Let user choose a folder   |
| `get_category()`    | Decide a file's category   |
| `scan_folder()`     | Find and display files     |
| `organize_files()`  | Move files into categories |
| `get_unique_name()` | Avoid duplicate filenames  |
| `clear()`           | Reset the application      |

The **core logic** is essentially:

```text
SELECT
   ↓
SCAN
   ↓
CLASSIFY
   ↓
CREATE FOLDER
   ↓
CHECK DUPLICATE
   ↓
MOVE
```

That is the main concept behind the entire program.
