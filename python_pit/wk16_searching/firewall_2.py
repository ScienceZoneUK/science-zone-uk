# CIA Firewall Version 2. PLEASE DO NOT HACK!!!!!!!!
import random
import time

def Bot(numberList, target):
    return 0 # Put your bot (which you wouldn't have unless you were HACKING OUR SYSTEM AGAIN) here

while True:
    print("Welcome to the CIA firewall Version 2. Please authorise using our authorisation system. Press enter to start.")
    input()
    
    numbers = [] # Generate the list of random sorted numbers
    for number in range(0,500,1):
        numbers.append(random.randint(1,20000))
    numbers.sort()
    
    for number in range(0,500,1):
        print(str(number + 1) + ". " + str(numbers[number]))
        
    # Choose a random number to be the one you need to find
    target = random.randint(0,500)
    print("Where is " + str(numbers[target]) + " in the list?")
    
    # Get the time that the guessing started
    startTime = time.time()
    
    # Guessing
    guess = Bot(numbers, target)
    if (guess == 0):
        # We're guessing manually
        guess = input()
        
    # Get the time that the guessing ended
    endTime = time.time()
    deltaTime = endTime - startTime # Calculate how much time has elapsed
    
    if (deltaTime > 10):
        print("You ran out of time. You're obviously not a real CIA agent. Try again.\n")
    elif (guess == str(target + 1)):
        print("Correct. To ensure you are a real CIA agent, you must authenticate again.\n")
    else:
        print("Wrong! Try again.\n")
