# 🍎 Teacher Help Sheet: Micro:bit Temperature Warning System

## Lesson Overview

- **Age group:** 9-year-olds
- **Duration:** 1hr 30 mins
- **Objective:** Students will learn how to use temperature sensors, variables, conditionals (`if/elif/else`), gesture input, and display output using MicroPython and the Micro:bit. The goal is to build a temperature warning system that shows different icons based on temperature and gestures.

---

## 🛠️ Setup Checklist

✅ Chrome browser is up to date  
✅ Micro:bit connected via USB and permission granted  
✅ Open Micro:bit online Python editor: [https://python.microbit.org/v/3](https://python.microbit.org/v/3)  

---

## 🛠️ Setup & Tools

### ✅ Recommended Editor

Use **Google Chrome** and go to:

🔗 [https://python.microbit.org/v/3](https://python.microbit.org/v/3)

- Click **Connect** and choose the Micro:bit
- Write your code → Click **Flash**
- No installation required

### ✅ Alternative Editor (Installed)

- Use **Mu Editor** if installed
- Plug in the Micro:bit and it should auto-detect
- Click **Flash** to upload code
- Use the REPL for live testing

---

## 🧾 Micro:bit MicroPython Cheat Sheet

📚 MicroPython Docs: [API Reference](https://microbit-micropython.readthedocs.io/en/v2-docs/)

### ✅ Import Library

```python
from microbit import *
```

### ✅ Display Commands

```python
display.scroll("Hello!")
display.show(Image.HAPPY)
display.clear()
```

### ✅ Variables & Loops

```python
temperature()             # Gets temperature in Celsius
while True:               # Infinite loop
sleep(500)                # Wait 0.5 seconds
```

### ✅ Buttons & Gestures

```python
button_a.was_pressed()                     # Detect Button A press
accelerometer.was_gesture('shake')        # Detect shake gesture
```

---

## 🛠️ Troubleshooting

| Problem                    | Fix                                        |
|----------------------------|---------------------------------------------|
| Flash button greyed out    | Close REPL or restart browser              |
| Temperature not updating   | Add `sleep(500)` in loop                   |
| Shake not detected         | Shake gently and check code syntax         |
| Button A does nothing      | Check indentation and `button_a` code line |

---

## 🚧 Common Pitfalls and Solutions

| Pitfall                     | Solution                                                        |
|-----------------------------|------------------------------------------------------------------|
| Conditionals not working    | Ensure proper indentation and check use of `if`, `elif`, `else` |
| Gesture not detected        | Try gentle shakes; use `was_gesture` not `is_gesture`           |
| Variable not updating       | Confirm correct use of `temp = temperature()` inside loop       |
| Display stuck               | Add `sleep()` to slow loop and `display.clear()` after showing  |

---

## 📚 Key Vocabulary

- **Temperature Sensor**: Built-in tool that reads room temperature.
- **Variable**: A box that stores values (e.g., `temp = 24`)
- **Conditionals**: Let the program make decisions using `if`, `elif`, `else`
- **Gesture**: Movement that triggers code (e.g., shake)
- **Loop**: Keeps checking and running your code forever

---

## 🎯 Step-by-Step Guide (Teacher Tips)

### Step 1: Connection

- Demonstrate connecting and flashing code using the online editor.

### Step 2: Show Image

- Let students flash a smiley face. This confirms setup success.

### Step 3: Button A for Temperature

- Walk through reading temperature and using `display.scroll()`.

### Step 4: `if` Logic

- Explain how `if temp >= 25:` checks for hot conditions.
- Show how `else:` gives a fallback action (e.g., happy face).

### Step 5: Add Shake Gesture

- Show how shaking triggers a warning face.
- Explain combining gestures with temperature (`and temp >= 25`).

### Step 6: Full System

- Go slowly through each condition (`if`, `elif`, `else`) in order.
- Tip: Flash and test after adding each new section.

### Step 7: Investigate & Modify

- Encourage students to experiment with threshold values or icons.

### Step 8: Challenge (Optional)

- Let advanced learners add cold warning with `elif temp < 10`.

### Step 9: Reflection

- Ask what students learned about logic, variables, and real-world data.

---

## 📌 Teaching Tips

- Reinforce `if`/`elif`/`else` by relating it to real-life choices.
- Celebrate small wins—every successful flash is progress!
- Let students test each other’s Micro:bits to see differences.
- Use “What do you think will happen?” to promote prediction.

---

## ✅ Final Completed Program (for teacher reference)

```python
from microbit import *

while True:
    temp = temperature()

    if button_a.was_pressed():
        display.scroll(str(temp) + "C")

    if accelerometer.was_gesture('shake') and temp >= 25:
        for i in range(3):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep(200)

    elif temp >= 25:
        display.show(Image.ANGRY)

    elif temp < 10:
        display.show(Image.TARGET)

    else:
        display.show(Image.HAPPY)

    sleep(500)
```

---

🎉 **Enjoy the session! Support curiosity and creativity! 🌈**
