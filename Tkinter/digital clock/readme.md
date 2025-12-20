**Tkinter Digital Clock** project (beginner-friendly) that updates every second.

## Level1 
## ✅ Digital Clock (Tkinter)

```python
import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)

# Clock label
clock_label = tk.Label(
    root,
    font=("Arial", 48, "bold"),
    bg="black",
    fg="lime",
    padx=20,
    pady=20
)
clock_label.pack(fill="both", expand=True)

def update_time():
    current_time = strftime("%H:%M:%S")   # 24-hour format
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # update every 1 second

update_time()
root.mainloop()
```

### How it works

* `strftime("%H:%M:%S")` gets the current time.
* `after(1000, update_time)` schedules the function to run again after 1 second (1000 ms).

---

## Upgrades you can add (pick one)

### 1) Show date too

Replace the `current_time` line with:

```python
current_time = strftime("%A, %d %B %Y\n%H:%M:%S")
```

### 2) 12-hour format with AM/PM

```python
current_time = strftime("%I:%M:%S %p")
```

## Level 2
---

## Step 1: Make a basic window

```python
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock+")
root.geometry("520x260")
root.mainloop()
```

What you learned:

* `Tk()` creates the app window
* `mainloop()` keeps it running

---

## Step 2: Put a label in the window

Labels display text (we’ll use one for the time).

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Digital Clock+")
root.geometry("520x260")

time_label = ttk.Label(root, text="12:34:56", font=("Consolas", 64, "bold"))
time_label.pack(expand=True)

root.mainloop()
```

What you learned:

* `Label` shows text
* `pack(expand=True)` centers it and lets it grow

---

## Step 3: Update the label every second

This is the main “clock” logic: get current time → update label → repeat.

```python
import tkinter as tk
from tkinter import ttk
from time import strftime

root = tk.Tk()
root.title("Digital Clock+")
root.geometry("520x260")

time_label = ttk.Label(root, text="", font=("Consolas", 64, "bold"))
time_label.pack(expand=True)

def tick():
    time_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, tick)  # call tick again after 1 second

tick()
root.mainloop()
```

What you learned:

* `strftime()` gets formatted time
* `after(ms, func)` schedules repeated updates (no infinite loops needed)

---

## Step 4: Add a date label under the time

```python
import tkinter as tk
from tkinter import ttk
from time import strftime

root = tk.Tk()
root.title("Digital Clock+")
root.geometry("520x260")

time_label = ttk.Label(root, text="", font=("Consolas", 64, "bold"))
time_label.pack(fill="both", expand=True)

date_label = ttk.Label(root, text="", font=("Segoe UI", 16))
date_label.pack()

def tick():
    time_label.config(text=strftime("%H:%M:%S"))
    date_label.config(text=strftime("%A, %d %B %Y"))
    root.after(1000, tick)

tick()
root.mainloop()
```

Now you have:

* time + date

---

## Step 5: Add “options” using checkboxes (state variables)

To toggle settings, Tkinter uses `BooleanVar`.

```python
use_24h = tk.BooleanVar(value=True)
show_seconds = tk.BooleanVar(value=True)
```

Then attach them to checkbuttons.

```python
ttk.Checkbutton(root, text="24-hour format", variable=use_24h).pack()
ttk.Checkbutton(root, text="Show seconds", variable=show_seconds).pack()
```

---

## Step 6: Make time formatting depend on options

We build a time format string:

* 24-hour: `%H:%M`
* 12-hour: `%I:%M %p`
* seconds optional: add `:%S`

Example function:

```python
def make_time_string():
    if use_24h.get():
        fmt = "%H:%M"
    else:
        fmt = "%I:%M"

    if show_seconds.get():
        fmt += ":%S"

    if not use_24h.get():
        fmt += " %p"

    return strftime(fmt).lstrip("0")
```

Then inside `tick()`:

```python
time_label.config(text=make_time_string())
```

---

## Step 7: Add theme switch (dark/light)

We’ll change background + text colors when the user toggles “Dark mode”.

You store the setting:

```python
dark_mode = tk.BooleanVar(value=True)
```

Then a function that applies styles:

```python
def apply_theme():
    if dark_mode.get():
        bg = "black"
        fg = "lime"
    else:
        bg = "white"
        fg = "black"

    root.configure(bg=bg)
    time_label.configure(background=bg, foreground=fg)
    date_label.configure(background=bg, foreground=fg)
```

Attach it to a checkbox:

```python
ttk.Checkbutton(root, text="Dark mode", variable=dark_mode, command=apply_theme).pack()
```

---

## Step 8: Put it all together (complete stepped-up version)

This is a clean “complex but understandable” final version:

```python
import tkinter as tk
from tkinter import ttk
from time import strftime

root = tk.Tk()
root.title("Digital Clock+")
root.geometry("520x300")
root.resizable(False, False)

# Settings (state)
use_24h = tk.BooleanVar(value=True)
show_seconds = tk.BooleanVar(value=True)
dark_mode = tk.BooleanVar(value=True)

# Labels
time_label = tk.Label(root, font=("Consolas", 64, "bold"))
time_label.pack(fill="both", expand=True)

date_label = tk.Label(root, font=("Segoe UI", 16))
date_label.pack(pady=(0, 10))

# Options frame
options = ttk.LabelFrame(root, text="Options", padding=10)
options.pack(fill="x", padx=12, pady=10)

ttk.Checkbutton(options, text="24-hour format", variable=use_24h).grid(row=0, column=0, sticky="w", padx=8)
ttk.Checkbutton(options, text="Show seconds", variable=show_seconds).grid(row=0, column=1, sticky="w", padx=8)
ttk.Checkbutton(options, text="Dark mode", variable=dark_mode).grid(row=1, column=0, sticky="w", padx=8)

options.columnconfigure(0, weight=1)
options.columnconfigure(1, weight=1)

def apply_theme():
    if dark_mode.get():
        bg = "#000000"
        fg_time = "#00ff66"
        fg_date = "#cfcfcf"
    else:
        bg = "#f5f5f5"
        fg_time = "#111111"
        fg_date = "#333333"

    root.configure(bg=bg)
    time_label.configure(bg=bg, fg=fg_time)
    date_label.configure(bg=bg, fg=fg_date)

def make_time_string():
    if use_24h.get():
        fmt = "%H:%M"
    else:
        fmt = "%I:%M"

    if show_seconds.get():
        fmt += ":%S"

    if not use_24h.get():
        fmt += " %p"

    return strftime(fmt).lstrip("0")

def tick():
    time_label.config(text=make_time_string())
    date_label.config(text=strftime("%A, %d %B %Y"))
    root.after(250, tick)

# Make dark mode checkbox apply immediately
def on_theme_toggle():
    apply_theme()

# Reconnect checkbox command after creation
for child in options.winfo_children():
    if isinstance(child, ttk.Checkbutton) and child.cget("text") == "Dark mode":
        child.config(command=on_theme_toggle)

apply_theme()
tick()
root.mainloop()
```

---

