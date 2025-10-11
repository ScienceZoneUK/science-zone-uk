# 🥔🔥 Student Handout — Micro:bit **Hot Potato Game**

---

## 🎯 Learning Goals

By the end of this session, I will be able to:

* Define what a **random timer** is.
* Describe how the Micro:bit can use **time and lights** to make a game.
* Use code to build a **Hot Potato** game.
* Test and improve the game by adding new features.

---

## 1️⃣ What Is Hot Potato?

💬 Think & Discuss:

* Have you ever played *Hot Potato* before?
* What happens when the music stops or timer ends?
* What makes it exciting?

📌 **Goal:**
Don’t get caught holding the “potato” when it explodes! 💥

---

## 2️⃣ The Challenge 🎮

We want to make a Micro:bit game that:

* Starts when **Button A** is pressed.
* Runs for a **random time** (between 3–10 seconds).
* Flashes or makes sounds while it’s “hot.”
* Ends with a **BOOM!** sound and explosion image.

✏️ Write:
What could make this game more fun or dramatic?

---

---

## 3️⃣ Build the Game Step by Step

✅ **Step 1: Start Up Code**

```python
from microbit import *
import random
import music
```

👉 This gets the Micro:bit ready for lights 🎇, sounds 🎵, and random timing 🎲.

---

✅ **Step 2: Wait for the Player**

```python
display.show(Image.HAPPY)
while not button_a.was_pressed():
    sleep(100)
```

👉 The game waits until someone presses **Button A** to start.

---

✅ **Step 3: Set the Random Timer**

```python
time_limit = random.randint(3000, 10000)
elapsed = 0
```

👉 The timer will run for a random time between **3 and 10 seconds**.

✏️ Why do you think using *random* makes the game more exciting?

---

---

✅ **Step 4: Start the Countdown**

```python
display.show(Image.TRIANGLE)
music.play(['C4:2', 'D4:2', 'E4:2'], wait=False)

while elapsed < time_limit:
    display.show(Image.ALL_CLOCKS, delay=100, wait=False)
    sleep(100)
    elapsed += 100
```

👉 The triangle shows the potato is “hot”!
👉 The clocks spin and beep until the timer ends.

---

✅ **Step 5: Explosion! 💥**

```python
display.show(Image.SKULL)
music.play(['C5:1', 'B4:1', 'A4:1', 'G4:2'])
display.scroll("BOOM!")
```

👉 The potato **explodes**! Whoever’s holding the Micro:bit loses that round.

---

✅ **Step 6: Full Code**

```python
from microbit import *
import random
import music

while True:
    display.show(Image.HAPPY)
    while not button_a.was_pressed():
        sleep(100)

    time_limit = random.randint(3000, 10000)
    elapsed = 0

    display.show(Image.TRIANGLE)
    music.play(['C4:2', 'D4:2', 'E4:2'], wait=False)

    while elapsed < time_limit:
        display.show(Image.ALL_CLOCKS, delay=100, wait=False)
        sleep(100)
        elapsed += 100

    display.show(Image.SKULL)
    music.play(['C5:1', 'B4:1', 'A4:1', 'G4:2'])
    display.scroll("BOOM!")

    sleep(2000)
```

---

## 4️⃣ Test & Reflect

💬 Try your game with friends!

* Who got “BOOM!” the most? 😅
* Did everyone get a fair chance?
* How could you tell the potato was about to explode?

✏️ Write down your test results:

---

---

---

## 5️⃣ Challenge Time 🚀

Choose one or more upgrades to make your version of **Hot Potato Plus+**!

🔹 Add **faster flashing lights** as time runs out.
🔹 Add **music that speeds up** before the explosion.
🔹 Make the potato **vibrate or shake** before BOOM (using gesture).
🔹 Add a **score system** for multiple rounds.
🔹 Create a **custom animation** instead of the skull.

✏️ Draw your custom explosion animation here:

```
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
```

---

## ✅ Wrap-Up

Today I:

* Learned about **random timers** and **loops**.
* Used **sound, images, and timing** to create a fun game.
* Tested my game with others.
* Designed new ideas to make the game even better!

---
