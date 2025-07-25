# 🌡️ Micro:bit Temperature Warning System

**Duration:** 1hr 30 mins  
**Age:** 9-year-olds  
**Editor:** [Micro:bit Python Online Editor](https://python.microbit.org/v/3)  
**Browser:** Google Chrome

---

## 1️⃣ Why is Temperature Important? (10 mins)

### 💬 Discussion Points:

**Ask students:**

- Why do we need to know the temperature?
  - Examples:
    - To know if it's safe to go outside
    - To keep pets or babies comfortable
    - To protect plants and food

**Highlight:**

- Monitoring temperature helps us:
  - Stay safe and healthy
  - Protect animals and objects
  - Make smart decisions (like turning on a fan or heater)

**Introduce the Micro:bit:**

The Micro:bit has a built-in **temperature sensor** and **LED screen**.  
We’ll use these to build a **Temperature Warning System** that keeps us safe!

---

## 2️⃣ Problem Introduction & Class Discussion (10 mins)

### 🧊🔥 **The Challenge:**

Let’s create a **Temperature Warning System** that:

- Shows a 😊 smiley if it's not too hot
- Shows a 😠 warning if it's hot (25°C or more)
- Scrolls the temperature when Button A is pressed
- Flashes a ⚠️ warning if it's hot and the Micro:bit is shaken

### 💬 Discussion Prompt:

Ask students:

- What temperatures feel hot or cold to you?
- What images could show “hot” or “cold”?
- How would YOU warn someone that it's too hot?

---

## ✅ Step 1: Connect your Micro:bit

- Plug the Micro:bit into your computer with the USB cable.
- Go to: [https://python.microbit.org/v/3](https://python.microbit.org/v/3)
- Click the ⚡ **Connect** button.
- Choose your Micro:bit and click **Connect**.

---

## ✅ Step 2: Show a Happy Face 😊

Let’s start simple—show a smiley to test your Micro:bit:

```python
from microbit import *

display.show(Image.HAPPY)
```

If you want to change your image look here for a [**list of images**](https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/images.html#)    

**Flash and test:**  
You should see a smiley face appear on your Micro:bit screen.

---

## ✅ Step 3: Scroll Temperature on Button A

We can use Button A to scroll the current temperature:

```python
from microbit import *

while True:
    if button_a.was_pressed():
        temp = temperature()
        display.scroll(str(temp) + "C")
```

**Flash and test:**  
Press **Button A**—you should see a number like `22C` scroll across the screen!

---

## 🧠 PAUSE: What is `while True:` and `if`?

Before we go further, let’s explain this strange code!

### 🔁 `while True:` — What does it do?

It means: **“Keep checking forever!”**  
Your Micro:bit becomes a robot that **never stops checking** for button presses, movement, or temperature.

> Like asking: “Now? Now? Now?” 20 times a second!

### ❓ `if` means “check something”

```python
if button_a.was_pressed():
```

This means: “If Button A was pressed, then do the stuff underneath.”

### ➕ What is `elif`?

It means: **“otherwise, if…”**

```python
if temp >= 25:
    # do this
elif temp < 10:
    # do something else
else:
    # do a default thing
```

🧱 Python checks in order:
1. Is it hot? (temp >= 25)
2. Else, is it cold? (temp < 10)
3. Else → it's just right

---

## ✅ Step 4: Show Warning if Too Hot 🔥

Now let’s show a warning if it’s hot (25°C or more):

```python
from microbit import *

while True:
    temp = temperature()
    if temp >= 25:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
    sleep(1000)
```

**Flash and test:**  
Warm the Micro:bit in your hands—does the face change from 😊 to 😠?

---

## ✅ Step 5: Add a Shake Alert ⚠️

Let’s make the Micro:bit flash a warning if you **shake it when it’s hot**:

```python
from microbit import *

while True:
    temp = temperature()

    if accelerometer.was_gesture('shake') and temp >= 25:
        for i in range(3):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep(200)
    elif temp >= 25:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)

    sleep(500)
```

**Flash and test:**

- Warm the Micro:bit first.
- Shake it—does it flash sad faces?
- If not warm, it should only show the normal smiley.

---

## ✅ Step 6: Combine Everything

Let’s add the **button** and **shake gesture** into one final program!

```python
from microbit import *

while True:
    temp = temperature()

    if button_a.was_pressed():
        display.scroll(str(temp) + "C")

    if accelerometer.was_gesture('shake') and temp >= 25:
        for i in range(3):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep(200)

    elif temp >= 25:
        display.show(Image.ANGRY)

    elif temp < 10:
        display.show(Image.TARGET)

    else:
        display.show(Image.HAPPY)

    sleep(500)
```

**Flash and test:**

- Try all actions: press Button A, shake it, warm it up, cool it down (put near fan or fridge).
- Watch the faces and messages change!

---

## ✅ Step 7: Investigate & Modify

🔎 Try changing:

- The hot temperature limit (e.g., 30°C instead of 25)
- What happens when it’s cold
- The image that scrolls

💡 Add your own ideas!

---

## ✅ Step 8: Optional Challenge – Reset Button

Let’s use **Button B** to reset everything:

```python
if button_b.was_pressed():
    display.scroll("Reset")
```

📍 Where would you place this in the code?

---

## ✅ Step 9: Reflection

### 🗣️ Discuss as a class:

- What was easy? What was tricky?
- What do `if`, `elif`, and `else` do?
- How could we make a version that:
  - Sends a sound?
  - Uses a speaker?
  - Warns about cold temperatures too?

---

🎉 **CONGRATULATIONS! You built a smart Micro:bit Temperature Warning System! 🌡️🎉**
