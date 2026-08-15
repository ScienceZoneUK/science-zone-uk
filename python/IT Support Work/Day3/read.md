# IT Ticketing System
When staff have an IT related issue / problem they raise tickets documenting the issues they are facing this helps the IT support keep track of what is going on.
# Necessary Imports
```
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path


```
# Setting up the file location
```python
TICKET_FILE = Path("tickets.txt")
```
This could also be stored in a separate location if you're feeling fancy
```python
TICKET_FILE = Path("NEWLOCATION/tickets.txt")
```
Main window
```python
root = tk.Tk()
root.title("IT Support Ticket Generator")
root.geometry("950x650")
root.minsize(800, 550)


```
# Variables
```python
name_var = tk.StringVar()
email_var = tk.StringVar()
category_var = tk.StringVar()
priority_var = tk.StringVar(value="Medium")
search_var = tk.StringVar()

```
# Ticket ID
```python
def get_next_ticket_id():
    """Generate the next ticket ID."""

    if not TICKET_FILE.exists():
        return 1

    try:
        text = TICKET_FILE.read_text(encoding="utf-8")

        ids = []

        for line in text.splitlines():
            if line.startswith("Ticket ID:"):
                try:
                    ticket_id = int(
                        line.split(":")[1].strip()
                    )
                    ids.append(ticket_id)
                except ValueError:
                    pass

        if ids:
            return max(ids) + 1

    except Exception:
        pass

    return 1

```
# Create Ticket
```python
def create_ticket():
    name = name_var.get().strip()
    email = email_var.get().strip()
    category = category_var.get().strip()
    priority = priority_var.get()
    issue = issue_text.get("1.0", tk.END).strip()

    # Validation
    if not name:
        messagebox.showerror(
            "Missing Information",
            "Please enter your name."
        )
        return

    if not email:
        messagebox.showerror(
            "Missing Information",
            "Please enter your email address."
        )
        return

    if not category:
        messagebox.showerror(
            "Missing Information",
            "Please select a category."
        )
        return

    if not issue:
        messagebox.showerror(
            "Missing Information",
            "Please describe the problem."
        )
        return

    # Generate ticket information
    ticket_id = get_next_ticket_id()

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Ticket text
    ticket = f"""
==================================================
Ticket ID: {ticket_id}
Date: {current_time}
Name: {name}
Email: {email}
Category: {category}
Priority: {priority}
Status: Open

Problem:
{issue}

==================================================

"""

    try:
        with open(
            TICKET_FILE,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(ticket)

    except Exception as error:
        messagebox.showerror(
            "File Error",
            f"Could not save ticket:\n{error}"
        )
        return

    messagebox.showinfo(
        "Ticket Created",
        f"Ticket #{ticket_id} created successfully!"
    )

    clear_form()
    load_tickets()

```
# Clear Form
```python
def clear_form():
    name_var.set("")
    email_var.set("")
    category_var.set("")
    priority_var.set("Medium")

    issue_text.delete(
        "1.0",
        tk.END
    )

```
# Load Tickets
```python
def load_tickets():
    """Load saved tickets into the table."""

    for item in ticket_tree.get_children():
        ticket_tree.delete(item)

    if not TICKET_FILE.exists():
        return

    try:
        text = TICKET_FILE.read_text(
            encoding="utf-8"
        )

        blocks = text.split(
            "=================================================="
        )

        for block in blocks:

            if "Ticket ID:" not in block:
                continue

            ticket_id = get_value(
                block,
                "Ticket ID:"
            )

            date_time = get_value(
                block,
                "Date:"
            )

            name = get_value(
                block,
                "Name:"
            )

            category = get_value(
                block,
                "Category:"
            )

            priority = get_value(
                block,
                "Priority:"
            )

            status = get_value(
                block,
                "Status:"
            )

            ticket_tree.insert(
                "",
                "end",
                values=(
                    ticket_id,
                    date_time,
                    name,
                    category,
                    priority,
                    status
                )
            )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not load tickets:\n{error}"
        )


```
# GET VALUE FROM TICKET

