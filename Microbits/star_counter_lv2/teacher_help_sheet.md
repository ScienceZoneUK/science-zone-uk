# 🍎 Teacher Help Sheet: Micro\:bit Star Counter Adventure

## Lesson Overview

- **Age group:** 9-year-olds
- **Duration:** 1hr 30 mins
- **Objective:** Students learn basic computational thinking, MicroPython programming, variables, inputs (buttons), sensors (accelerometer), and outputs (display).

---

## 🛠️ Setup Checklist

✅ Ensure Chrome browser is updated.\
✅ Micro\:bit connected via USB and permission granted via Chrome.\
✅ Open Micro\:bit online Python editor: [python.microbit.org/v/3](https://python.microbit.org/v/3)

---

## 🛠️ Setup & Tools

### ✅ Recommended Editor

Use **Google Chrome** and go to:

🔗 [https://python.microbit.org/v/3](https://python.microbit.org/v/3)

- Click **Connect** and choose the Micro\:bit
- Write your code → Click **Flash** to upload
- Works without installing anything

### ✅ Alternative Editor (Installed)

- **Mu Editor** is pre-installed on PCs
- Plug in the Micro\:bit (should auto-detect)
- Click **Flash** to upload
- REPL can be used for live testing

---

## 🧾 Micro\:bit MicroPython Cheat Sheet

Microbit API docs here [CLICK](https://microbit-micropython.readthedocs.io/en/v2-docs/)

### ✅ ALWAYS use the microbit library

```python
from microbit import *          # Setup the microbit api
```

### ✅ Display

```python
display.scroll("Hello!")            # Scroll text
display.set_pixel(x, y, brightness) # Light pixel at (x, y)
display.clear()                     # Clear screen
```

### ✅ Loops & Timing

```python
for i in range(5):    # Loop from 0 to 4
while True:           # Infinite loop
sleep(100)            # Wait 100ms
```

### ✅ Buttons

```python
button_a.is_pressed()   # True if pressed now
button_b.was_pressed()  # True if pressed since last check
```

### ✅ Gesture sensor

The recognised gestures names are: up, down, left, right, face up, face down, freefall, 3g, 6g, 8g, shake.

```python

# return True or False to indicate if the named gesture is currently active.
accelerometer.is_gesture(name) #See above recognised gesture name

```

### ✅ Pins

```python
pin0.write_digital(1)    # Output ON
```

---

## 🛠️ Troubleshooting

| Problem                    | Fix                                       |
| -------------------------- | ----------------------------------------- |
| Flash button disabled      | Close REPL tab or Mu REPL terminal        |
| Flashing fails (online)    | Unplug/replug Micro\:bit, use Chrome only |
| Mu won’t detect Micro\:bit | Restart Mu or check USB port              |
| Code runs too fast         | Add `sleep(100)` to slow it down          |

---

## 🚧 Common Pitfalls and Solutions

| Pitfall                    | Solution                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| Micro\:bit not detected    | Refresh Chrome, reconnect Micro\:bit, grant browser permission     |
| Code syntax errors         | Carefully check indentation and colon (`:`) usage                  |
| Counts not incrementing    | Ensure students have used `stars = stars + 1` correctly            |
| Shake gesture not detected | Gently shake; check code line `accelerometer.was_gesture('shake')` |

---

## 📚 Key Vocabulary

- **Variable**: A storage container for numbers (e.g., `stars = 0`)
- **Increment**: Increasing a number (e.g., `stars = stars + 1`)
- **Gesture**: Movement detected by sensors (e.g., shaking)
- **Display**: Shows images or numbers on Micro\:bit LEDs

---

## 🎯 Step-by-Step Guide (Teacher Tips)

### Step 1: Connection

- Clearly demo connecting and flashing code.

### Step 2: Display Images

- Check each child successfully displays an image first.

### Step 3: Button Inputs

- Ensure students understand button inputs (`button_a.was_pressed()`).
- Tip: Explain difference between `was_pressed()` (one-off) and `is_pressed()` (continuous).

### Step 4: Counting with Variables

- Reinforce the concept of counting: variables keep track of numbers.
- Ensure each student tests incrementing the count.

### Step 5: Shake Gesture

- Clearly demonstrate how gentle shakes trigger gestures.
- Tip: Let students experiment with shaking intensity.

### Step 6: Animation and Text

- Discuss creativity: encourage altering the images and text.

### Step 7: Building the Final Program

- Go slow: build step-by-step clearly from the provided snippets.
- Frequently pause to flash and test incrementally.

### Step 8: Investigate & Modify

- Encourage student prediction before running the code.
- Prompt reflection: "What did you think would happen? Did it?"

### Step 9: Challenge (Optional Reset)

- Provide the advanced reset feature for stronger students to maintain engagement.

### Step 10: Reflection

- Have students share their learning clearly.
- Reinforce computational thinking skills and vocabulary.

---

## 📌 Teaching Tips

- Praise incremental successes.
- Promote peer-to-peer help.
- Ensure each child experiences coding confidence by frequent checks.
- Encourage creative modifications for deeper learning.

---

## ✅ Final Completed Program (for teacher reference)

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()

    if button_b.was_pressed():
        shooting_stars = shooting_stars + 1
        display.show(Image.ARROW_N)
        sleep(300)
        display.clear()

    if accelerometer.was_gesture('shake'):
        for i in range(2):
            display.show(Image.GHOST)
            sleep(300)
            display.clear()
            sleep(200)

        display.scroll("Stars:")
        display.scroll(str(stars))

        display.scroll("Shooting Stars:")
        display.scroll(str(shooting_stars))
```

---

🎉 **Enjoy your lesson! You’ve got this! 🌟**

