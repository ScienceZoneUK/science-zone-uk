
# Sense HAT Color Selector

This project is designed to help kids learn coding concepts step-by-step while creating a fun and interactive program for the Sense HAT on a Raspberry Pi. By the end of this guide, students will have a program where users can select a color from the console and display it on the LED matrix.

---

## **What You’ll Learn**
- **Basic Python Concepts**: How to use variables, functions, loops, and conditionals.
- **Interacting with Hardware**: How to control the Sense HAT’s LED matrix.
- **User Input**: Letting the user choose options and responding to their choices.

---

## **How to Use**
1. Follow the steps below to build the program incrementally.
2. Copy and paste the code snippets into your Raspberry Pi’s Python editor (e.g., Thonny).
3. Test each step to see how it works before moving to the next.

---

## **Step-by-Step Guide**

### **Step 1: Set Up the Sense HAT**
The Sense HAT is an add-on board for the Raspberry Pi with an 8x8 LED matrix, sensors, and a joystick.

Start by writing the following code to set up the Sense HAT in Python:

**Code:**
```python
from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()
```

**What’s Happening?**
- `from sense_hat import SenseHat`: This imports the Sense HAT library, which allows us to control the hardware.
- `sense = SenseHat()`: This creates a `sense` object, which we’ll use to interact with the Sense HAT.

**Test It:**
Run the code. If there are no errors, the Sense HAT is ready to use!

---

### **Step 2: Turn Off the LED Matrix**
Before displaying anything, let’s make sure the LED matrix is clear.

**Code:**
```python
# Turn off the LED matrix
sense.clear()
```

**What’s Happening?**
- `sense.clear()`: This turns off all the LEDs on the Sense HAT.

**Test It:**
Run the code. The LED matrix should go blank.

---

### **Step 3: Display a Color**
Let’s display a solid color on the LED matrix. We’ll start with red.

**Code:**
```python
# Display a solid red color
sense.clear((255, 0, 0))
```

**What’s Happening?**
- `sense.clear((255, 0, 0))`: This lights up the LED matrix with the color red. The numbers `(255, 0, 0)` represent the RGB (Red, Green, Blue) color values.

**Test It:**
Run the code. The LED matrix should turn red.

---

### **Step 4: Add a Dictionary of Colors**
A dictionary lets us store multiple colors in one place. This will make it easy to let users pick from several options.

**Code:**
```python
# Define RGB values for colors
color_options = {
    "1": (255, 0, 0),   # Red
    "2": (0, 255, 0),   # Green
    "3": (0, 0, 255),   # Blue
    "4": (255, 255, 0), # Yellow
    "5": (128, 0, 128), # Purple
    "6": (255, 255, 255) # White
}
```

**What’s Happening?**
- `color_options`: This is a dictionary where each key (e.g., `"1"`) represents a color, and the value (e.g., `(255, 0, 0)`) is the RGB color code.

---

### **Step 5: Ask the User to Pick a Color**
We’ll use `input()` to let the user pick a color.

**Code:**
```python
# Ask the user for a color
print("Choose a color:")
print("1. Red")
print("2. Green")
print("3. Blue")
print("4. Yellow")
print("5. Purple")
print("6. White")

choice = input("Enter the number of your choice: ")
```

**What’s Happening?**
- `input()`: This asks the user to type something into the console. Whatever they type is stored in the variable `choice`.

---

### **Step 6: Use Conditionals to Respond to the User**
Conditionals let the program decide what to do based on the user’s input.

**Code:**
```python
# Check the user's choice and display the corresponding color
if choice in color_options:
    selected_color = color_options[choice]
    sense.clear(selected_color)
    print(f"Displayed color: {selected_color}")
else:
    print("Invalid choice. Please try again.")
```

**What’s Happening?**
- `if choice in color_options`: This checks if the user’s input is one of the keys in the dictionary.
- `sense.clear(selected_color)`: Lights up the LED matrix with the chosen color.
- `else`: If the user enters something invalid, they get an error message.

---

### **Step 7: Add a Loop**
Let’s make the program run continuously so the user can pick multiple colors.

**Code:**
```python
while True:
    print("\nChoose a color to display:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Yellow")
    print("5. Purple")
    print("6. White")
    print("Type 'exit' to quit.")

    choice = input("Enter the number of your choice: ")
    
    if choice.lower() == "exit":
        sense.clear()  # Turn off the LED matrix
        print("Exiting the program.")
        break
    elif choice in color_options:
        selected_color = color_options[choice]
        sense.clear(selected_color)
        print(f"Displayed color: {selected_color}")
    else:
        print("Invalid choice. Please try again.")
```

**What’s Happening?**
- `while True`: This creates a loop that keeps running until the user types `"exit"`.
- `break`: This exits the loop and ends the program.
- `choice.lower() == "exit"`: Converts the user’s input to lowercase and checks if it’s `"exit"`.

---

## **Final Program**
Here’s the complete program:

```python
from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()

# Define RGB values for the colors
color_options = {
    "1": (255, 0, 0),   # Red
    "2": (0, 255, 0),   # Green
    "3": (0, 0, 255),   # Blue
    "4": (255, 255, 0), # Yellow
    "5": (128, 0, 128), # Purple
    "6": (255, 255, 255) # White
}

# Main loop to handle user input
while True:
    print("\nChoose a color to display:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Yellow")
    print("5. Purple")
    print("6. White")
    print("Type 'exit' to quit.")

    choice = input("Enter the number of your choice: ")
    
    if choice.lower() == "exit":
        sense.clear()  # Turn off the LED matrix
        print("Exiting the program.")
        break
    elif choice in color_options:
        selected_color = color_options[choice]
        sense.clear(selected_color)
        print(f"Displayed color: {selected_color}")
    else:
        print("Invalid choice. Please try again.")
```

---

## **What’s Next?**
- Add more colors to the `color_options` dictionary.
- Let the user define custom colors by typing in RGB values.
- Explore other Sense HAT features, like the joystick or sensors.

---

### **License**
Feel free to use, modify, and share this project for educational purposes! 😊

