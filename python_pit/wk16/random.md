# 📝 Python Workshop: **"Rolling the Dice – Fun with Random Numbers!"**

**Target Age:** 10–12 years

**Length:** 1.5 hours

**IDE:** Thonny

**Theme:** Using the `random` library to generate numbers for fun and games.

**Final Outcome:** Students create a simple number guessing game.

---

## 1️⃣ Why This Topic is Important (10 minutes – Discussion)

**Class prompts:**

* "Have you ever rolled a dice in a board game? You don’t know which number will come up – that’s randomness."
* "Why do games need randomness?" (Possible answers: enemies moving differently, loot drops, shuffling cards.)
* "Do you think randomness is only for games?" (Also in weather forecasts, password generation, testing.)

**Key point:** Random numbers make programs **unpredictable and exciting**, and they’re also used in many serious applications.

---

## 2️⃣ Coding Concepts for This Workshop

Students will learn:

* **Importing libraries** – `import random`.
* **Generating random numbers** – `random.randint(start, end)`.
* **Using random numbers in programs** – decisions, movement, selections.
* **Variables** – storing results.
* **Conditionals** – `if` statements to act on random values.
* **Loops** – repeating until a condition is met.
* **Recognising when randomness is useful** – games, simulations, unpredictability.

---

## 3️⃣ Project Introduction: Number Guessing Game 🎯

**Scenario:**
You are making a game where the computer chooses a **random number between 1 and 10**, and the player has to guess it.

**Requirements:**

1. Import the `random` library.
2. Generate a random number between 1 and 10.
3. Let the user guess until they get it right.
4. Tell the user if their guess is too high or too low.
5. Count the number of attempts.

---

## 4️⃣ Step-by-Step Activities with Testable Code

---

### **Activity 1: Importing and Creating a Random Number** (10 minutes)

```python
import random

number = random.randint(1, 10)
print(number)
```

✅ Test: Run it several times – the number changes!
💬 Ask: "Why don’t we get the same number each time?"

---

### **Activity 2: Using the Random Number in a Decision** (10 minutes)

```python
import random

dice_roll = random.randint(1, 6)

if dice_roll == 6:
    print("You rolled a 6! You get another turn!")
else:
    print("You rolled a", dice_roll)
```

✅ Test: Run multiple times – sometimes you get a special message.

---

### **Activity 3: Random Choice from a List** (10 minutes)

```python
import random

animals = ["dog", "cat", "penguin", "lion"]
chosen_animal = random.choice(animals)
print("You got a", chosen_animal)
```

✅ Test: Students make their own animal lists.
💬 Ask: "Where could this be useful in a game?"

---

### **Activity 4: Build the Number Guessing Game – Step 1** (10 minutes)

**Generate the number and take one guess.**

```python
import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("You guessed it!")
else:
    print("Nope! The number was", secret_number)
```

✅ Test: Students play a few rounds.

---

### **Activity 5: Add a Loop to Keep Guessing** (15 minutes)

```python
import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("You guessed it in", attempts, "tries!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
```

✅ Test: Students play until they win.
💬 Ask: "How could we make this harder or easier?"

---

### **Activity 6: Bonus Random Features** (Optional – 10 minutes)

Ideas for extra fun:

* Let the range change (`1–20` or `1–100`).
* Limit guesses to 5 tries.
* Make a "computer guessing your number" version.
* Add random funny responses when wrong.

---

## 5️⃣ Reflection: Recognising When to Use Randomness (10 minutes)

Brainstorm situations where randomness is useful:

* Board games
* Enemy movement in games
* Random rewards in apps
* Password generation
* Testing programs

---

## 6️⃣ Wrap-Up (5 minutes)

* Review: How to import, generate, and use random numbers.
* Quick challenge: Students make a **random coin flip** program in 2 lines.

```python
import random
print(random.choice(["Heads", "Tails"]))
```

---

## Materials Needed

* Thonny installed.
* Whiteboard for brainstorming.
* Handout with:

  * `import random`
  * `random.randint(start, end)`
  * `random.choice(list)`

---
