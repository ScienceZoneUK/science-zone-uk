# Week 3 Advanced Challenge: Loops using Lists
# Instructions:
# 1. Add a list of different words to print at different points in the rocket launch
# 2. At each second, get the word it needs to print from the list, and print it
# 3. Have your difficulty and how many guesses it took affect the words in the list
# 4. Loop through each word at the end, after the launch, in a fun way.

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
guessCount = 0
while (guess != targetNumber):
    # Ask the user for a number
    guess = int(input("Enter your guess: "))

    guessCount += 1

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