```python
def get_value(block, label):
    """Extract a value from a ticket block."""

    for line in block.splitlines():

        line = line.strip()

        if line.startswith(label):
            return line[len(label):].strip()

    return ""

```
# SEARCH TICKETS
```python

def search_tickets(*args):
    """Search tickets by name, category or priority."""

    search = search_var.get().lower().strip()

    for item in ticket_tree.get_children():
        ticket_tree.delete(item)

    if not TICKET_FILE.exists():
        return

    try:
        text = TICKET_FILE.read_text(
            encoding="utf-8"
        )

        blocks = text.split(
            "=================================================="
        )

        for block in blocks:

            if "Ticket ID:" not in block:
                continue

            ticket_id = get_value(
                block,
                "Ticket ID:"
            )

            date_time = get_value(
                block,
                "Date:"
            )

            name = get_value(
                block,
                "Name:"
            )

            category = get_value(
                block,
                "Category:"
            )

            priority = get_value(
                block,
                "Priority:"
            )

            status = get_value(
                block,
                "Status:"
            )

            searchable = (
                ticket_id
                + " "
                + name
                + " "
                + category
                + " "
                + priority
                + " "
                + status
            ).lower()

            if search in searchable:

                ticket_tree.insert(
                    "",
                    "end",
                    values=(
                        ticket_id,
                        date_time,
                        name,
                        category,
                        priority,
                        status
                    )
                )

    except Exception as error:
        messagebox.showerror(
            "Search Error",
            str(error)
        )


```
# VIEW SELECTED TICKET
```python
def view_ticket():
    selected = ticket_tree.selection()

    if not selected:
        messagebox.showwarning(
            "No Ticket Selected",
            "Please select a ticket first."
        )
        return

    item = ticket_tree.item(
        selected[0]
    )

    ticket_id = item["values"][0]

    if not TICKET_FILE.exists():
        return

    text = TICKET_FILE.read_text(
        encoding="utf-8"
    )

    blocks = text.split(
        "=================================================="
    )

    for block in blocks:

        if f"Ticket ID: {ticket_id}" in block:

            show_ticket_window(
                block.strip()
            )

            return

```
# TICKET DETAILS WINDOW
```python

def show_ticket_window(ticket):
    window = tk.Toplevel(root)

    window.title("Ticket Details")
    window.geometry("600x500")

    text_box = tk.Text(
        window,
        wrap="word",
        font=("Arial", 11)
    )

    text_box.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    text_box.insert(
        "1.0",
        ticket
    )

    text_box.config(
        state="disabled"
    )



```

# Header
```python
header = ttk.Frame(
    root,
    padding=15
)

header.pack(fill="x")

ttk.Label(
    header,
    text="🎫 IT Support Ticket Generator",
    font=("Arial", 24, "bold")
).pack()

ttk.Label(
    header,
    text="Create and manage IT support requests"
).pack(pady=5)

```


# CREATE TICKET FORM

```python
form = ttk.LabelFrame(
    root,
    text="Create New Ticket",
    padding=15
)

form.pack(
    fill="x",
    padx=15,
    pady=10
)


# Name
ttk.Label(
    form,
    text="Name:"
).grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

ttk.Entry(
    form,
    textvariable=name_var,
    width=30
).grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Email
ttk.Label(
    form,
    text="Email:"
).grid(
    row=0,
    column=2,
    sticky="w",
    padx=5,
    pady=5
)

ttk.Entry(
    form,
    textvariable=email_var,
    width=30
).grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# Category
ttk.Label(
    form,
    text="Category:"
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

category_combo = ttk.Combobox(
    form,
    textvariable=category_var,
    values=[
        "Hardware",
        "Software",
        "Network",
        "Printer",
        "Email",
        "Account/Login",
        "Security",
        "Other"
    ],
    state="readonly",
    width=28
)

category_combo.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# Priority
ttk.Label(
    form,
    text="Priority:"
).grid(
    row=1,
    column=2,
    sticky="w",
    padx=5,
    pady=5
)

priority_combo = ttk.Combobox(
    form,
    textvariable=priority_var,
    values=[
        "Low",
        "Medium",
        "High",
        "Critical"
    ],
    state="readonly",
    width=28
)

priority_combo.grid(
    row=1,
    column=3,
    padx=5,
    pady=5
)


# Problem
ttk.Label(
    form,
    text="Problem:"
).grid(
    row=2,
    column=0,
    sticky="nw",
    padx=5,
    pady=5
)

issue_text = tk.Text(
    form,
    width=65,
    height=5,
    font=("Arial", 10)
)

issue_text.grid(
    row=2,
    column=1,
    columnspan=3,
    padx=5,
    pady=5
)


# Buttons
button_frame = ttk.Frame(form)

button_frame.grid(
    row=3,
    column=0,
    columnspan=4,
    pady=10
)

ttk.Button(
    button_frame,
    text="Create Ticket",
    command=create_ticket
).pack(
    side="left",
    padx=5
)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_form
).pack(
    side="left",
    padx=5
)
```


