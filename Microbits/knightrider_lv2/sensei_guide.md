
# 👩‍🏫 Teacher Guide: Running the Knight Rider Micro:bit Workshop

This guide supports the delivery of the Micro:bit Knight Rider workshop. It includes setup tips, student guidance, answers, and API references.

---

## 🛠️ Setup & Tools

### ✅ Recommended Editor
Use **Google Chrome** and go to:  
🔗 [https://python.microbit.org/v/3](https://python.microbit.org/v/3)

- Click **Connect** and choose the Micro:bit
- Write your code → Click **Flash** to upload
- Works without installing anything

### ✅ Alternative Editor (Installed)
- **Mu Editor** is pre-installed on PCs
- Plug in the Micro:bit (should auto-detect)
- Click **Flash** to upload
- REPL can be used for live testing

---

## 💡 Teaching Prompts by Stage

For all activities, it would be best for you to model how to use the microbit while walking through the steps.      
Show learners how you test and debug code, use print() often to demonstrate how to check variables and loops are working etc.            

### 🌟 Warm-up (display.scroll)
- ✅ Confirm Micro:bit setup is working
- Ask: "What message will scroll? Can you change it to your name?"

---

### 🧱 Stage 1: Light a Single Pixel
- Ask: “What do x and y do?”
- Try different coordinates and brightness levels

---

### 🔁 Stage 2: Move a Pixel
- Ask: “What happens if we remove `sleep()`?”
- Extend: “Can you move the pixel on row 0 instead of 2?”

---

### 🧱 Stage 3: Light a Full Column
- Try different `x` values
- Challenge: light 2 or more columns at once

---

### 🔁 Stage 4: Sweep Columns
- Emphasise nested loops (x then y)
- Ask: “Why do we use `range(4, -1, -1)` to go backwards?”
- Extend: only sweep one direction

---

### 🌟 Stage 5: Fading Trail
- Explain brightness levels (9, 7, 2)
- Ask: “What happens if you add a 4th column trail?”
- Change brightness values to control trail effect

---

## 🧾 Micro:bit MicroPython Cheat Sheet

Microbit api docs here [CLICK](https://microbit-micropython.readthedocs.io/en/v2-docs/)

### ✅ ALWAYS use the microbit library
```python
from microbit import *          # Setup the microbit api

```

### ✅ Display
```python
display.scroll("Hello!")            # Scroll text
display.set_pixel(x, y, brightness) # Light pixel at (x, y)
display.clear()                     # Clear screen
```

### ✅ Loops & Timing
```python
for i in range(5):    # Loop from 0 to 4
while True:           # Infinite loop
sleep(100)            # Wait 100ms
```

### ✅ Buttons
```python
button_a.is_pressed()   # True if pressed now
button_b.was_pressed()  # True if pressed since last check
```

### ✅ Sensors
```python
accelerometer.get_x()   # Tilt value
microphone.sound_level() # Sound intensity (if available)
```

### ✅ Pins
```python
pin0.write_digital(1)   # Output ON
```

---

## 🛠️ Troubleshooting

| Problem                  | Fix                                      |
|--------------------------|------------------------------------------|
| Flash button disabled    | Close REPL tab or Mu REPL terminal       |
| Flashing fails (online)  | Unplug/replug Micro:bit, use Chrome only |
| Mu won’t detect Micro:bit| Restart Mu or check USB port             |
| Code runs too fast       | Add `sleep(100)` to slow it down         |

---

## 🏁 Extension Ideas

| Idea                      | Concepts Involved            |
|---------------------------|------------------------------|
| Add more trail columns    | `if`, brightness, loops      |
| Change direction on button| `button_a.is_pressed()`      |
| Accelerometer control     | `accelerometer.get_x()`      |
| Flash with sound          | `microphone.sound_level()`   |
