# 🧑‍🏫 Teacher Help Sheet – Micro:bit Snake Game Workshop

## 📝 Overview

- **Age Group:** 13-year-old students
- **Duration:** 1.5 hours
- **Goal:** Guide students to build a fully functioning Snake game using MicroPython on a Micro:bit.

### 👩‍💻 Learning Objectives

Students will:
- Use **variables** and **lists** to manage game data.
- Use **loops**, **conditions**, and **functions** to control flow.
- Understand the use of **modulo** to wrap screen positions.
- Interact with the **LED matrix**, **buttons**, and **accelerometer**.

---

## ✅ Setup Checklist

### Hardware
- One Micro:bit per student
- USB cable
- Computer with internet access

### Software
- Online Editor: [https://python.microbit.org/v/3](https://python.microbit.org/v/3)
- Optional: Serial console viewer for print statements

### Before the Lesson
- Test the editor and ensure Micro:bits connect properly.
- Prepare workshop files or code snippets for easy pasting.
- Familiarise yourself with each step of the program.

---

## 📘 MicroPython Quick Cheat Sheet

| Action                    | Code Example                              |
|---------------------------|-------------------------------------------|
| Show LED                  | `display.set_pixel(x, y, 9)`              |
| Clear display             | `display.clear()`                         |
| Pause                     | `sleep(500)`                              |
| Loop forever              | `while True:`                             |
| Button press              | `button_a.was_pressed()`                  |
| Get gesture               | `accelerometer.current_gesture()`         |
| Random number             | `random.randint(0, 4)`                    |
| Modulo (wrap)             | `x = x % 5`                                |
| Add to list front         | `snake.insert(0, head)`                   |
| Remove from end of list   | `snake.pop()`                             |

---

## 🛠️ Troubleshooting Tips

| Issue                              | Solution                                               |
|-----------------------------------|--------------------------------------------------------|
| Micro:bit not connecting           | Refresh page, try another USB port or cable           |
| Nothing showing on Micro:bit      | Check `draw_snake()` function and pixel coordinates   |
| Error: list index out of range    | Usually means head moved off the grid — use wrap!     |
| Buttons/tilt not responding       | Make sure gesture/button code is inside the loop      |
| Snake disappears                  | Check if `display.clear()` is called before drawing   |

---

## ⚠️ Common Pitfalls

- Forgetting `wrap(position)` for head movement
- Not clearing screen before re-drawing snake
- Misunderstanding coordinates: `x, y` = `left-right, top-bottom`
- Using `=` instead of `==` in `if` statements

---

## 🗝️ Key Vocabulary

- **Loop:** Code that runs again and again
- **List:** A collection of items (like the snake’s body segments)
- **Function:** A block of code you can reuse (e.g., `draw_snake()`)
- **Modulo (`%`):** Remainder operator, helps wrap values on the grid
- **Pixel:** One tiny light on the Micro:bit screen

---

## 📚 Step-by-Step Guidance

### STEP 1 – Create Snake
- Use: `snake = [[2, 2]]`
- Tip: Explain coordinates and grid structure.

### STEP 2 – Show Snake
- Introduce `display.set_pixel(x, y, 9)`
- Tip: Check if all students’ snakes appear.

### STEP 3 – Move the Snake
- Add movement logic with a `direction` list.
- Tip: Use diagrams to show head movement.

### STEP 4 – Add Wrapping with Modulo
- Introduce `%` operator to loop around screen.
- Tip: Test with `print()` to understand head position.

### STEP 5 – Add Button and Tilt Controls
- Use `button_a`, `button_b`, and `accelerometer`
- Tip: Make it a challenge to “steer” the snake!

### STEP 6 – Add an Apple
- Use `random.randint(0, 4)` and condition to check for eating
- Tip: Draw apple with different brightness (e.g. 5)

---

## 💬 Teaching Tips

- Keep energy fun and supportive — it’s a game!
- Live code alongside students where possible.
- Reinforce debugging as a natural part of coding.
- Use visual aids: whiteboards or printed grids.
- Ask students to explain their code to each other.

---

## ✅ Final Reference Code

```python
import random
from microbit import *

snake = [[2, 2]]
apple = [random.randint(0, 4), random.randint(0, 4)]
direction = [0, -1]

def draw_snake_and_apple():
    display.clear()
    display.set_pixel(apple[0], apple[1], 5)
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)

def wrap(position):
    return [position[0] % 5, position[1] % 5]

while True:
    gesture = accelerometer.current_gesture()
    if button_a.was_pressed(): direction = [-1, 0]
    if button_b.was_pressed(): direction = [1, 0]
    if gesture == "up": direction = [0, -1]
    if gesture == "down": direction = [0, 1]

    head = wrap([snake[0][0] + direction[0], snake[0][1] + direction[1]])
    snake.insert(0, head)

    if head == apple:
        apple = [random.randint(0, 4), random.randint(0, 4)]
    else:
        snake.pop()

    draw_snake_and_apple()
    sleep(400)
```

---

🎉 **Enjoy the lesson! Help your students feel like coding heroes.**
