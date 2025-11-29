# 🧠 **Tkinter Calculator **

---

## ✅ **1. Importing Tkinter**

```python
import tkinter as tk
from tkinter import ttk
```

* `tkinter` provides the GUI tools.
* `ttk` provides nicer, modern-looking widgets.

---

## ✅ **2. Creating the Calculator Class**

```python
class Calculator(tk.Tk):
```

* This makes a **window** that *is itself* a Tkinter app.
* We extend `tk.Tk` to build everything into one object.

---

## ✅ **3. Window Setup**

```python
self.title("Tkinter Calculator")
self.geometry("300x400")
self.resizable(False, False)
```

* Sets the window title, size, and prevents resizing.

---

## ✅ **4. Expression Variable**

```python
self.expression = ""
```

* This stores what the user types (like “45+3*2”).

---

## ✅ **5. Calculator Display**

```python
self.display = tk.Entry(...)
```

* The display is just a big text entry box.
* `justify="right"` makes numbers align like a real calculator.
* The display holds the **current expression** or the **result**.

---

## ✅ **6. Buttons Layout System**

A list defines **text**, **row**, and **column**:

```python
buttons = [
    ("7", 0, 0), ("8", 0, 1), ...
```

Each button uses:

```python
ttk.Button(..., command=lambda t=text: self.on_button_click(t))
```

💡 The lambda is important — it sends the button’s text to `on_button_click`.

Buttons are placed using `.grid()` and the frame rows/columns expand using:

```python
buttons_frame.rowconfigure(...)
buttons_frame.columnconfigure(...)
```

---

## ✅ **7. Button Behavior — The Calculator Brain**

Everything happens inside:

```python
def on_button_click(self, char):
```

### ▶️ **A. Clear Button ("C")**

```python
if char == "C":
    self.expression = ""
    self.display.delete(0, tk.END)
```

* Wipes both the visible display and the internal expression.

---

### ▶️ **B. Equals ("=") Button**

```python
elif char == "=":
    try:
        result = str(eval(self.expression))
```

* Evaluates the expression using `eval()`.
* Writes the result in the display.
* Stores the result so the user can continue calculating.

If the expression is invalid:

```python
self.display.insert(tk.END, "Error")
```

---

### ▶️ **C. Any Other Button (numbers/operators)**

```python
else:
    self.expression += str(char)
    self.display.delete(0, tk.END)
    self.display.insert(tk.END, self.expression)
```

* Adds the button text to the expression.
* Updates the display.

---

## ✅ **8. Starting the App**

```python
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
```

* Creates the `Calculator` object.
* Starts the main Tkinter event loop (keeps the window open).

---