# SEARCH

```
search_frame = ttk.Frame(
    root,
    padding=(15, 5)
)

search_frame.pack(
    fill="x"
)

ttk.Label(
    search_frame,
    text="Search Tickets:"
).pack(
    side="left",
    padx=5
)

search_entry = ttk.Entry(
    search_frame,
    textvariable=search_var,
    width=40
)

search_entry.pack(
    side="left",
    padx=5
)

search_var.trace_add(
    "write",
    search_tickets
)
```


# TICKET TABLE

```python
table_frame = ttk.LabelFrame(
    root,
    text="Support Tickets",
    padding=10
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

columns = (
    "ID",
    "Date",
    "Name",
    "Category",
    "Priority",
    "Status"
)

ticket_tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    ticket_tree.heading(
        column,
        text=column
    )

ticket_tree.column(
    "ID",
    width=60
)

ticket_tree.column(
    "Date",
    width=150
)

ticket_tree.column(
    "Name",
    width=150
)

ticket_tree.column(
    "Category",
    width=130
)

ticket_tree.column(
    "Priority",
    width=100
)

ticket_tree.column(
    "Status",
    width=100
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=ticket_tree.yview
)

ticket_tree.configure(
    yscrollcommand=scrollbar.set
)

ticket_tree.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

```

# VIEW BUTTON

```python
ttk.Button(
    root,
    text="View Selected Ticket",
    command=view_ticket
).pack(
    pady=(0, 15)
)
```


# LOAD EXISTING TICKETS

```python
load_tickets()
```


# START APPLICATION

```python
root.mainloop()
```
```python

```


