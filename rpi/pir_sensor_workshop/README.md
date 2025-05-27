
# 🛡️ Raspberry Pi Intruder Alarm Workshop (Learner Guide)

Welcome to your Raspberry Pi workshop! 🎉  
In this session, you'll build an intruder alarm system using code, electronics, and your imagination. Let's get started!

---

## 🧰 What You’ll Need

### Hardware:
- Raspberry Pi (with power, keyboard, mouse, and screen)
- Breadboard
- PIR motion sensor (HC-SR501)
- LED (any color)
- 330Ω resistor
- Jumper wires (male-to-male)

---
- wifi ssid: BTBHub6-JQ2W
- Password: d6QGFiGEGLxv

---

## 🕐 Part 1: Using the Terminal & Writing Python

### ✅ Step 1: Open the Terminal
Click the terminal icon in the top bar. It looks like a black square.

### ✅ Step 2: Check Your Internet Connection
Type this and press **Enter**:
```bash
ping google.com -c 2
```

### ✅ Step 3: Find Your IP Address
```bash
hostname -I
```

### ✅ Step 4: Update Your Pi
```bash
sudo apt update && sudo apt upgrade
```

### ✅ Step 5: Open Pi Configuration
```bash
sudo raspi-config
```
- Use the arrow keys and **Enter**
- Make sure **SSH** and **VNC** are **enabled**
- Press **Tab** and select **Finish**

### ✅ Step 6: Make a Folder for Your Work
```bash
mkdir intruder_alarm
cd intruder_alarm
```

### ✅ Step 7: Your First Python Program!
```bash
nano hello_world.py
```
Type this inside the file:
```python
print("Hello, intruder alert system!")
```
Then press:
- **Ctrl + X**
- **Y** to save
- **Enter** to confirm

Now run it!
```bash
python3 hello_world.py
```

---

## 💡 Part 2: Blink an LED

### ✅ Step 1: Build the LED Circuit

- Connect **GPIO 17** to the resistor
- Resistor to LED long leg (anode +)
- LED short leg (cathode -) to GND

### ✅ Step 2: Write the Code
```bash
nano blink.py
```
Add:
```python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Run it:
```bash
python3 blink.py
```
The LED should blink every second! 💡

---

## 🕵️‍♂️ Part 3: Detect Motion with a PIR Sensor

### ✅ Step 1: Build the PIR Sensor Circuit

- **VCC** → 5V (Pin 2)
- **GND** → GND (Pin 6)
- **OUT** → GPIO 4 (Pin 7)

### ✅ Step 2: Write the Motion Detector
```bash
nano pir.py
```
Add:
```python
from gpiozero import MotionSensor

pir = MotionSensor(4)

print("Waiting for motion...")

while True:
    pir.wait_for_motion()
    print("⚠️ Intruder Detected!")
    pir.wait_for_no_motion()
```

Run it:
```bash
python3 pir.py
```

Move your hand in front of the sensor. Watch the message!

---

## 💡 Part 4: PIR Sensor + LED Alert

Now let’s make the LED light up when motion is detected.

### ✅ Step 1: Create the Script
```bash
nano pir_led.py
```
Add:
```python
from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(4)
led = LED(17)

print("System Ready...")

while True:
    pir.wait_for_motion()
    print("⚠️ Motion Detected!")
    led.on()
    sleep(2)
    led.off()
    pir.wait_for_no_motion()
```

Run it:
```bash
python3 pir_led.py
```

---

## 🌐 Part 5: Show Alerts on a Webpage

We will now make a web page that updates when motion is detected.

### ✅ Step 1: Install Flask (only once)
```bash
pip3 install flask
```

### ✅ Step 2: Create the Web Server
```bash
nano pir_webserver.py
```
Add:
```python
from flask import Flask
from gpiozero import MotionSensor
import threading

pir = MotionSensor(4)
app = Flask(__name__)
status = {"motion": "All clear"}

@app.route('/')
def home():
    return f"""<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="refresh" content="5">
        <title>PIR Alert</title>
      </head>
      <body>
        <h1>Motion Status: {status['motion']}</h1>
      </body>
    </html>"""

def watch_motion():
    while True:
        pir.wait_for_motion()
        status['motion'] = "🚨 Motion Detected!"
        pir.wait_for_no_motion()
        status['motion'] = "✅ All Clear"

threading.Thread(target=watch_motion, daemon=True).start()
app.run(host='0.0.0.0')
```

Run it:
```bash
python3 pir_webserver.py
```

On another device in the same Wi-Fi, open:
```
http://<your-pi-ip>:5000
```

✅ You’ll see the motion status update every 5 seconds!

---

## 🧪 Optional: Use SSH (PuTTY)

From a Windows laptop:
1. Open **PuTTY**
2. Enter your Pi's IP address
3. Login with:
   ```
   pi
   raspberry
   ```

Now run your scripts remotely!

---

## ✅ Wrap-Up

🎉 You’ve now built:
- A blinking light
- A motion detector
- A visual alert
- A web-based intruder alarm!

Well done! 👏

---

## 📝 Bonus Ideas
- Add sound (buzzer)
- Take a photo when motion is detected
- Send an email or text message
