Nice choice 👍 **BMI Calculator** is a perfect beginner Tkinter project.

I’ll give you:
1️⃣ Simple explanation
2️⃣ Clean beginner-friendly code
3️⃣ How to upgrade it later

---

## 🧮 BMI Calculator (Beginner Friendly)

### 📘 What is BMI?

**BMI = weight (kg) / (height in meters)²**

---

## 🧠 What You’ll Learn

* `Label`, `Entry`, `Button`
* Functions
* Basic math
* Error handling (simple)

---

## ✅ Features

✔ Input height (cm)
✔ Input weight (kg)
✔ Calculate BMI
✔ Show health category

---

## 🧑‍💻 Complete Tkinter Code

```python
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal weight"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nStatus: {status}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")

# Height
tk.Label(root, text="Height (cm)").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Weight
tk.Label(root, text="Weight (kg)").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
```

---

## ▶️ How to Run

1. Save as `bmi_calculator.py`
2. Run:

```bash
python bmi_calculator.py
```

---

## 🔼 Beginner Upgrades (Try These Next)

* Clear button
* Color result (green = normal, red = obese)
* Use `grid()` instead of `pack()`
* Add age & gender (optional)

---

## 💼 Resume Line

> **BMI Calculator (Python, Tkinter)** – Built a GUI application to calculate BMI and health status using user input with validation.

---

If you want, I can:

* Explain **each line**
* Add **better UI**
* Convert it to **calculator-style layout**
* Make it **mobile-sized UI**

Just tell me 😄
