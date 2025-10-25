# 💧 **Micro:bit Game: Catch the Drop**

---

## 🎯 **Learning Objectives (Bloom’s Taxonomy)**

| Bloom’s Level        | Learning Objective                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 🔵 **Remembering**   | Pupils will be able to **identify** what the accelerometer does on the Micro:bit.                                 |
| 🟢 **Understanding** | Pupils will be able to **explain** how tilt affects player movement.                                              |
| 🟡 **Applying**      | Pupils will be able to **use** tilt input to move a player sprite left and right.                                 |
| 🟠 **Analysing**     | Pupils will be able to **compare** how different speeds affect gameplay.                                          |
| 🔴 **Evaluating**    | Pupils will be able to **judge** how fair or difficult their game is.                                             |
| 🟣 **Creating**      | Pupils will be able to **design** their own version of the game (e.g., faster drops, multiple levels, or sounds). |

---

## 🕹️ **Game Description**

A single raindrop falls from the top of the Micro:bit screen.
The player moves a “bucket” at the bottom by tilting the Micro:bit left or right.
Catch the raindrop to score a point — if you miss, you lose one!

---

## ⏱️ **Lesson Flow (Teacher Guide)**

---

### 1️⃣ **Introduction (10 mins)**

💬 Ask students:

* What happens when it rains?
* How would you “catch” a drop using the Micro:bit?
* How can we tell when something has been caught?

📌 Explain:
The **Micro:bit’s accelerometer** can sense tilt — left, right, or flat — so we can use it to move our bucket.
We’ll use the LEDs as our screen.

---

### 2️⃣ **The Problem: Catch the Drop! (5 mins)**

Challenge:

> Build a game where a **raindrop falls from the top**, and the **player tilts** the Micro:bit to move a bucket at the bottom to **catch it** before it hits the ground.

---

### 3️⃣ **Step-by-Step Coding Guide**

---

✅ **Step 1: Import Libraries**

```python
from microbit import *
import random
```

We need `microbit` for LED and tilt controls, and `random` for drop positions.

---

✅ **Step 2: Set Up Game Variables**

```python
drop_x = random.randint(0, 4)
drop_y = 0
bucket_x = 2
score = 0
```

* `drop_x`, `drop_y` → position of the falling drop
* `bucket_x` → where the player’s bucket sits
* `score` → player’s current score

---

✅ **Step 3: Game Loop**

```python
while True:
    display.clear()
```

We’ll continuously redraw the screen so it updates as the drop falls.

---

✅ **Step 4: Read Tilt Movement**

```python
    x = accelerometer.get_x()

    if x < -200 and bucket_x > 0:
        bucket_x -= 1
    elif x > 200 and bucket_x < 4:
        bucket_x += 1
```

👉 Tilting left or right moves the bucket.
We also keep it within the screen edges (0–4).

---

✅ **Step 5: Move the Drop**

```python
    drop_y += 1
```

Each loop makes the raindrop fall one row lower.

---

✅ **Step 6: Check for Catch or Miss**

```python
    if drop_y == 4:
        if drop_x == bucket_x:
            score += 1
            display.show(Image.HAPPY)
        else:
            score -= 1
            display.show(Image.SAD)
        sleep(500)
        drop_x = random.randint(0, 4)
        drop_y = 0
```

When the drop reaches the bottom row:

* If it lands on the same x-position as the bucket → **catch it!**
* Otherwise → **miss!**

---

✅ **Step 7: Draw Drop and Bucket**

```python
    display.set_pixel(drop_x, drop_y, 9)
    display.set_pixel(bucket_x, 4, 5)
    sleep(500)
```

This shows both the falling drop and the player’s bucket at the same time.

---

✅ **Step 8: Full Code**

```python
from microbit import *
import random

drop_x = random.randint(0, 4)
drop_y = 0
bucket_x = 2
score = 0

while True:
    display.clear()

    # Move bucket using tilt
    x = accelerometer.get_x()
    if x < -200 and bucket_x > 0:
        bucket_x -= 1
    elif x > 200 and bucket_x < 4:
        bucket_x += 1

    # Move drop down
    drop_y += 1

    # Check if drop reaches the bottom
    if drop_y == 4:
        if drop_x == bucket_x:
            score += 1
            display.show(Image.HAPPY)
        else:
            score -= 1
            display.show(Image.SAD)
        sleep(500)
        drop_x = random.randint(0, 4)
        drop_y = 0

    # Draw drop and bucket
    display.set_pixel(drop_x, drop_y, 9)
    display.set_pixel(bucket_x, 4, 5)
    sleep(500)
```

---

### 🧠 **Discussion & Reflection**

💬 Ask pupils:

* How does tilt affect the bucket’s movement?
* How can we make the game more challenging?
* What happens if we make the drop fall faster?

---

### 🚀 **Extension Ideas**

* Increase drop speed as score increases.
* Display the score after 10 drops.
* Add sound effects when catching or missing.
* Add a “Game Over” animation when the score drops below 0.
* Use different LED brightness for water splash effects.

---

### ✅ **Wrap-Up**

By the end of the session, students can:

* Use accelerometer inputs to control movement.
* Use variables to track position and score.
* Create a working **Catch the Drop** game with feedback and logic.

---
