
# Micro:bit Knight Rider Workshop for 13-Year-Olds
## Context – What Is Knight Rider?

    “Knight Rider” was a cool 1980s sci-fi TV show. It featured a futuristic talking car called KITT with a signature red light that moved smoothly from side to side on its front. The animation made it feel alive and smart — just like the car could ‘see’ with that red eye.

    Today, we’ll recreate that animation to learn about algorithms, iteration, and selection in MicroPython!

---

![Kit the Knightrider car](https://i.ytimg.com/vi/5BsFnk83NMI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHekuY69frlizAa7U_gqpadllZ1A
)

## 🕐 Workshop Schedule (1.5 hours)

| Time       | Activity                                                                 |
|------------|--------------------------------------------------------------------------|
| 0–10 mins  | Welcome & context: What is Knight Rider? Why make lights move?          |
| 10–20 mins | Intro to Micro:bit: buttons, LED grid, code editor                      |
| 20–30 mins | Brainstorm logic: How can we make a light move? (Use pseudocode)        |
| 30–45 mins | Coding: One-way movement (left to right)                                |
| 45–60 mins | Looping & bouncing back (right to left, then repeat)                    |
| 60–75 mins | Add color (with external neopixel if available) or speed effect         |
| 75–90 mins | Reflection & Extension Challenges                                       |

## Microbit Documentation

[Code Docs here](https://microbit-micropython.readthedocs.io/en/v2-docs/index.html).      


## 🔄 Code Concepts We Will Use         

✅ **Variables**  
store our position and logic.

✅ **Iteration**  
repeats a sequence forever.

✅ **Selection**  
program deciscions.

✅ **Algorithm**  
The step-by-step processes.


## 🧱 Stage 1: Light a Single Pixel

### 🎯 Goal: Learn how to turn on one light at a specific position

#### 🧠 Pseudocode:

```
Turn on a single LED at a specific (x, y) coordinate with full brightness.
```

```python
from microbit import *

# Turn on the LED at position (2, 2) with full brightness (9)
display.set_pixel(2, 2, 9)
```

### 🧠 Explanation:
- `display.set_pixel(x, y, brightness)` lights up one pixel.
- `x` is the column (0 = left, 4 = right)
- `y` is the row (0 = top, 4 = bottom)
- `brightness` ranges from 0 (off) to 9 (full brightness)

---

## 🔁 Stage 2: Move a Single Pixel Left to Right

### 🎯 Goal: Use a loop to move a pixel

#### 🧠 Pseudocode:
```
Repeat forever:
    Move a single pixel across row 2 from left to right
    Wait a moment
    Turn off the pixel before moving to the next
```

```python
from microbit import *

while True:
    for x in range(0, 5):  # x = 0, 1, 2, 3, 4
        display.set_pixel(x, 2, 9)
        sleep(100)
        display.set_pixel(x, 2, 0)
```

### 🧠 Explanation:
- `while True:` runs forever
- `range(0, 5)` moves across the grid
- We light one pixel in row 2 and turn it off before lighting the next

---

## 🧱 Stage 3: Light a Full Column

### 🎯 Goal: Light a whole column using a loop

#### 🧠 Pseudocode:
```
For each row from 0 to 4:
    Turn on the LED at column 2
```

```python
from microbit import *

for y in range(0, 5):       # y = 0 to 4
    display.set_pixel(2, y, 9)  # Column stays the same (x=2)
```

---

## 🔁 Stage 4: Sweep a Column Left to Right and Back

### 🎯 Goal: Use nested loops to animate a sweeping column

#### 🧠 Pseudocode:
```
Repeat forever:
    For each column from 0 to 4:
        Light up all LEDs in that column
        Wait
        Turn off that column
    Then for each column from 4 to 0:
        Do the same in reverse
```

```python
from microbit import *

while True:
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, 9)
        sleep(100)
        for y in range(0, 5):
            display.set_pixel(x, y, 0)

    for x in range(4, -1, -1):
        for y in range(0, 5):
            display.set_pixel(x, y, 9)
        sleep(100)
        for y in range(0, 5):
            display.set_pixel(x, y, 0)
```

---

## 🌟 Stage 5: Add Fading Trail (Final Knight Rider Effect)

### 🎯 Goal: Add memory and fading effect to previous columns

#### 🧠 Pseudocode:
```
Repeat forever:
    For each column from 0 to 4:
        Light up the current column brightly
        Light up the previous 1–2 columns with dimmer brightness
        Wait
        Turn off all 3 columns
    Then repeat in reverse from column 4 to 0
```

```python
from microbit import *

while True:
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, 9)
            if x > 0:
                display.set_pixel(x - 1, y, 7)
            if x > 1:
                display.set_pixel(x - 2, y, 2)
        sleep(100)
        for y in range(0, 5):
            display.set_pixel(x, y, 0)
            if x > 0:
                display.set_pixel(x - 1, y, 0)
            if x > 1:
                display.set_pixel(x - 2, y, 0)

    for x in range(4, -1, -1):
        for y in range(0, 5):
            display.set_pixel(x, y, 9)
            if x < 4:
                display.set_pixel(x + 1, y, 7)
            if x < 3:
                display.set_pixel(x + 2, y, 2)
        sleep(100)
        for y in range(0, 5):
            display.set_pixel(x, y, 0)
            if x < 4:
                display.set_pixel(x + 1, y, 0)
            if x < 3:
                display.set_pixel(x + 2, y, 0)
```

---

## 🏁 Summary

| Concept       | What You Learned                             |
|---------------|-----------------------------------------------|
| Coordinates   | How pixels are placed in a grid using `(x, y)` |
| Loops         | Use `for` and `while` to repeat actions       |
| Brightness    | Set LEDs to dim or bright for visual effects |
| Algorithms    | Step-by-step instructions to animate lights  |
| Conditions    | Use `if` to avoid out-of-bounds errors       |


## 🔄 Code Concepts

✅ **Variables**  
`x`, `row`, and `direction` store our position and logic direction.

✅ **Iteration**  
`while True:` repeats the light animation forever.

✅ **Selection**  
`if` and `elif` decide when to change direction.

✅ **Algorithm**  
The step-by-step process of moving, lighting, waiting, and turning off.

