
# 🥳 BBC Micro:bit Python Workshop  
### 👧👦 Ages: 9+ | Editor: Mu | Duration: 1 hour  
### Project: **Emoticon Switcher using Buttons & Radio!**

---

## 🎯 Learning Goals:
- Understand how to use buttons and loops
- Store data using a **dictionary**
- Use variables to control the display
- Send and receive messages using **radio**
- Bonus: Control the micro:bit with **tilt**

---

## 🧱 Step 1: Show Your First Image

```python
from microbit import *

display.show(Image.HEART)
```

### ❓ Think about it:
- What do you think this line does?
- What if you change `HEART` to `SAD` or `HAPPY`?

---

## 🗂 Step 2: Create a Dictionary of Emoticons
Create a new program and paste in this snippet:
```python
from microbit import *

images = {
    1: Image.HEART,
    2: Image.HEART_SMALL,
    3: Image.HAPPY,
    4: Image.SAD,
    5: Image.SURPRISED,
    6: Image.ANGRY,
    7: Image.ASLEEP,
    8: Image.BUTTERFLY,
    9: Image.DIAMOND,
    10: Image.CONFUSED,
    11: Image.COW,
    12: Image.PACMAN,
}
```

### 🧠 What is a dictionary?
A dictionary links **keys** (numbers) to **values** (images).  
You can use the number to choose the image!

---

## 🔢 Step 3: Pick the First Emoticon
Below the dict and this snippet:
```python
index_num = 1
```

### ❓ Try this:
- What will `images[1]` show?
- What happens if you change it to `3`?

---

## 🔁 Step 4: Loop + Buttons
Below ``` index_num = 1 ``` add this snippet:
```python
while True:
    if button_b.is_pressed():
        index_num += 1
    if button_a.is_pressed():
        index_num -= 1
```

### ❓ Think about it:
- What happens if you press B a lot?
- What if the number goes above 12?

---

## 🛑 Step 5: Keep the Number Safe
Below ``` if button_a.is_pressed(): ``` secction, add this snippet:
```python
    if index_num > 12:
        index_num = 1
    elif index_num < 1:
        index_num = 12
```

> This keeps `index_num` between 1 and 12.

---

## 👀 Step 6: Show the Chosen Emoticon
Finally below ```if elif``` add this snippet:
```python
    display.show(images[index_num])
    sleep(500)
```

### ❓ Try it:
- Change the index manually and see what shows up.

---

## 📡 Step 7: Turn on the Radio

```python
import radio
radio.config(channel=10)
radio.on()
```

Put this **above** your `while True` loop.

### ❓ Talk about it:
- What do you think the channel number does?
- Why might we want more than one channel?

---

## 📬 Step 8: Receive Messages

```python
    incoming = radio.receive()
    if incoming:
        display.show(Image.TARGET)
        sleep(500)
        display.show(images[int(incoming)])
        sleep(2000)
```

### ❓ Think about it:
- Why do we show a "target" first?
- What does `int(incoming)` do?

---

## 📤 Step 9: Send an Emoticon

```python
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(index_num))
        display.show("sending...")
```

### ❓ Discuss:
- Why do we use both buttons to send?
- What does `str(index_num)` do?

---

## ✅ Complete Working Code

```python
from microbit import *
import radio

images = {
    1: Image.HEART,
    2: Image.HEART_SMALL,
    3: Image.HAPPY,
    4: Image.SAD,
    5: Image.SURPRISED,
    6: Image.ANGRY,
    7: Image.ASLEEP,
    8: Image.BUTTERFLY,
    9: Image.DIAMOND,
    10: Image.CONFUSED,
    11: Image.COW,
    12: Image.PACMAN,
}

index_num = 1
radio.config(channel=10)
radio.on()

while True:
    incoming = radio.receive()

    if button_b.is_pressed():
        index_num += 1
    if button_a.is_pressed():
        index_num -= 1

    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(index_num))
        display.show("sending...")

    if incoming:
        display.show(Image.TARGET)
        sleep(500)
        display.show(images[int(incoming)])
        sleep(2000)

    if index_num > 12:
        index_num = 1
    elif index_num < 1:
        index_num = 12

    display.show(images[index_num])
    sleep(500)
```

---

## 🧠 BONUS CHALLENGE: Tilt to Switch Emoticons!

🎯 Can you control your emoticons using **tilt** instead of buttons?

### 💡 Hints:
- Use `accelerometer.get_x()` to get the **left/right tilt** value.
- If it's tilted **right**, the number will be **greater than 400**.
- If it's tilted **left**, the number will be **less than -400**.
- Use an `if` statement to change `index_num`.
- Add a short `sleep()` to stop it skipping too fast.

---

### Example hint (don't copy – try it yourself!):

```python
x_tilt = accelerometer.get_x()
# check if x_tilt is > 400 or < -400
# change index_num and add a sleep delay
```

---

👏 Well done! You just built a program that:
- Stores multiple images in a dictionary
- Loops to check buttons and radio
- Sends and receives messages
- Can even be upgraded with tilt control!
