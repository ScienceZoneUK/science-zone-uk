**Micro:bit** Virtual Pet Workshop (1hr 15min Follow-Along Guide)**

Welcome to the Micro\:bit Virtual Pet Workshop! Today we'll build a virtual pet that reacts to your touch and movement, gets sad if you ignore it, and even makes sounds! You'll explore MicroPython code, learn how computers make decisions, and build a mini-program that feels almost alive.

This guide is split into two parts:

1. **Code Explorations** – where you’ll try small bits of code and learn key concepts.
2. **Virtual Pet Project** – where you’ll bring it all together into a fun and interactive final project.

Please read each section carefully. The pseudocode tells you what the code should do. Your job is to turn that into working Python on your Micro\:bit. Let’s get coding!

---
Open MU editor or download it [here](https://codewith.mu/)



## 📂 Part 1: Code Explorations

Each short program below teaches you something new. Try them one at a time. Read the pseudocode first, then type in the real code!

---

### 🌟 1. Scroll a Message

**Concept:** This is your very first Micro\:bit program! You're using a built-in function called `display.scroll()` to scroll text across the LED screen. It's a great way to check if your Micro\:bit is working and to try your first bit of Python.     
**Pseudocode:**

```
Import the microbit tools
Scroll the message "Hello!" across the screen
```

Copy into the editor and flash your microbit.    

Troubleshooting if flash fails:       
- Close the repl to enable flash button
- If flash hangs up, disconnect/reconnect cable and flash again
- Press reset button on back of microbit resets the code

```python
from microbit import *

display.scroll("Hello!")
```

---

### 🔹 2. Try the REPL

**Concept:** REPL stands for Read-Eval-Print Loop. It lets you type Python code one line at a time and see what happens instantly. It’s great for testing code without flashing your Micro\:bit every time. **Pseudocode:**

```
Import the microbit tools
Show a cow image on the screen using REPL
```
Open repl by pressing button.    
Type this into the repl and press enter.     
```python
from microbit import *
display.show(Image.COW)
```

*Use the REPL in Mu to test this live. Press up arrow to repeat previous commands.*

---

### 🔹 3. Blink a Pixel (No Loop)

**Concept:** This shows how to turn a single pixel on and off. It introduces the idea of using coordinates `(x, y)` and brightness values on the LED grid. `sleep()` pauses the program temporarily. **Pseudocode:**

```
Import the microbit tools
Turn on the center pixel
Wait half a second
Turn it off
Wait again
```

```python
from microbit import *

display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(2, 2, 0)
sleep(500)
```

---

### 🔹 4. Blink a Pixel (Loop)

**Concept:** We add a `while True:` loop to make the pixel blink forever. This shows how to repeat actions and introduces the idea of infinite loops in programming. **Pseudocode:**
Copy and modify above code -Hint: While loop
```
Import the microbit tools
Repeat forever:
    Turn on the pixel
    Wait
    Turn off the pixel
    Wait
```

---

### 🔹 5. Show Two Faces

**Concept:** You're using Micro\:bit's built-in images to switch between two emotions. This helps you understand how to show and change what's on the LED screen. **Pseudocode:**

```
Import the microbit tools
Show happy face
Wait
Show sad face
```

```python
from microbit import *

display.show(Image.HAPPY)
sleep(500)
display.show(Image.SAD)
```

---

### 🔹 6. Show Faces in a Loop

**Concept:** Just like the pixel blink, we now loop between two different images. This creates a simple animation and reinforces how to use loops. **Pseudocode:**

```
Import the microbit tools
Repeat forever:
    Show happy
    Wait
    Show sad
    Wait
```


---

### 🔹 7. Touch the Logo

**Concept:** This introduces `if` and `else` statements. The Micro\:bit checks if the logo is being touched and shows a happy face if true, or clears the screen otherwise. You're learning about conditionals! **Pseudocode:**

```
Import the microbit tools
Repeat forever:
    If logo is touched:
        Show happy
    Else:
        Clear screen
```

```python
from microbit import *

while True:
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
    else:
        display.clear()
```

---

### 🔹 8. Shake to Show Emotion

**Concept:** Using the accelerometer sensor, your Micro\:bit can detect shaking! This program introduces input from the real world (movement) and how to respond to it. **Pseudocode:**

```
Import the microbit tools
Repeat forever:
    If shaken:
        Show surprised face
        Wait
    Else:
        Clear
```

```python
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.SURPRISED)
        sleep(1000)
    else:
        display.clear()
```

---

### 🔹 9. Timer

**Concept:** Now you're creating a variable that increases over time. This is your first example of tracking something with a counter. You’ll use this in your pet to measure how long it's been ignored. **Pseudocode:**

```
Import the microbit tools
Start at 0
Repeat forever:
    Wait one second
    Add one to timer
    Print the value
```

```python
from microbit import *

timer = 0
while True:
    sleep(1000)
    timer += 1
    print(timer)
```

*Open the REPL to view output. Remember to close it before flashing new code.*

---

### 🔹 10. Shake to Play Sound

**Concept:** You're combining sensors and sound! When the Micro\:bit is shaken, it plays a sound using the built-in speaker. This builds up toward making your pet expressive. **Pseudocode:**

```
Import the microbit tools
Repeat forever:
    If shaken:
        Play a sound
```

```python
from microbit import *
import audio

while True:
    if accelerometer.was_gesture('shake'):
        audio.play(Sound.HAPPY)
```

---

## 🐾 Part 2: Build the Virtual Pet

Now that you've learned all the basic skills — movement, sensing, sounds, timers, loops, and conditions — it's time to build your **Virtual Pet**!

Your pet will be happy when you interact with it, sad if you ignore it, and eventually fall asleep or worse if left alone.

If you're confident at building your pet then just use the psuedocode as your starter.    
Else there is template code below if you're stuck.

---

### 📖 Full Pseudocode

**Concept:** Before building our virtual pet, we plan out what it should do step-by-step using plain English. This is called pseudocode. It helps you understand the logic before writing real Python code.

```
1. Import the microbit library
2. Set a timer to 0
3. Show a welcome face and sound
4. Repeat forever:
    If logo is touched:
        Reset timer
        Show happy
        Play happy sound
    Else if shaken:
        Reset timer
        Show surprised
        Play giggle sound
    Else:
        Wait
        Add time
    If timer is 20:
        Show sad + sound
    If timer is 30:
        Show asleep + sound
    If timer is 40:
        Show skull + sound
        Break loop
```

---

### 🔧 Scaffolded Template (Fill-in-the-Blanks)

**Concept:** This is your chance to build the full virtual pet! Use everything you’ve learned: loops, conditionals, sensors, timers, and sounds. The blanks give you room to make decisions and personalise your pet.

Try to complete this code using what you’ve learned in the explorations:

```python
from microbit import *
import audio

timer = 0

display.show(Image.______)  # Start face
audio.play(Sound.______)   # Start sound

while True:
    if pin_logo.is_touched():
        timer = 0
        display.show(Image.______)  # Happy face
        audio.play(Sound.______)    # Happy sound

    elif accelerometer.was_gesture('shake'):
        timer = 0
        display.show(Image.______)  # Surprise face
        audio.play(Sound.______)    # Giggle sound

    else:
        sleep(____)  # Wait
        timer += ____  # Add time

    if timer == 20:
        display.show(Image.______)  # Sad face
        audio.play(Sound.______)    # Sad sound

    elif timer == 30:
        display.show(Image.______)  # Asleep
        audio.play(Sound.______)    # Yawn sound

    elif timer == 40:
        display.show(Image.______)  # Skull
        audio.play(Sound.______)    # Mysterious sound
        break
```

Fantastic work exploring, coding, and thinking like a computer. You’ve just made your own interactive digital pet!