```python
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path


# ==========================================
# FILE SETTINGS
# ==========================================

TICKET_FILE = Path("tickets.txt")


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()
root.title("IT Support Ticket Generator")
root.geometry("950x650")
root.minsize(800, 550)


# ==========================================
# VARIABLES
# ==========================================

name_var = tk.StringVar()
email_var = tk.StringVar()
category_var = tk.StringVar()
priority_var = tk.StringVar(value="Medium")
search_var = tk.StringVar()


# ==========================================
# TICKET ID
# ==========================================

def get_next_ticket_id():
    """Generate the next ticket ID."""

    if not TICKET_FILE.exists():
        return 1

    try:
        text = TICKET_FILE.read_text(encoding="utf-8")

        ids = []

        for line in text.splitlines():
            if line.startswith("Ticket ID:"):
                try:
                    ticket_id = int(
                        line.split(":")[1].strip()
                    )
                    ids.append(ticket_id)
                except ValueError:
                    pass

        if ids:
            return max(ids) + 1

    except Exception:
        pass

    return 1


# ==========================================
# CREATE TICKET
# ==========================================

def create_ticket():
    name = name_var.get().strip()
    email = email_var.get().strip()
    category = category_var.get().strip()
    priority = priority_var.get()
    issue = issue_text.get("1.0", tk.END).strip()

    # Validation
    if not name:
        messagebox.showerror(
            "Missing Information",
            "Please enter your name."
        )
        return

    if not email:
        messagebox.showerror(
            "Missing Information",
            "Please enter your email address."
        )
        return

    if not category:
        messagebox.showerror(
            "Missing Information",
            "Please select a category."
        )
        return

    if not issue:
        messagebox.showerror(
            "Missing Information",
            "Please describe the problem."
        )
        return

    # Generate ticket information
    ticket_id = get_next_ticket_id()

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Ticket text
    ticket = f"""
==================================================
Ticket ID: {ticket_id}
Date: {current_time}
Name: {name}
Email: {email}
Category: {category}
Priority: {priority}
Status: Open

Problem:
{issue}

==================================================

"""

    try:
        with open(
            TICKET_FILE,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(ticket)

    except Exception as error:
        messagebox.showerror(
            "File Error",
            f"Could not save ticket:\n{error}"
        )
        return

    messagebox.showinfo(
        "Ticket Created",
        f"Ticket #{ticket_id} created successfully!"
    )

    clear_form()
    load_tickets()


# ==========================================
# CLEAR FORM
# ==========================================

def clear_form():
    name_var.set("")
    email_var.set("")
    category_var.set("")
    priority_var.set("Medium")

    issue_text.delete(
        "1.0",
        tk.END
    )


# ==========================================
# LOAD TICKETS
# ==========================================

def load_tickets():
    """Load saved tickets into the table."""

    for item in ticket_tree.get_children():
        ticket_tree.delete(item)

    if not TICKET_FILE.exists():
        return

    try:
        text = TICKET_FILE.read_text(
            encoding="utf-8"
        )

        blocks = text.split(
            "=================================================="
        )

        for block in blocks:

            if "Ticket ID:" not in block:
                continue

            ticket_id = get_value(
                block,
                "Ticket ID:"
            )

            date_time = get_value(
                block,
                "Date:"
            )

            name = get_value(
                block,
                "Name:"
            )

            category = get_value(
                block,
                "Category:"
            )

            priority = get_value(
                block,
                "Priority:"
            )

            status = get_value(
                block,
                "Status:"
            )

            ticket_tree.insert(
                "",
                "end",
                values=(
                    ticket_id,
                    date_time,
                    name,
                    category,
                    priority,
                    status
                )
            )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not load tickets:\n{error}"
        )


# ==========================================
# GET VALUE FROM TICKET
# ==========================================

def get_value(block, label):
    """Extract a value from a ticket block."""

    for line in block.splitlines():

        line = line.strip()

        if line.startswith(label):
            return line[len(label):].strip()

    return ""


# ==========================================
# SEARCH TICKETS
# ==========================================

def search_tickets(*args):
    """Search tickets by name, category or priority."""

    search = search_var.get().lower().strip()

    for item in ticket_tree.get_children():
        ticket_tree.delete(item)

    if not TICKET_FILE.exists():
        return

    try:
        text = TICKET_FILE.read_text(
            encoding="utf-8"
        )

        blocks = text.split(
            "=================================================="
        )

        for block in blocks:

            if "Ticket ID:" not in block:
                continue

            ticket_id = get_value(
                block,
                "Ticket ID:"
            )

            date_time = get_value(
                block,
                "Date:"
            )

            name = get_value(
                block,
                "Name:"
            )

            category = get_value(
                block,
                "Category:"
            )

            priority = get_value(
                block,
                "Priority:"
            )

            status = get_value(
                block,
                "Status:"
            )

            searchable = (
                ticket_id
                + " "
                + name
                + " "
                + category
                + " "
                + priority
                + " "
                + status
            ).lower()

            if search in searchable:

                ticket_tree.insert(
                    "",
                    "end",
                    values=(
                        ticket_id,
                        date_time,
                        name,
                        category,
                        priority,
                        status
                    )
                )

    except Exception as error:
        messagebox.showerror(
            "Search Error",
            str(error)
        )


# ==========================================
# VIEW SELECTED TICKET
# ==========================================

def view_ticket():
    selected = ticket_tree.selection()

    if not selected:
        messagebox.showwarning(
            "No Ticket Selected",
            "Please select a ticket first."
        )
        return

    item = ticket_tree.item(
        selected[0]
    )

    ticket_id = item["values"][0]

    if not TICKET_FILE.exists():
        return

    text = TICKET_FILE.read_text(
        encoding="utf-8"
    )

    blocks = text.split(
        "=================================================="
    )

    for block in blocks:

        if f"Ticket ID: {ticket_id}" in block:

            show_ticket_window(
                block.strip()
            )

            return


# ==========================================
# TICKET DETAILS WINDOW
# ==========================================

def show_ticket_window(ticket):
    window = tk.Toplevel(root)

    window.title("Ticket Details")
    window.geometry("600x500")

    text_box = tk.Text(
        window,
        wrap="word",
        font=("Arial", 11)
    )

    text_box.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    text_box.insert(
        "1.0",
        ticket
    )

    text_box.config(
        state="disabled"
    )


# ==========================================
# HEADER
# ==========================================

header = ttk.Frame(
    root,
    padding=15
)

header.pack(fill="x")

ttk.Label(
    header,
    text="🎫 IT Support Ticket Generator",
    font=("Arial", 24, "bold")
).pack()

ttk.Label(
    header,
    text="Create and manage IT support requests"
).pack(pady=5)


# ==========================================
# CREATE TICKET FORM
# ==========================================

form = ttk.LabelFrame(
    root,
    text="Create New Ticket",
    padding=15
)

form.pack(
    fill="x",
    padx=15,
    pady=10
)


# Name
ttk.Label(
    form,
    text="Name:"
).grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

ttk.Entry(
    form,
    textvariable=name_var,
    width=30
).grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Email
ttk.Label(
    form,
    text="Email:"
).grid(
    row=0,
    column=2,
    sticky="w",
    padx=5,
    pady=5
)

ttk.Entry(
    form,
    textvariable=email_var,
    width=30
).grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# Category
ttk.Label(
    form,
    text="Category:"
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

category_combo = ttk.Combobox(
    form,
    textvariable=category_var,
    values=[
        "Hardware",
        "Software",
        "Network",
        "Printer",
        "Email",
        "Account/Login",
        "Security",
        "Other"
    ],
    state="readonly",
    width=28
)

category_combo.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# Priority
ttk.Label(
    form,
    text="Priority:"
).grid(
    row=1,
    column=2,
    sticky="w",
    padx=5,
    pady=5
)

priority_combo = ttk.Combobox(
    form,
    textvariable=priority_var,
    values=[
        "Low",
        "Medium",
        "High",
        "Critical"
    ],
    state="readonly",
    width=28
)

priority_combo.grid(
    row=1,
    column=3,
    padx=5,
    pady=5
)


# Problem
ttk.Label(
    form,
    text="Problem:"
).grid(
    row=2,
    column=0,
    sticky="nw",
    padx=5,
    pady=5
)

issue_text = tk.Text(
    form,
    width=65,
    height=5,
    font=("Arial", 10)
)

issue_text.grid(
    row=2,
    column=1,
    columnspan=3,
    padx=5,
    pady=5
)


# Buttons
button_frame = ttk.Frame(form)

button_frame.grid(
    row=3,
    column=0,
    columnspan=4,
    pady=10
)

ttk.Button(
    button_frame,
    text="Create Ticket",
    command=create_ticket
).pack(
    side="left",
    padx=5
)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_form
).pack(
    side="left",
    padx=5
)


# ==========================================
# SEARCH
# ==========================================

search_frame = ttk.Frame(
    root,
    padding=(15, 5)
)

search_frame.pack(
    fill="x"
)

ttk.Label(
    search_frame,
    text="Search Tickets:"
).pack(
    side="left",
    padx=5
)

search_entry = ttk.Entry(
    search_frame,
    textvariable=search_var,
    width=40
)

search_entry.pack(
    side="left",
    padx=5
)

search_var.trace_add(
    "write",
    search_tickets
)


# ==========================================
# TICKET TABLE
# ==========================================

table_frame = ttk.LabelFrame(
    root,
    text="Support Tickets",
    padding=10
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

columns = (
    "ID",
    "Date",
    "Name",
    "Category",
    "Priority",
    "Status"
)

ticket_tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    ticket_tree.heading(
        column,
        text=column
    )

ticket_tree.column(
    "ID",
    width=60
)

ticket_tree.column(
    "Date",
    width=150
)

ticket_tree.column(
    "Name",
    width=150
)

ticket_tree.column(
    "Category",
    width=130
)

ticket_tree.column(
    "Priority",
    width=100
)

ticket_tree.column(
    "Status",
    width=100
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=ticket_tree.yview
)

ticket_tree.configure(
    yscrollcommand=scrollbar.set
)

ticket_tree.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# ==========================================
# VIEW BUTTON
# ==========================================

ttk.Button(
    root,
    text="View Selected Ticket",
    command=view_ticket
).pack(
    pady=(0, 15)
)


# ==========================================
# LOAD EXISTING TICKETS
# ==========================================

load_tickets()


# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()

```
