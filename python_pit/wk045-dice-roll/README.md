# 📝 Python Workshop: **“Rolling the Dice – Randomness, Timing & Fun with ASCII Art!”**

**Age Group:** 10–12 years
**Duration:** 1.5 hours
**Platform:** Thonny IDE
**Theme:** Using random numbers and the sleep function to simulate dice rolls
**Final Project:** A console-based dice rolling simulator with animated delays and ASCII art

---

## 🎯 Learning Objectives (Aligned to Bloom’s Taxonomy)

By the end of the workshop, students should be able to:

1. **Remember** how to create random numbers in Python.
2. **Understand** what the `sleep()` function does and how to use it.
3. **Apply** random numbers and sleep delays in a program to simulate rolling dice.
4. **Analyze** and explain how the dice roll simulator works.
5. **Create** an attractive text-based dice rolling program using ASCII art.

---

## 🗣️ 1. Discussion – Why Is This Topic Important? (10 minutes)

Start with an engaging chat:

* “How do games like Monopoly or Dungeons & Dragons decide your move?”
* “Why do computers need random numbers?”
* “Have you ever seen a loading animation or delay before something happens in a game?”

**Key takeaway:**
Randomness makes games **unpredictable and fun**, and adding small pauses with `sleep()` can make your program feel **alive** and more like a real-world simulation.

---

## 🧩 2. Coding Concepts to Be Covered

| Concept                | Explanation                                 |
| ---------------------- | ------------------------------------------- |
| `import random`        | Used to generate random numbers             |
| `random.randint(a, b)` | Returns a random integer between a and b    |
| `import time`          | Gives access to the `sleep()` function      |
| `time.sleep(seconds)`  | Pauses the program for a given time         |
| ASCII art              | Drawing pictures with text characters       |
| `while` loops          | Repeating actions (like rolling dice again) |
| `if` statements        | To match dice numbers to ASCII art          |
| `input()`              | To let users interact with the program      |

---

## 🎮 3. Project Introduction – Dice Roll Simulator

**Project Idea:**
Students will create a **Dice Roll Simulator** that:

* Randomly rolls a dice (1–6).
* Displays a short delay before showing the result (using `time.sleep()`).
* Shows an **ASCII art** picture of the dice face.
* Lets the user roll again or quit.

**Project Requirements:**

* Must use `random.randint()`.
* Must use `time.sleep()` for a short delay.
* Must include ASCII art for all 6 sides of a dice.
* Must use a loop to let the user roll multiple times.

---

## 🧱 4. Step-by-Step Activities with Testable Code

---

### 🥇 **Step 1: Import Libraries**

Explain that you need both `random` and `time` for this project.

```python
import random
import time
```

✅ *Test:* No output, but make sure there’s no red underline in Thonny.

---

### 🎲 **Step 2: Generate a Random Dice Roll**

Introduce `random.randint(1, 6)` and print the result.

```python
import random

roll = random.randint(1, 6)
print("You rolled a", roll)
```

✅ *Test:* Run it several times — does it change each time?

---

### ⏳ **Step 3: Add a Rolling Delay**

Explain that `time.sleep()` pauses the program.

```python
import random
import time

print("Rolling the dice...")
time.sleep(1.5)  # waits for 1.5 seconds
roll = random.randint(1, 6)
print("You rolled a", roll)
```

✅ *Test:* It should say “Rolling the dice…” then pause, then show the number.

---

### 🎨 **Step 4: Add ASCII Art for the Dice Faces**

Introduce ASCII art to make the dice look cool:

```python
dice_art = {
    1: (
        "---------\n"
        "|       |\n"
        "|   o   |\n"
        "|       |\n"
        "---------"
    ),
    2: (
        "---------\n"
        "| o     |\n"
        "|       |\n"
        "|     o |\n"
        "---------"
    ),
    3: (
        "---------\n"
        "| o     |\n"
        "|   o   |\n"
        "|     o |\n"
        "---------"
    ),
    4: (
        "---------\n"
        "| o   o |\n"
        "|       |\n"
        "| o   o |\n"
        "---------"
    ),
    5: (
        "---------\n"
        "| o   o |\n"
        "|   o   |\n"
        "| o   o |\n"
        "---------"
    ),
    6: (
        "---------\n"
        "| o   o |\n"
        "| o   o |\n"
        "| o   o |\n"
        "---------"
    ),
}
```

✅ *Test:* No output yet — just check for syntax errors.

---

### 🎮 **Step 5: Combine Everything**

Now, let’s roll the dice and print the ASCII art result.

```python
import random
import time

dice_art = {
    1: ("---------\n|       |\n|   o   |\n|       |\n---------"),
    2: ("---------\n| o     |\n|       |\n|     o |\n---------"),
    3: ("---------\n| o     |\n|   o   |\n|     o |\n---------"),
    4: ("---------\n| o   o |\n|       |\n| o   o |\n---------"),
    5: ("---------\n| o   o |\n|   o   |\n| o   o |\n---------"),
    6: ("---------\n| o   o |\n| o   o |\n| o   o |\n---------"),
}

print("Rolling the dice...")
time.sleep(1.5)
roll = random.randint(1, 6)
print(dice_art[roll])
print("You rolled a", roll)
```

✅ *Test:* Run it — it should show the ASCII dice face for a random roll.

---

### 🔁 **Step 6: Let the User Roll Again**

Add a loop and input prompt:

```python
import random
import time

dice_art = {
    1: ("---------\n|       |\n|   o   |\n|       |\n---------"),
    2: ("---------\n| o     |\n|       |\n|     o |\n---------"),
    3: ("---------\n| o     |\n|   o   |\n|     o |\n---------"),
    4: ("---------\n| o   o |\n|       |\n| o   o |\n---------"),
    5: ("---------\n| o   o |\n|   o   |\n| o   o |\n---------"),
    6: ("---------\n| o   o |\n| o   o |\n| o   o |\n---------"),
}

while True:
    input("Press ENTER to roll the dice...")
    print("Rolling the dice...")
    time.sleep(1.5)
    roll = random.randint(1, 6)
    print(dice_art[roll])
    print("You rolled a", roll)
    
    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 🎲")
        break
```

✅ *Test:* Try rolling multiple times — does it loop correctly?

---

### 🌟 **Step 7: Challenge Ideas (Optional)**

If there’s extra time:

* Add a **double-dice roll** (roll two dice at once and show both).
* Keep a **score counter** for total points.
* Make the **delay random** (between 0.5–2 seconds).

---

## 🧠 5. Reflection & Wrap-Up (10 minutes)

**Class Discussion:**

* What does `random.randint()` do?
* What does `time.sleep()` do?
* How could we use these in a game (e.g., waiting for a turn, countdown timers)?
* How did we make the dice look more fun using ASCII art?

✅ *Exit Ticket:* Ask students to explain the line `roll = random.randint(1, 6)` in their own words.

---

## 🧰 Materials Needed

* Computers with Thonny installed
* Projector/whiteboard for code walkthrough
* Printable ASCII art examples (optional)

---

## 💡 Extension Ideas for Next Workshops

* Add **sound effects** (using `winsound` on Windows).
* Turn it into a **“Race to 20”** game using dice rolls and points.
* Combine with **file handling** to save total scores between runs.
