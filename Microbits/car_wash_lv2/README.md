# Micro:bit Smart Car Wash System Workshop

## 🧠 Overview
In this 1.5-hour hands-on workshop, we will simulate building a smart embedded system for a modern car wash using a Micro:bit. Our system will:

- Let the user choose between 3 wash cycles: E-Car, Motorbike, Van
- Start the wash when the logo is touched
- Simulate driving into the wash with animation and sound
- Wash cycle with LED animations and a countdown
- Exit animation and system reset

This project introduces embedded systems thinking, inputs, outputs, animation, sound, and control flow using MicroPython.

---

## 🚘 Introduction (10 minutes)

### Ask:
- Who’s been through a car wash?
- What happens step by step?
  
### Example Real-World Car Wash Steps:
1. Choose your wash type (e.g. standard, deluxe)
2. Pay
3. Enter the car wash bay
4. Roll forward
5. Stop and wait
6. Wash sequence begins
7. Exit after the wash

---

## 🔁 Pseudocode Plan (10 minutes)

We’ll break down our car wash logic into simple steps. Here’s how the program will work in plain English:

```plaintext
START
Display wash type selection using buttons
If button A is pressed → E-Car
If button B is pressed → Motorbike
If both buttons are pressed → Van

Wait for logo press to start

PLAY forward arrow + beep sound (drive into car wash)

RUN animation around border to simulate washing

COUNTDOWN from 9 to 0 (washing time)

Show full grid (spray) + long beep (rinse)

Show arrow (exit)

Reset and allow another user to try
```

Now let’s build this step-by-step using MicroPython.

---

## 🧪 Step-by-Step Implementation

### 1. 💡 Setup Pixel Animation Function
We’ll animate the border of the Micro:bit’s LED screen to simulate the washing motion.

On the microbit we can use built-in IMAGES or draw our own low-fi icons and animate them quite easily.     
We have a couple of methoods to use the pixels.


## Method 1 
### Use an image container

- First read the code **DO NOT RUN**
- 0-9 is pixel brightness
- Each pixel row terminates with a ``` : ```     is contained between  ``` " " ```
- we can display a custom image with a built in function ``` display.show(your_image)  ```
- What will the code draw?

Here's the pixel grid illustrated:

![Micro:bit 5x5 Grid](mb_pixels.png)



```
    y →
  x ↓
     0   1   2   3   4
   +-------------------
0 | (0,0)(1,0)(2,0)(3,0)(4,0)
1 | (0,1)(1,1)(2,1)(3,1)(4,1)
2 | (0,2)(1,2)(2,2)(3,2)(4,2)
3 | (0,3)(1,3)(2,3)(3,3)(4,3)
4 | (0,4)(1,4)(2,4)(3,4)(4,4)


```

```python
from microbit import *

#create the custom image and save into a variable 
border = Image("99999:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

#use the built-in display function
display.show(border)


```

## Method 2 
### Control individual pixels

```
from microbit import *


display.set_pixel(0, 0, 9)

```

## Challenge
I want you to create a bright pixel border around the pixels
- First discuss how you might achieve this
- Use psuedocode to plan your **ATTACK**
- Write some code
- Is it possible to use both methods?      

Paste this code into the editor, flash microbit, discuss the code amoungst yourselves
```python
from microbit import *

#I want to animate the border to show it as a timer
#Ive created a list of the pixels I want to use for the border
#The pixels are ordered from start to finsh of the border, IMPORTANT
pixel_numbers = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5]


# This loop below goes through the list to create an x and y coord for every pixel, I will have 16 pairs of x anf y values
# Im using modulo(%) to return an x value and (//) to return a y value
# A list of 16 tuples (x and y) will be saved into variable xy_coords, this is where all 16 positons will be saved
xy_coords = [(n % 5, n// 5) for n in pixel_numbers]

#I want to animate one pixel so i need to count the 16 loops
#Set the counter to 0
counter = 0

#Use a loop to move the animation
while True:
    for index, (x,y) in enumerate(xy_coords):  #We can loop through pixel coords to get the x,y, pos and get its position in the list(index)
        if index != counter: # Ive decide that if the pixel index is not the same as the counter value then turn pixel on
            display.set_pixel(x, y, 9)
        else: # Otherwise turn it off, so one pixel will turn off
            display.set_pixel(x, y, 0)
            

    counter +=1 #Increase the counter by 1 every loop
    counter = counter % len(pixel_numbers) # Here is a trick to reset the counter once it reaches the same value as the number of items in the list(16 pixels)

    sleep(100) # slow down the animation

```


The code above demostrates how to animate one pixel using an algorithm.         


