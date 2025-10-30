# 🧠 Python Workshop: **"True or False? Learning Booleans with Python"**

**Target Age:** 10–12 years
**Length:** 1.5 hours
**IDE:** Thonny
**Theme:** Learning and using Booleans in simple programs
**Final Project:** Build a short “Treasure Hunt” game using Boolean logic.

---

## 1️⃣ Why This Topic is Important (10 minutes – Discussion)

**Warm-up Questions:**

* “Have you ever had to make a yes/no decision before?”
  (e.g., “Is it raining?” → *If yes, bring an umbrella!*)
* “Computers make these yes/no decisions all the time — but they use something called **Booleans**.”

**Explain simply:**
Booleans are a special type of data in Python that can only be **True** or **False**.
They help computers make decisions like:

* Should the player win or lose?
* Is the score high enough?
* Did the player press the right button?

**Key takeaway:**
Booleans are the foundation of **logic** in coding — they control how programs “think.”

---

## 2️⃣ Coding Concepts for This Workshop

Students will learn:

* What a **Boolean** is (`True`, `False`).
* How to evaluate **Boolean expressions** (`>`, `<`, `==`, `!=`).
* How to use **comparison operators**.
* How to combine Boolean values using:

  * **`and`** – both must be true
  * **`or`** – at least one is true
  * **`not`** – flips True/False
* Using Booleans in **`if` statements**.
* Recognising where Boolean logic is used in programs and games.

---

## 3️⃣ Project Introduction: **Treasure Hunt Game 🏝️**

**Scenario:**
You’re lost on an island. You need to find the hidden treasure — but you’ll have to make the right True/False decisions to survive!

**Requirements:**

1. Use Boolean expressions to check conditions (e.g., “Do you have a key?”).
2. Use `if` statements to branch the story.
3. Combine conditions using `and`, `or`, and `not`.
4. Make the game respond to user choices.

---

## 4️⃣ Step-by-Step Activities with Testable Code

---

### **Activity 1: True and False Values** (10 minutes)

```python
# Booleans are True or False
print(True)
print(False)

# You can store them in variables
is_raining = True
is_sunny = False

print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)
```

✅ Test: Run and see printed True/False values.
💬 Ask: “Can a Boolean be both True and False?” (No!)

---

### **Activity 2: Boolean Expressions (Comparisons)** (10 minutes)

```python
print(5 > 3)   # True
print(4 < 1)   # False
print(10 == 10) # True
print(7 != 2)  # True
```

✅ Test: Try changing numbers to predict results.
💬 Ask: “Which ones are True? Why?”

---

### **Activity 3: Using Booleans in If Statements** (10 minutes)

```python
age = int(input("How old are you? "))

if age >= 10:
    print("You can play this game!")
else:
    print("Sorry, too young!")
```

✅ Test: Enter different ages to see what happens.
💬 Ask: “What happens if the condition is False?”

---

### **Activity 4: Combining Conditions (AND, OR, NOT)** (15 minutes)

```python
# AND example: both must be True
has_key = True
door_locked = True

if has_key and door_locked:
    print("You unlock the door and go inside!")
else:
    print("You can’t open the door.")

# OR example: one must be True
raining = False
umbrella = True

if raining or umbrella:
    print("You’re safe from the rain!")
else:
    print("You’ll get soaked!")

# NOT example: flips True/False
is_tired = False
if not is_tired:
    print("You feel great and ready for adventure!")
```

✅ Test: Change the values and predict what will print.
💬 Ask: “What would happen if we changed `and` to `or`?”

---

### **Activity 5: Build the Treasure Hunt Game – Step 1 (Base Story)** (20 minutes)

```python
print("🏝️ Welcome to Treasure Island!")
print("You wake up on a beach. There’s a forest ahead and a cave nearby.")

has_torch = False
found_treasure = False

choice = input("Do you go into the cave? (yes/no): ")

if choice == "yes":
    has_torch = True
    print("You found a torch in the cave!")
else:
    print("You stay outside. The forest looks dark...")

choice2 = input("Do you go into the forest? (yes/no): ")

if choice2 == "yes" and has_torch:
    found_treasure = True
    print("You light your torch and find a treasure chest! 🪙")
elif choice2 == "yes" and not has_torch:
    print("It’s too dark! You trip and find nothing.")
else:
    print("You wait by the beach. Maybe next time...")
```

✅ Test: Students play multiple times, changing their answers to see different paths.
💬 Ask: “Which decisions made it True or False that you found treasure?”

---

### **Activity 6: Add More Logic (Optional Bonus – 10 minutes)**

```python
if found_treasure:
    print("Congratulations! You win! 🏆")
else:
    print("Better luck next time...")
```

Challenge students to:

* Add more choices (e.g., “Do you swim to the boat?”)
* Add more Boolean flags (`has_map`, `has_key`, etc.)
* Use `and` and `or` to combine them.

---

## 5️⃣ Reflection & Wrap-Up (10 minutes)

**Recap Questions:**

* What are the two Boolean values?
* What does `>` mean? What about `==`?
* What’s the difference between `and`, `or`, and `not`?
* How did we use Booleans in our treasure game?

**Mini Challenge:**
Write a program that checks:

* If the player has both **a sword** *and* **a shield**, print “Ready for battle!”
* Otherwise, print “You need more gear!”

---

## 6️⃣ Materials Needed

* Computers with **Thonny** installed.
* Whiteboard to show Boolean logic flow.
* Optional: printout cheat sheet of Boolean operators and examples.

---

## ✅ Learning Outcomes Recap

By the end of this workshop, students should be able to:

* ✅ Describe what a Boolean is.
* ✅ Correctly evaluate Boolean expressions (`>`, `<`, `==`, `!=`).
* ✅ Recognize and use `and`, `or`, and `not`.
* ✅ Use Booleans in Python programs (decision-making).
* ✅ Recognize where Boolean logic is used in games and apps.
