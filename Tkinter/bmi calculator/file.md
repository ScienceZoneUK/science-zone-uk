
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

## ✅ Features ( **BMI = weight (kg) / (height in meters)²** )

✔ Input height (cm)
✔ Input weight (kg)
✔ Calculate BMI
✔ Show health category

---

## Step 1 Perform necessary imports
```python
import tkinter as tk
from tkinter import messagebox
```
## Step 2 The BMI Calculator
**BMI = weight (kg) / (height in meters)²**
```python
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
```
## Step 3 Setting up the Window
```python
# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
```
## Step 4
```python
# Height
tk.Label(root, text="Height (cm)").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()
```
## Step 5
```python
# Weight
tk.Label(root, text="Weight (kg)").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()
```
## Step 6
```python
# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)
```
## Step 7
```python
# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
```

---



## 🔼 Step 8 Do this Upgrades

* Clear button
* Color result (green = normal, red = obese)
* Use `grid()` instead of `pack()` (refer to the first note for this task)
* Add age & gender (optional)

---


> **BMI Calculator (Python, Tkinter)** – Built a GUI application to calculate BMI and health status using user input with validation.

---


