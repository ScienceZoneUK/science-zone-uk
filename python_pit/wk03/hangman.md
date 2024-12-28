# Hangman Game Tutorial

Welcome to the **Hangman Game Tutorial**! In this tutorial, you'll learn how to build the classic Hangman game step-by-step using Python. By the end, you'll have a fully working game that you can customize and show off to your friends.

## Prerequisites

This tutorial is designed for beginners. All you need is:

- Basic knowledge of Python (variables, loops, if-statements).
- A Python environment installed on your computer.

---

## Part 1: Getting Started with Hangman

In this part, we'll:

1. Randomly pick a word for the game.
2. Ask the user to guess a letter.
3. Check if the guessed letter is in the word.

### Code

```python
from random import choice

# Step 1: Create a list of words for the game
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)

# TODO-2: Ask the user to guess a letter and make it lowercase.
guess = input("Guess a letter a-z: ").lower()

# TODO-3: Check if the guessed letter is in the chosen_word and print "Right" if it is, "Wrong" if it’s not.
if guess in chosen_word:
    print("Right!")
else:
    print("Wrong!")
```

### Test It Out

1. Run the code.
2. Try guessing different letters. What happens when you guess correctly or incorrectly?

---

## Part 2: Revealing the Word

Now we'll:

1. Create a placeholder for the word using underscores.
2. Reveal the guessed letters in the word.

### Code

```python
from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
guess = input("Guess a letter a-z: ").lower()

# TODO-1: Create a placeholder for the word with underscores.
placeholder = "_" * len(chosen_word)
print(f"Hint: {placeholder}")

# TODO-2: Reveal the guessed letter in the correct position.
display = ""
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display += guess
    else:
        display += placeholder[i]
print(display)
```

### Test It Out

1. Guess letters and see them revealed in the correct positions.
2. Try letters that aren’t in the word. What happens?

---

## Part 3: Keep Guessing Until You Win

We’ll now:

1. Let the user keep guessing until they’ve guessed the entire word.
2. Stop the game when all blanks (“\_”) are gone.

### Code

```python
from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = "_" * len(chosen_word)

while "_" in display:
    guess = input("Guess a letter a-z: ").lower()

    new_display = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    display = new_display
    print(display)

print("You win!")
```

### Test It Out

1. Keep guessing until you’ve completed the word.
2. Try letters that don’t exist in the word. Does it still work?

---

## Part 4: Adding Lives and ASCII Art

Time to make it more challenging! We’ll:

1. Add lives to the game.
2. End the game if the user runs out of lives.
3. Add ASCII art to make it fun.

### Code

```python
from random import choice

word_list = ["aardvark", "baboon", "camel"]
stages = [
    r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

chosen_word = choice(word_list)
display = "_" * len(chosen_word)
lives = 6

while "_" in display and lives > 0:
    guess = input("Guess a letter a-z: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(stages[6 - lives])
        print(f"You have {lives} lives left.")

    new_display = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    display = new_display
    print(display)

if "_" not in display:
    print("You win!")
else:
    print(f"You lose! The word was {chosen_word}.")
```

### Test It Out

1. Guess wrong and see your lives decrease.
2. Notice the ASCII art change as lives decrease.
3. Try losing all lives. What happens?

---

## Part 5: Adding Custom Word Lists and Enhancements

Let’s finish with some improvements:

1. Import a larger word list.
2. Import ASCII art and a logo from external files.
3. Prevent repeated guesses from deducting lives.

### Code

```python
from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = choice(word_list)
display = "_" * len(chosen_word)
lives = 6
guessed_letters = []

while "_" in display and lives > 0:
    guess = input("Guess a letter a-z: ").lower()

    if guess in guessed_letters:
        print(f"You’ve already guessed {guess}!")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that’s not in the word. You lose a life.")
        print(stages[6 - lives])
        print(f"You have {lives} lives left.")

    new_display = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    display = new_display
    print(display)

if "_" not in display:
    print("You win!")
else:
    print(f"You lose! The word was {chosen_word}.")
```

---

## Next Steps

Congratulations on completing your Hangman game! Here are some ideas to expand it:

- Add a difficulty setting (e.g., easy, medium, hard).
- Allow the user to pick their own word list.
- Save high scores to a file.

Keep coding and have fun!
