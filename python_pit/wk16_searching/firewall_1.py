# CIA Firewall. DO NOT HACK!!!
import random

possibleObjects = ["Apple", "Banana", "Cabbage", "Diamond", "Elephant", "Frost", "Gladiator", "Helicopter", "Igloo", "Joke", "Keyboard", "Limousine", "Magnet", "Nose", "Oatmeal", "Purse", "Quazar", "Rainbow", "Salt", "Turntable", "Umbrella", "Van", "Wig", "Xylophone", "Yacht", "Zip"]

def Bot(objectList, target):
    return 0 # Put your bot (which you wouldn't have unless you were HACKING OUR SYSTEM) here

while True:
    print("Welcome to the CIA firewall. Please authorise using our authorisation system. Press enter to start.")
    input()
    
    objects = possibleObjects.copy() # Create a new copy of the possible objects list
    random.shuffle(objects) # Shuffle the list
    objects = objects[:13] # Take the first half of the list
    for number in range(1,14,1): # Print the object list
        print(str(number) + ". " + objects[number - 1])
        
    # Choose a random object to be the one you need to find
    target = random.randint(0,12)
    print("Where is " + objects[target] + " in the list?")
    
    # Guessing
    guess = Bot(objects, target)
    if (guess == 0):
        # We're guessing manually
        guess = input()

    if (guess == str(target + 1)):
        print("Correct. To ensure you are a real CIA agent, you must authenticate again.\n")
    else:
        print("Wrong! Try again.\n")
