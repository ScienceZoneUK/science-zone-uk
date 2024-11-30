## Rock paper scissors

https://wrpsa.com/

### The Basic Rules of RPS

Despite its underlying complexity, the game’s rules are straightforward. 
Players deliver hand signals representing rock, paper, or scissors, with 
the outcome determined by these three rules:

```text
    Rock wins against scissors.
    Scissors win against paper.
    Paper wins against rock.
```

1. Import necessary libraries
    - Import `random` for the computer's choice

2. Define ASCII art for gestures
    - Store each ASCII art (e.g., rock, paper, scissors) in a variable
    -  each variable should be a gesture name (e.g., "rock", "paper", "scissors")
    - Make a list of the variable names

3. Create a function to display the game rules
    - Print the rules for the player

4. Create a function to get the player's choice
    - Prompt the player to choose "rock", "paper", or "scissors"
    - Validate the input to ensure it is one of the valid choices
    - Return the player's choice

5. Create a function to get the computer's choice
    - Use `random.choice()` to select between "rock", "paper", or "scissors"
    - Return the computer's choice

6. Create a function to determine the winner
    - Accept the player's choice and the computer's choice as arguments
    - Compare the choices using the rules of the game:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock
    - Return "Player wins", "Computer wins", or "Tie"

7. Create the main game loop
    - Display the game rules
    - Get the player's choice
    - Get the computer's choice
    - Display the ASCII art for both choices
    - Determine the winner
    - Print the result

8. Ask the player if they want to play again
    - If yes, repeat the game loop
    - If no, exit the game

9. End the program



```python    
############################################
#THE RPS GAME
############################################
import time
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
```
