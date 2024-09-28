# Week 3: Loops - Class Activity

# We import the "random" and "time" libraries here for use later. You will learn more about how this works in Week 7
import random
import time

# Print a message to greet the user
print("Welcome to the Higher or Lower Game!")

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