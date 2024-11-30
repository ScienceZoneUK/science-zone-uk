
# Step-by-Step: Iterating Through a List of Colors on Sense HAT

This guide will show you how to cycle through a list of colors and display them on the Sense HAT's 8x8 LED matrix.

---

## Step 1: Install Sense HAT Library

Make sure you have the Sense HAT library installed. If not, install it using:

```bash
sudo apt-get install sense-hat
```

---

## Step 2: Import the Sense HAT Library

Start your Python script by importing the Sense HAT library:

```python
from sense_hat import SenseHat
```

---

## Step 3: Define Your List of Colors

Create a list of RGB values representing the colors you want to display:

```python
colors = [
    [255, 0, 0],    # Red
    [0, 255, 0],    # Green
    [0, 0, 255],    # Blue
    [255, 255, 0],  # Yellow
    [255, 255, 255] # White
]
```

---

## Step 4: Initialize the Sense HAT

Create an instance of the Sense HAT class:

```python
sense = SenseHat()
```

---

## Step 5: Iterate Through the List of Colors

Use a loop to iterate through the list of colors and set the entire LED matrix to each color:

```python
for color in colors:
    sense.clear(color)  # Set the entire LED matrix to the current color
    sense.sleep(1)      # Pause for 1 second before moving to the next color
```

---

## Step 6: Add a Reset at the End (Optional)

To turn off the LED matrix after the loop ends, add this line:

```python
sense.clear()
```

---

## Full Code Example

Here's the complete code for iterating through a list of colors:

```python
from sense_hat import SenseHat

# Define a list of colors
colors = [
    [255, 0, 0],    # Red
    [0, 255, 0],    # Green
    [0, 0, 255],    # Blue
    [255, 255, 0],  # Yellow
    [255, 255, 255] # White
]

# Initialize Sense HAT
sense = SenseHat()

# Iterate through the colors and display them
for color in colors:
    sense.clear(color)  # Set the entire matrix to the current color
    sense.sleep(1)      # Pause for 1 second

# Turn off the LED matrix
sense.clear()
```

---

## Step 7: Run the Script

1. Save the script as `color_cycle.py`.
2. Run it on your Raspberry Pi with:

```bash
python3 color_cycle.py
```

---

## Step 8: Experiment

- Add more colors to the `colors` list to expand the cycle.
- Adjust the pause duration by modifying the `sense.sleep()` value.
- Experiment with setting individual pixels instead of the whole matrix!

Enjoy creating colorful displays with your Sense HAT!