Ive now put that into a function to make it neat and reuseable. We now have          
a timer animation to use in our car wash.       
Below is a template for you to fill in with the correct functions and function calls.            
**READ THE COMMENTS**


```python

from microbit import *
import audio

# Border animation setup
pixel_numbers = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5]
xy_coords = [(n % 5, n // 5) for n in pixel_numbers]
counter = 0

# Wash type selection
wash_type = None

def loop_animation(_counter):
    display.clear()
    for index, (x, y) in enumerate(xy_coords):
        if index == _counter:
            display.set_pixel(x, y, 0)
        else:
            display.set_pixel(x, y, 9)
    _counter = (_counter + 1) % len(xy_coords)
    sleep(100)
    return _counter

#add countdown function

#add wait_for_start function

#add show_exit function

#while True:
    #scroll("A=Ecar B=Bike A+B=Van")

    # Wait for wash type selection
    # Add choose wash type 

    #scroll(wash_type)

    # Wait for logo to be touched to start
    #call wait_for_start()

    # Enter wash: arrow + sound
    display.show(Image.ARROW_E)
    audio.play(Sound.GIGGLE)
    sleep(1000)

    # Wash process: animation + countdown
    for i in range(30):  # enough frames for a 9–0 countdown
        counter = loop_animation(counter)

    #call countdown()

    # Stop: sound + all pixels on
    display.show(Image.HAPPY)
    audio.play(Sound.HAPPY)
    for x in range(5): #Turn all pixels on
        for y in range(5):
            display.set_pixel(x, y, 9)
    sleep(1000)

    # Exit arrow
    #call show_exit

    # Reset for next cycle
    wash_type = None
    counter = 0
    display.clear()



```

```python
from microbit import *

#I want to animate the border to show it as a timer
#Ive created a list of the pixels I want to use for the border
#The pixels are ordered from start to finsh of the border, IMPORTANT
pixel_numbers = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5]


#This loop below goes through the list to create an x and y coord for every pixel
# Im using modulo(%) to return an x value and (//) to return a y value
# A list of tuples (x and y) will be saved into variable xy_coords
xy_coords = [(n % 5, n // 5) for n in pixel_numbers]

def loop_animation(counter): 
    for index, (x, y) in enumerate(xy_coords):
        if index == counter:
            display.set_pixel(x, y, 0)
        else:
            display.set_pixel(x, y, 9)
    counter = (counter + 1) % len(xy_coords)
    sleep(100)
    return counter
```

### 2. 🧼 Choose Wash Type
Use buttons to let users pick what kind of vehicle they're washing.

```python

while wash_type == "None":
    if button_a.is_pressed() and button_b.is_pressed():
        wash_type = "Van"
    elif button_a.is_pressed():
        wash_type = "E-Car"
    elif button_b.is_pressed():
        wash_type = "Bike"
    sleep(200)

display.scroll(wash_type)
```

### 3. 🟢 wait_for_start 
Now we wait for the user to touch the Micro:bit’s logo to begin the wash.

```python
def wait_for_start():
    while not pin_logo.is_touched():
        display.show(Image.ARROW_N)
        sleep(100)
```

### 4. ♻️ loop_animation
We now activate our LED border loop as the washing motion.

```python
def loop_animation(_counter):
    display.clear()
    for index, (x, y) in enumerate(xy_coords):
        if index == _counter:
            display.set_pixel(x, y, 0)
        else:
            display.set_pixel(x, y, 9)
    _counter = (_counter + 1) % len(xy_coords)
    sleep(100)
    return _counter
```

### 5. ⏱ Countdown Timer
Let’s count down while the wash is happening!

```python
def countdown():
    for i in range(9, -1, -1):
        display.show(str(i))
        sleep(500)
```

### 6. 🚿 Rinse!
Flash all the pixels to simulate a powerful rinse.            
This code is already in the template.     

```python
    display.show(Image.HAPPY)
    audio.play(Sound.HAPPY)
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9)
    sleep(1000)
```

### 7. ⏩ Exit and Reset
Display a final arrow to guide the car out, then clear the screen.

```python
display.show(Image.ARROW_E)
sleep(1000)
display.clear()
```

### 8. 🔁 Loop it!
Wrap everything in a loop to restart the whole process for the next user.

```python
while True:
    # insert steps 1–7 here
```

---

## 🧠 Recap (10 minutes)
- What inputs and outputs did we use?
- How did we control the flow of the program?
- What makes this an embedded system?

---

## 💡 Optional Challenges (if time)
- Add sound with `audio.play(Sound.HELLO)` or buzzer
- Add delays or unique animations per wash type
- Track the number of washes completed

Let me know if you'd like a printable worksheet or slide deck for delivery.

