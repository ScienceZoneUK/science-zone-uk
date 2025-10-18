

# 📘 **Teacher’s Guide — Micro:bit Duel Game**

---

## 🎯 Learning Objectives (Bloom’s Taxonomy)

By the end of this lesson, pupils will be able to:

* 🔵 **Remembering**: Define what an input event is (button press).
* 🟢 **Understanding**: Describe how the Micro:bit can compare timing between players.
* 🟡 **Applying**: Use Micro:bit buttons and timing functions to detect the fastest player.
* 🟠 **Analysing**: Compare different players’ reaction speeds.
* 🔴 **Evaluating**: Reflect on what makes a fair duel.
* 🟣 **Creating**: Design their own Duel variations (e.g., sound effects, LED animations, or best-of-three).

---

## 🕒 Lesson Flow

---

### 1️⃣ Introduction (10 mins)

💬 **Discussion Questions:**

* Have you ever played a reflex game like *Quick Draw* or *Snap*?
* What makes it exciting or fair?
* How can we tell who reacts first?

📌 **Highlight:**
In a **Micro:bit Duel**, players must **wait for the signal**, then **press their button as fast as possible**.
If you press too early — you lose automatically!

---

### 2️⃣ Problem Setup (5–10 mins)

🌟 **Duel Game Challenge:**
We need to make a Micro:bit that:

* Waits for a random time before the “Go!” signal ⚡
* Shows a quick icon (like a heart or target 🎯)
* Detects which player pressed their button first
* Announces who wins or loses

💬 **Discussion Prompt:**

* How can we make the game fair?
* What should happen if both press too soon?

---

## 🧠 Coding Step by Step

---

✅ **Step 1: Import Libraries**

```python
from microbit import *
import random
```

---

✅ **Step 2: Start the Duel**

```python
display.scroll("Ready...")
sleep(random.randint(2000, 5000))
display.show(Image.TARGET)
```

👉 Random wait between 2–5 seconds keeps players guessing.

---

✅ **Step 3: Check Who Presses First**

```python
start_time = running_time()
winner = None

while True:
    if button_a.was_pressed():
        winner = "A"
        break
    elif button_b.was_pressed():
        winner = "B"
        break
```

👉 As soon as one player presses, the loop stops and stores the winner.

---

✅ **Step 4: Show the Winner**

```python
if winner == "A":
    display.scroll("A Wins!")
elif winner == "B":
    display.scroll("B Wins!")
```

---

✅ **Step 5: Handle Early Presses**

If someone presses **before** the signal appears, they lose automatically.

Add this check **before showing the target**:

```python
display.scroll("Ready...")
early = False
for i in range(random.randint(20, 50)):
    if button_a.is_pressed() or button_b.is_pressed():
        early = True
        break
    sleep(100)

if early:
    display.scroll("Too Soon!")
    sleep(2000)
    reset()
```

---

✅ **Step 6: Full Code**

```python
from microbit import *
import random

while True:
    display.scroll("Ready...")

    # Random delay before showing target
    early = False
    for i in range(random.randint(20, 50)):
        if button_a.is_pressed() or button_b.is_pressed():
            early = True
            break
        sleep(100)

    if early:
        display.scroll("Too Soon!")
        sleep(2000)
        continue

    display.show(Image.TARGET)
    start_time = running_time()
    winner = None

    # Wait for a button press
    while True:
        if button_a.was_pressed():
            winner = "A"
            break
        elif button_b.was_pressed():
            winner = "B"
            break

    # Show the winner
    if winner == "A":
        display.scroll("A Wins!")
    elif winner == "B":
        display.scroll("B Wins!")

    sleep(2000)
```

---

## 🧩 Extension Ideas

✨ Encourage students to:

* ⏱️ Show the **reaction time** for each player.
* 🎶 Add **sound effects** (music.play) when someone wins or loses.
* 💥 Show a **countdown animation** before “Go!”.
* 🏆 Play a **best-of-three duel** and track scores.
* 🎨 Replace the “Target” with a custom image (like a lightning bolt ⚡).

---

## 🧠 Reflection Questions

💬 Ask pupils:

* What strategy helps you react quickly but not too soon?
* How could we make the game even fairer?
* How does using randomness make it more exciting?

---

## ✅ Wrap-Up

By the end of this lesson, pupils have:

* Used **random timing** and **input detection**
* Built a **competitive reaction game**
* Practised coding **loops, conditions, and variables**
* Learned how to handle **fair play** and **timing logic**

---

Would you like me to make the **Student Handout** next (with fill-in-the-blanks, testing section, and “Design Your Own Duel” challenge)?
