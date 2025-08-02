
# 💧 Flood Alert Heroes: Code to the Rescue!
## Micro:bit Python Workshop Worksheet  
**Age**: 11+ — **Time**: 1.5 hours

📺 [Water Sensor Explained (YouTube)](https://www.youtube.com/watch?v=Drxf9VuTkPM)  
📚 [Sensor Tutorial (Last Minute Engineers)](https://lastminuteengineers.com/water-level-sensor-arduino-tutorial/)  
🐍 Python Editor: [https://python.microbit.org/v/3](https://python.microbit.org/v/3)  
🧠 MicroPython Help: [https://microbit-micropython.readthedocs.io/en/v2-docs/index.html](https://microbit-micropython.readthedocs.io/en/v2-docs/index.html)  

---

## 🌊 Mission:
Your village is near a river. The rainy season is coming. You’ve been asked to build a **flood warning system** using your Micro:bit and a **water sensor**. Are you ready to become a Flood Alert Hero?

---

## 1. WARM-UP CHALLENGES

### 🟢 Easy: Print "Hello World"
```python
# Print message to serial
print("Hello World")
```

### 🟡 Medium: Display "Hello" on the LED screen
```python
from microbit import *
display.scroll("Hello")
```

### 🔴 Hard: Countdown then display message
```python
from microbit import *

for i in range(5, 0, -1):
    display.show(str(i))
    sleep(1000)

display.scroll("Hello World")
```

---

## 2. UNDERSTANDING THE TECHNOLOGY

### 👁 What is a Sensor?
Sensors help machines "feel" things like water, light, or sound.

### 🧠 What is a Micro:bit?
A small computer that reads sensors (input), makes decisions, and shows or plays results (output).

### 🧮 INPUT ➔ THINK ➔ OUTPUT
- Sensor: "I'm wet!"
- Micro:bit: "Oh no, it might flood!"
- Output: Flash light or sound alarm

---

## 3. DIGITAL vs ANALOG

### ✉️ Quick Quiz: Circle the type of signal

| Thing           | Digital or Analog? |
|----------------|--------------------|
| Light Switch   | DIGITAL            |
| Volume Knob    | ANALOG             |
| Water Sensor   | ANALOG             |

---

## 4. HOW DOES THE WATER SENSOR WORK?

### 🧪 What It Does
- Water touches the sensor → electricity flows
- More water = more voltage

![Water Level Animation](https://lastminuteengineers.com/wp-content/uploads/arduino/v2/Water-Level-Sensor-Working.gif)

### 🔢 Analog Reading
- 0 volts = number 0
- 3.3 volts = number 1023
- The micro:bit turns **voltage** into a **number** using binary (10 bits)

---

## 5. SETUP & TESTING THE SENSOR

### 🔌 Wiring:
- **VCC** ➔ 3V  
- **GND** ➔ GND  
- **SIG** ➔ pin0     

![Sensor Schematic](water_level_sensor.png)


## 🚧 Project Problem & Requirements

You're building a **smart water monitor** for a plant pot, water tank, or river!  
It should:

- Measure how high the water is
- Print the analog value
- Show a happy face if full, sad face if low
- Let you think about **how to improve it in future**

---

## 🪜 Step-by-Step Activities

### 🔹 Step 1: Connect the Sensor

**Pseudocode:**
- Connect sensor SIG to pin0
- Connect GND and VCC
- Read analog value

```python
from microbit import *

# Read from water level sensor connected to pin0
val = pin0.read_analog()
print(val)
```

🧠 *Q: What range of values do you see when there's no water vs full water?*

---

### 🔹 Step 2: Show Different Faces

**Concept:** Use `if` to check value

**Basic Test:**
```python
from microbit import *

val = pin0.read_analog()

if val < 300:
    display.show(Image.SAD)
else:
    display.show(Image.HAPPY)
```

**Scaffolding Options:**

**Easy:**
```python
# Show happy/sad face depending on water level
level = pin0.read_analog()
if level > 500:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
```

**Experienced Pseudocode:**
- Read value
- If value > 500 → happy
- Else → sad

---

### 🔹 Step 3: Add Loop and Live Readings

```python
from microbit import *

while True:
    level = pin0.read_analog()
    print(level)
    if level > 500:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(500)
```

🧠 *Q: Why do we use a loop here?*

---

## ⚙️ CHALLENGE: Build Your Own Water Alarm

Can you:
- Add a **sound** using
 ```
# Play a sound
audio.play(Sound.HELLO)
sleep(2000)
 ``` 
 to make a sound?
[ Microbit sound effects here](https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html#built-in-sounds-v2)
- Make the alarm go off when water is **too low**?

---
## 6. BUILDING THE ALERT SYSTEM

### 🔍 Step 2: Use `if` statements to react

**Pseudocode**:  
- Read level  
- If low → show '-'  
- If medium → show arrow  
- If high → show warning

**Code:**
```python
from microbit import *

while True:
    level = pin0.read_analog()

    if level < 300:
        display.show("-")
    elif level < 600:
        display.show(Image.ARROW_N)
    else:
        display.show(Image.SKULL)

    sleep(1000)
```

**Q: What does each condition mean? What happens when the level changes?**

---

## 7. ADDING A Sound OR SCROLL MESSAGE (OPTIONAL)

**Challenge:**  
Can you add a buzzer or display a scrolling message if flooding is detected?

**Idea:**
```python
# Scroll message for high level
if level > 600:
    display.scroll("FLOOD ALERT")
```

---

## 8. CHALLENGES

- Add a **sound alert** using another pin
- Add a **scrolling message**
- Show a **countdown** when the flood level is reached
- Make it **flash** or play a game

---

## 9. REFLECTION & SHARING

- What did your system do well?
- How could it be improved?
- Where else could this sensor be used?
- Share and test a friend’s prototype!

---

## ✅ YOU DID IT!
You’ve created a real flood detector system using sensors and code. What would your next invention be?

---

## 🧠 Concepts Practiced

- `print()` and serial output  
- `display.show()` and `scroll()`  
- Analog input with `read_analog()`  
- `if`/`elif`/`else` logic  
- Loops with `while` and `for`  
- Pseudocode and testing  
