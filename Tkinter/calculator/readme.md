# Calculator
---

# 🧱 **Step-by-Step Breakdown With Full Code Blocks**

---

# ✅ **Step 1 — Imports**

### **Code Block**

```python
import tkinter as tk
from tkinter import ttk
```

### **Explanation**

* `import tkinter as tk` loads Tkinter and shortens the name to `tk`.
* `from tkinter import ttk` imports themed widgets such as `ttk.Button`.
* These two lines load everything needed for the GUI.

---

# ✅ **Step 2 — Calculator Class Definition**

### **Code Block**

```python
class Calculator(tk.Tk):
```

### **Explanation**

* Creates a new class named `Calculator`.
* It **inherits** from `tk.Tk`, meaning the class *is* a Tkinter window.

---

# ✅ **Step 3 — Constructor (**init**)**



```python
def __init__(self):
    super().__init__()
    self.title("Tkinter Calculator")
    self.geometry("300x400")
    self.resizable(False, False)

    self.expression = ""
    self.create_widgets()
```

### **Explanation**

* `super().__init__()` initializes the Tkinter window.
* `title()`, `geometry()`, and `resizable()` configure how the window looks.
* `self.expression = ""` stores all typed numbers/operators.
* `self.create_widgets()` builds the display and buttons.

---

# ✅ **Step 4 — Display Widget**



```python
self.display = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
self.display.pack(fill="both", ipadx=8, ipady=8, pady=10)
```

### **Explanation**

* Creates a large text entry box for showing input and results.
* `justify="right"` makes it behave like a real calculator display.
* `.pack()` places it at the top and stretches it across the window.

---

# ✅ **Step 5 — Buttons Frame**



```python
buttons_frame = tk.Frame(self)
buttons_frame.pack(expand=True, fill="both")
```

### **Explanation**

* Creates a container (`Frame`) to hold all calculator buttons.
* `.pack(expand=True)` allows the frame to grow.

---

# ✅ **Step 6 — Button Definitions List**



```python
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
    ("C", 4, 0)
]
```

### **Explanation**

* Each tuple defines:
  **(text_on_button, row_number, column_number)**
* This is how you build the grid layout.

---

# ✅ **Step 7 — Creating Each Button**



```python
for (text, row, col) in buttons:
    button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
```

### **Explanation**

* Loops through each button definition.
* Creates a button with the correct label (`text`).
* `command=lambda t=text:` ensures the button sends **its own text** to the handler.
* `.grid()` places buttons into rows & columns.
* `sticky="nsew"` makes each button stretch to fill its grid cell.

---

# ✅ **Step 8 — Making Rows & Columns Expandable**



```python
for i in range(5):
    buttons_frame.rowconfigure(i, weight=1)
for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)
```

### **Explanation**

* Makes the 5 rows and 4 columns scale evenly.
* Without these, buttons would not resize properly.

---

# ✅ **Step 9 — Button Click Handler**



```python
def on_button_click(self, char):
    if char == "C":
        self.expression = ""
        self.display.delete(0, tk.END)
    elif char == "=":
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""
    else:
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
```

### **Explanation**

#### 🔹 **If user presses “C”**

* Clears the expression and display.

#### 🔹 **If user presses “=”**

* Uses `eval()` to compute the math.
* Shows the result.
* Stores the result to continue calculating.
* If invalid → shows `"Error"`.

#### 🔹 **Otherwise (numbers or + - * / . )**

* Adds the pressed character to `self.expression`.
* Updates the display.

---

# ✅ **Step 10 — Program Entry Point**



```python
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
```
#full Code
```python
import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
        self.display.pack(fill="both", ipadx=8, ipady=8, pady=10)

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

```
