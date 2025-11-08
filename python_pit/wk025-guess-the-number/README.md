# 📝 Python Workshop: **"Guess the Number!"**

**Age Group:** 10–12 years
**Duration:** 1.5 hours
**Platform:** Thonny IDE
**Theme:** Creating a number-guessing game using random numbers
**Final Outcome:** A game where the computer picks a random number, and the player has to guess it.

---

## 🎯 Learning Objectives (Aligned to Bloom’s Taxonomy)

By the end of this session, students should be able to:

1. **Remember** how to create random numbers using `random.randint()`.
2. **Understand** how a random number generator works in Python.
3. **Apply** their knowledge to write a program that generates and displays a random number.
4. **Analyze** and explain how user input and comparisons are used in the guessing logic.
5. **Create** a fully functional “Guess the Number” game that runs in the console.

---

## 🗣️ 1. Discussion – Why This Topic Is Important (10 minutes)

Start by asking:

* “Have you ever played a guessing game before?”
* “How do games decide what number or word you have to guess?”
* “Why is randomness important in games or simulations?”

**Key Points:**

* Random numbers make games **unpredictable** and **fun**.
* Computers don’t naturally “guess”; they use **algorithms** to generate random numbers.
* Knowing how to use random numbers helps us build games, quizzes, and even simulations!

---

## 🧩 2. Coding Concepts to Be Covered

| Concept                | Explanation                                                |
| ---------------------- | ---------------------------------------------------------- |
| `import random`        | Imports the random number library.                         |
| `random.randint(a, b)` | Generates a random integer between `a` and `b`.            |
| `input()`              | Takes input from the player.                               |
| `int()`                | Converts a string input to an integer.                     |
| `if`, `elif`, `else`   | Used for decision making in guessing logic.                |
| `while` loop           | Allows multiple guesses until the correct number is found. |
| `print()`              | Displays messages to the player.                           |

---

## 🎮 3. Project Introduction – “Guess the Number” Game

**Scenario:**
We’re going to create a game where the computer thinks of a random number between 1 and 10, and the player has to guess it!
The computer will tell you if your guess is **too high**, **too low**, or **correct**.

**Requirements:**

* The program should generate a random number between 1 and 10.
* The player can enter guesses until they find the correct one.
* The program should give hints (“Too high” / “Too low”).
* The program should congratulate the player when they win.

---

## 🧱 4. Step-by-Step Activities with Testable Code

---

### 🥇 **Step 1: Import the Random Library**

Explain that before we can create random numbers, we must **import** the `random` module.

```python
import random
```

✅ **Test:** Run the code — no output, but check that there’s no red underline (syntax error).

---

### 🎲 **Step 2: Generate and Print a Random Number**

Introduce `random.randint()`, which picks a random number between two values.

```python
import random

number = random.randint(1, 10)
print("The random number is:", number)
```

✅ **Test:**
Run several times — does the number change between 1 and 10?

🧠 **Discuss:**
“What happens if we change `random.randint(1, 10)` to `random.randint(1, 100)`?”

---

### 💡 **Step 3: Add User Input**

Now, let’s ask the player for a guess.

```python
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
print("You guessed:", guess)
```

✅ **Test:**
Type a number and check that it prints correctly.

---

### ⚖️ **Step 4: Compare the Guess and the Number**

Add an `if` statement to check if the player’s guess matches the random number.

```python
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You guessed it!")
else:
    print("Sorry, that’s not right. The number was", number)
```

✅ **Test:**
Run it multiple times — sometimes you’ll win, sometimes not!

---

### 🔁 **Step 5: Keep Guessing Until You’re Right (Loop)**

Let’s use a **while loop** to let the player guess until they get it correct.

```python
import random

number = random.randint(1, 10)
guess = 0  # starting value

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
```

✅ **Test:**
Run it — it should keep asking until the correct number is guessed.

---

### 🌟 **Step 6: Make It More Exciting**

Add a **guess counter** and a fun message at the end.

```python
import random

number = random.randint(1, 10)
guess = 0
attempts = 0

print("Welcome to the Guess the Number Game!")
print("I’m thinking of a number between 1 and 10...")

while guess != number:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 You got it in {attempts} tries! The number was {number}.")
```

✅ **Test:**
Try to guess the number — it should count your attempts and end when correct.

---

### 🧠 **Optional Challenge: Make It Replayable**

If there’s extra time, let’s let the player play again.

```python
import random

play_again = "yes"

while play_again == "yes":
    number = random.randint(1, 10)
    guess = 0
    attempts = 0
    print("\nI'm thinking of a number between 1 and 10...")
    
    while guess != number:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
    
    play_again = input("Play again? (yes/no): ").lower()

print("Thanks for playing!")
```

✅ **Test:**
It should let the user choose to play again.

---

## 🧠 5. Reflection & Wrap-Up (10 minutes)

**Class Discussion:**

* What function created the random number?
* How does the computer know when to stop the loop?
* What happens if you remove `int()` from the `input()` line?
* How could you make the game more challenging?

✅ **Exit Ticket:**
Ask students to explain what `random.randint(1, 10)` and `while guess != number:` do in their own words.

---

## 🧰 Materials Needed

* Computers with Thonny installed
* Whiteboard or projector to demonstrate key lines
* Optional printed code outline for reference

---

## 💡 Extension Ideas (for advanced or fast finishers)

* Add difficulty levels (1–10, 1–50, 1–100).
* Add a timer to see how long it takes to guess.
* Save the player’s best score in a text file.
* Use ASCII art to make a visual game title screen.
