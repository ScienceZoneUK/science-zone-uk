# Week 3 Challenge: Loops
# Instructions:
# 1. Modify the program to ask the user what difficulty level they want
# 2. Based on the user's input, change what range of number the computer can guess from (10, 100, 1000 etc.)
# 3. Ensure, if the user enters an invalid difficulty, they are asked again until they don't.

# We import the "random" and "time" libraries here for use later. You will learn more about how this works in Week 7
import random
import time

# Print a message to greet the user
print("Welcome to the Higher or Lower Game!")

# Ask for the difficulty
validDifficulty = False
targetRange = 10
# Keep looping until they enter a valid difficulty
while not validDifficulty:

    print("Which difficulty do you want to play?")
    difficulty = input("Easy, Medium or Hard: ")
    
    if difficulty.lower() == "easy":
        targetRange = 10
        validDifficulty = True
    elif difficulty.lower() == "medium":
        targetRange = 100
        validDifficulty = True
    elif difficulty.lower() == "hard":
        targetRange = 1000
        validDifficulty = True

# Generate a random number
targetNumber = random.randint(1, 100)

# While the user hasn't guessed the number:
guess = 0
while (guess != targetNumber):
    # Ask the user for a number
    guess = int(input("Enter your guess: "))

    # Print higher or lower depending on the guess
    if (guess < targetNumber):
        print("Higher!")
    elif (guess > targetNumber):
        print("Lower!")

# When they've guessed it, launch a rocket using a countdown
print("You guessed the number! Rocket Launching!")

for countdown in range(10):
    print(10 - countdown)
    time.sleep(1) # This makes the program pause for a second before printing the next value
    
print("Blastoff!")