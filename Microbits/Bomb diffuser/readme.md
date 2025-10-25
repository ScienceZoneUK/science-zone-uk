---

# 💣 **Micro:bit Game: Bomb Defuse**

---

## 🎯 **Learning Objectives (Bloom’s Taxonomy)**

| Bloom’s Level        | Learning Objective                                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| 🔵 **Remembering**   | Pupils will be able to **recall** how to use time delays and button inputs.                              |
| 🟢 **Understanding** | Pupils will be able to **describe** how a countdown timer works in a program.                            |
| 🟡 **Applying**      | Pupils will be able to **use** loops and conditions to create a working countdown.                       |
| 🟠 **Analysing**     | Pupils will be able to **compare** different strategies to “defuse” the bomb before time runs out.       |
| 🔴 **Evaluating**    | Pupils will be able to **justify** their design choices (e.g., button combinations, timing).             |
| 🟣 **Creating**      | Pupils will be able to **design** their own bomb-defuse variation with sound, flashing lights, or clues. |

---

## ⏱️ **Lesson Flow (Teacher Guide)**

---

### 1️⃣ **Introduction (10 mins)**

💬 **Ask students:**

* What happens in movies when there’s a ticking bomb?
* How do people try to defuse it?
* What makes it tense or exciting?

📌 **Explain:**
We’ll simulate that tension using the **Micro:bit**!
The Micro:bit bomb will **count down** and **explode** unless you press the **correct combination of buttons** in time.

---

### 2️⃣ **The Problem: Build a Bomb Defuse Game (5 mins)**

We need to make a Micro:bit that:

* Starts a countdown timer (random between 5–15 seconds ⏱️)
* Beeps or flashes as time runs out 🔊💡
* Allows the player to press a **secret button combination** (e.g., A+B) to defuse it
* Explodes if not defused in time 💥

💬 **Discussion Prompt:**

* What could make the game more exciting?
* How could we give players clues about when it’s about to explode?

---

## 🧠 **Step-by-Step Coding Guide**

---

**Step 1: Import Libraries**

```python
from microbit import *
import random
import music
```

We’ll use:

* `microbit` → display, buttons
* `random` → random countdown
* `music` → ticking and explosion sounds

---

**Step 2: Set a Random Timer**

```python
timer = random.randint(5, 15)
```

💡 Each round, the bomb timer is random — players never know how much time they have!

---

 **Step 3: Start the Countdown**

```python
while timer > 0:
    display.show(str(timer))
    music.play(['C4:1'], wait=False)
    sleep(1000)
    timer -= 1
```

💡 The Micro:bit shows numbers counting down from `timer` to 0, with a short beep every second.

---

**Step 4: Check for Defuse Attempt**

Inside the same loop, we’ll check if **both buttons** are pressed:

```python
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HAPPY)
        music.play(['C5:2'])
        display.scroll("DEFUSED!")
        break
```

💡 If the player presses A+B together, the bomb is **defused** and the loop stops.

---

 **Step 5: Explosion if Not Defused**

After the loop ends, if time reaches zero, the bomb explodes:

```python
if timer == 0:
    display.show(Image.SKULL)
    music.play(['C5:1', 'B4:1', 'A4:1', 'G4:3'])
    display.scroll("BOOM!")
```

💥 The skull icon and explosion sound appear if the player doesn’t defuse in time.

---

**Step 6: Full Code**

```python
from microbit import *
import random
import music

while True:
    display.scroll("ARMED!")
    timer = random.randint(5, 15)

    while timer > 0:
        display.show(str(timer))
        music.play(['C4:1'], wait=False)
        sleep(1000)
        timer -= 1

        # Check for defuse
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(Image.HAPPY)
            music.play(['C5:2'])
            display.scroll("DEFUSED!")
            break

    # If not defused
    if timer == 0:
        display.show(Image.SKULL)
        music.play(['C5:1', 'B4:1', 'A4:1', 'G4:3'])
        display.scroll("BOOM!")

    sleep(2000)
    display.clear()
```

---

## 🧩 **Extension Challenges**

---

### 🚀 Challenge 1: Add Flashing Lights

Make LEDs flash faster as the timer approaches zero:

```python
if timer <= 3:
    display.show(Image.ARROW_N)
    sleep(100)
    display.clear()
    sleep(100)
```

---

### 🔊 Challenge 2: Faster Beeping

Make the ticking sound faster near the end by reducing the `sleep` time.

---

### 🧠 Challenge 3: Add a Secret Code

Instead of pressing both buttons, make a **button sequence** to defuse (e.g., A → B → A → shake).

Hint:

```python
sequence = ["A", "B", "A"]
```

Track presses to check if they match!

---

### 🧨 Challenge 4: Add a “Lives” System

Give the player 3 tries before total failure — add a variable `lives = 3` and subtract when missed.

---

### 🕵️ Challenge 5: Add Clues

Use the Micro:bit’s **display** to show hints like “Too slow!” or “Faster!” near the end.

---

## 💬 **Reflection Questions**

* What happens when you press the wrong buttons?
* How could you make the game fairer or more difficult?
* What could you change to make your version unique?

---

## **Wrap-Up**

By the end of this lesson, students can:

* Use **loops and conditions** to build a timed game
* Apply **random numbers** to make gameplay unpredictable
* Combine **buttons, sounds, and visuals**
* Create a working **Bomb Defuse Game** with real tension and creativity 🎮💥

---

