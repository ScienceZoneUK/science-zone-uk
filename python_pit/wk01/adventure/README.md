
# Adventure Game - Step-by-Step Guide

This is a step-by-step guide to building a simple text-based adventure game in Python. The game involves a player navigating through various scenarios by making choices. Incorrect choices result in failure, while correct choices lead to progression.

---

## Step 1: Introduction and Setup

1. Open your favorite Python IDE or text editor.
2. Create a new Python file, e.g., `adventure_game.py`.
3. Add an introductory message to welcome the player:

```python
print("Welcome to the Adventure Game!")
print("You find yourself at the entrance of a mysterious forest.")
print("Your goal is to navigate safely through the forest and uncover its secrets.")
```

---

## Step 2: First Decision - Enter or Walk Away

1. Add a choice for the player to either enter the forest or walk away:

```python
choice1 = input("\nDo you want to ENTER the forest or WALK AWAY? (enter/walk): ").lower()

if choice1 == "enter":
    # Proceed to the next stage of the game
    print("\nYou step into the forest. The atmosphere is eerie, and the sound of rustling leaves surrounds you.")
elif choice1 == "walk":
    # End the game
    print("\nYou decide the forest is too dangerous and walk away. Perhaps another adventure awaits you.")
    print("Game Over.")
else:
    # Handle invalid input
    print("\nYou hesitate too long at the entrance, and the opportunity passes. The adventure ends before it begins.")
```

---

## Step 3: Fork in the Path - Left or Right

1. If the player enters the forest, present them with a fork in the path:

```python
choice2 = input("You come across a fork in the path. Do you go LEFT towards the sound of running water or RIGHT into the darker trail? (left/right): ").lower()

if choice2 == "left":
    # Proceed to the next scenario
    print("\nYou follow the sound of water and reach a tranquil stream. Suddenly, a troll appears!")
elif choice2 == "right":
    # End the game
    print("\nYou walk down the darker trail, and the shadows grow deeper. Suddenly, you fall into a pit!")
    print("There was no way out of the pit. You failed.")
else:
    # Handle invalid input
    print("\nYou stand indecisively at the fork, and the forest creatures take notice. It's not safe here. You failed.")
```

---

## Step 4: Troll Encounter - Talk or Run

1. If the player goes left, they encounter a troll who demands a password:

```python
choice3 = input("The troll demands a password to cross the stream. Do you try to TALK to it or RUN away? (talk/run): ").lower()

if choice3 == "talk":
    print("\nThe troll grins and asks: 'What is the square root of 64?'")
    answer = input("Your answer: ").strip()

    if answer == "8":
        print("\nThe troll nods in approval and lets you cross the stream. You've survived this encounter!")
        print("You continue your adventure and eventually uncover the forest's hidden treasures. Congratulations!")
    else:
        print("\nThe troll growls in anger. 'Wrong answer!' It throws you into the stream. You failed.")
else:
    print("\nYou turn to run, but the troll is faster. It grabs you and tosses you into the stream. You failed.")
```

---

## Step 5: Finalizing the Game

1. Add an overall structure to run the game as a single function:

```python
def adventure_game():
    # Add all the game logic here
    # Start with the introduction
    # Follow the decisions step by step

# Run the game
adventure_game()
```

2. Save the file and run it using Python.

---

## Step 6: Enhancements (Optional)

1. Add more scenarios and branching paths.
2. Implement a scoring system or inventory for added complexity.
3. Create a retry mechanism to allow the player to play again after failure.

---

## Run the Game

To play the game, open a terminal and run the following command:

```bash
python adventure_game.py
```

Enjoy your adventure!

