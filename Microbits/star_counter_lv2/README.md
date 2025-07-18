
# 🌟 Micro:bit Star Counter Adventure

**Duration:** 1hr 30 mins  
**Age:** 9-year-olds  
**Editor:** [Micro:bit Python Online Editor](https://python.microbit.org/v/3)  
**Browser:** Google Chrome

## 1️⃣ Why is Recording Data Important? (10 mins)

### 💬 Discussion Points:

**Ask students:**

- Why might we want to keep track of something?
  - Examples:
    - Steps counted daily
    - Recording goals in sports
    - Stars received for good behavior at school

**Highlight:**

- Recording data helps us:
  - Understand patterns
  - Improve ourselves
  - Solve problems
  - Invent new things!

**Introduce the Micro:bit:**

Explain that the Micro:bit is a tiny computer that can help us record data using:

- **Buttons:** Record events
- **Gestures:** Trigger actions
- **LED screen:** Show recorded data

---

## 2️⃣ Problem Introduction & Class Discussion (10 mins)

### 🌟 **Star Counter Problem:**

We need to invent a Micro:bit tool called the **Star Counter**.

**Requirements:**

- **Button A pressed →** Record/collect a star (add 1)
- **Button B pressed →** Shooting star Record/collect a shooting star (add 1)
- **Shake gesture →** Display animation and show number of stars and shooting stars

### 💬 **Discussion Prompt:**

Ask students:

- How can we solve this?
- How can the Micro:bit help us?
- What happens if we have no stars left?
- How will we clearly show the star count?

*(Encourage groups or pairs to briefly discuss and share their ideas.)*


---

## ✅ Step 1: Connect your Micro:bit

- Plug your Micro:bit into your computer using the USB cable.
- Open **Google Chrome** and go to: [python.microbit.org/v/3](https://python.microbit.org/v/3)
- At the top, click the ⚡ **Connect** button.
- Select your Micro:bit and click **Connect**.

---

## ✅ Step 2: Showing an Image

Make the Micro:bit show a happy face:

```python
from microbit import *

display.show(Image.HAPPY)
```

**Flash** and check your Micro:bit.

---

## ✅ Step 3: Button Pressing

Show the happy face **only** when button A is pressed:

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        sleep(1000)
        display.clear()
```

Then try Button B with another image:

```python
from microbit import *

while True:
    if button_b.was_pressed():
        display.show(Image.ARROW_N)
        sleep(1000)
        display.clear()
```

---

## ✅ Step 4: Counting with Variables

Count button presses using a **variable**:

```python
from microbit import *

stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(str(stars))
        sleep(500)
        display.clear()
```

Do the same with Button B:

```python
from microbit import *

shooting_stars = 0

while True:
    if button_b.was_pressed():
        shooting_stars = shooting_stars + 1
        display.show(str(shooting_stars))
        sleep(500)
        display.clear()
```

---

## ✅ Step 5: Using Shake

Detect shake gesture:

```python
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.GHOST)
        sleep(500)
        display.clear()
```

---

## ✅ Step 6: Animations and Scrolling Text

Shake animation with scrolling text:

```python
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        for i in range(3):
            display.show(Image.STAR)
            sleep(300)
            display.clear()
            sleep(200)
        display.scroll("Hello!")
```

---

## ✅ Step 7: Final Star Counter Program (Step-by-Step)

### ⭐ Step 7.1: Starting template

Begin with your basic program loop structure:

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    pass  # this means "do nothing yet"
```

Flash and test: *(Your Micro:bit won't show anything yet.)*

---

### ⭐ Step 7.2: Add counting Stars with Button A

Now add code to count stars each time **Button A** is pressed:

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()
```

Flash and test: *(Press Button A multiple times. Does the happy face appear?)*

---

### ⭐ Step 7.3: Add Shooting Stars with Button B

Next, let's count shooting stars each time **Button B** is pressed. Add this below your Button A code:

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()

    if button_b.was_pressed():
        shooting_stars = shooting_stars + 1
        display.show(Image.ARROW_N)
        sleep(300)
        display.clear()
```

Flash and test: *(Press Button B. Does the arrow appear? Try pressing both buttons and see the different images.)*

---

### ⭐ Step 7.4: Add Shake Gesture with Animation

Now let's make your Micro:bit detect a **shake** and show a simple animation. Add this part to your existing program:

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()

    if button_b.was_pressed():
        shooting_stars = shooting_stars + 1
        display.show(Image.ARROW_N)
        sleep(300)
        display.clear()

    if accelerometer.was_gesture('shake'):
        for i in range(2):
            display.show(Image.GHOST)
            sleep(300)
            display.clear()
            sleep(200)
```

Flash and test: *(Shake your Micro:bit. Did you see the ghost animation?)*

---

### ⭐ Step 7.5: Showing the Counts Clearly

Finally, after shaking, display the number of **stars** and **shooting stars**. Add this below your animation:

**Your complete final program is now:**

```python
from microbit import *

stars = 0
shooting_stars = 0

while True:
    if button_a.was_pressed():
        stars = stars + 1
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()

    if button_b.was_pressed():
        shooting_stars = shooting_stars + 1
        display.show(Image.ARROW_N)
        sleep(300)
        display.clear()

    if accelerometer.was_gesture('shake'):
        for i in range(2):
            display.show(Image.GHOST)
            sleep(300)
            display.clear()
            sleep(200)

        display.scroll("Stars:")
        display.scroll(str(stars))

        display.scroll("Shooting Stars:")
        display.scroll(str(shooting_stars))
```

Flash and test:  
- Press Button A and Button B several times.
- Shake your Micro:bit.
- You should clearly see your totals displayed.

---

## 🎉 Well done! You've carefully built your complete Star Counter step-by-step! 🌟


---

## ✅ Step 8: Investigate & Modify

- Predict and Investigate pressing buttons quickly.
- Modify images or animations.

---

## ✅ Step 9: Optional Challenge (Reset function)

Reset counters with buttons A+B         
Ask yourself where you might put this code:

```python
#hint: put me after the button presses
if button_a.is_pressed() and button_b.is_pressed():
    stars = 0
    shooting_stars = 0
    display.show(Image.YES)
    sleep(500)
    display.clear()
```

Double check indentation after pasting in code       

---

## ✅ Step 10: Reflection

- Did your program work well?
- Which part was easiest/hardest?
- What did you learn about variables, buttons, shake, and animations?

---

🎉 **CONGRATULATIONS! You've built your own Micro:bit Star Counter! 🌟🌠**
