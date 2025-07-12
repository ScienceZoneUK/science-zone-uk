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

```python
from microbit import *

border = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")

display.show(border)


```

## Method 2 
### Control individual pixels

```
from microbit import *


display.set_pixel(0, 0, 9)

```



```python
from microbit import *

pixel_numbers = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5]
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
wash_type = "None"
display.scroll("Choose Wash")

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

### 3. 🟢 Start the Wash
Now we wait for the user to touch the Micro:bit’s logo to begin the wash.

```python
while not pin_logo.is_touched():
    display.show(Image.ARROW_W)
    sleep(100)

# Simulate driving in
display.show(Image.ARROW_E)
sleep(500)
```

### 4. ♻️ Run Animation
We now activate our LED border loop as the washing motion.

```python
counter = 0
for i in range(32):
    counter = loop_animation(counter)
```

### 5. ⏱ Countdown Timer
Let’s count down while the wash is happening!

```python
for i in range(9, -1, -1):
    display.show(str(i))
    sleep(500)
```

### 6. 🚿 Rinse!
Flash all the pixels to simulate a powerful rinse.

```python
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

