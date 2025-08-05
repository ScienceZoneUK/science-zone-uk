# IOT project - Sensing water levels

# 🐍 Raspberry Pi + Micro:bit Flood Monitor Workshop
**Duration:** 3 Hours  
**Age Group:** 13+  
**Tools Needed:**
- Raspberry Pi (headless)
- Micro:bit + USB cable
- Windows PC with PuTTY
- LED + resistor
- Water level sensor (analog)
- Breadboard + jumper wires
- WiFi connection

---

## 🕘 Part 1: Getting Connected (45 mins)

### 🔌 Setup Your Raspberry Pi

If you have your **own Pi** with a screen:
1. Power up.
2. Connect to WiFi.
3. Open Terminal and type:
    ```bash
    hostname -I
    ```
4. 📌 **Note down your IP address!**

---

### 🖥️ Headless Pi Access from a PC (via PuTTY)

#### 🔍 Identify Your Pi Using LEDs
We’ll use blinking LEDs to identify which Pi is yours.

#### 📌 Connect Your LED
Refer to this GPIO diagram:  
[GPIO Pinout](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png?hash=df7d7847c57a1ca6d5b2617695de6d46)

- Long leg (positive) → GPIO26 (pin 37)
- Short leg (negative) → GND (pin 39)
- Use a resistor if available (220Ω or 330Ω)

---

### 💻 Use PuTTY to Connect to Your Pi

1. Download PuTTY: [Microsoft Store](https://apps.microsoft.com/detail/putty/9PGJWD2V9V2H)
2. Open PuTTY
3. Enter your Raspberry Pi’s IP address
4. Use SSH login:
    ```
    Username: pi
    Password: raspberry (or ask facilitator)
    ```

---

## 🧪 Part 2: Terminal Commands and LED Blink (30 mins)

### 🧠 Learn Basic Linux Commands

Try these in your terminal:

| Command | Description |
|--------|-------------|
| `ls` | Lists files |
| `cd foldername` | Changes directory |
| `cd ..` | Goes up a directory |
| `mkdir my_folder` | Makes a new folder |
| `nano filename.py` | Opens file in editor |
| `clear` | Clears terminal screen |

---

### 💡 Blink Your LED

1. Create a folder:
    ```bash
    mkdir yourname_summer_rpi
    cd yourname_summer_rpi
    ```

2. Create a Python file:
    ```bash
    nano blink_led.py
    ```

3. Paste this code:
    ```python
    from gpiozero import LED
    from time import sleep

    led = LED(26)

    while True:
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.5)
        led.on()
        sleep(1)
        led.off()
        sleep(0.2)
    ```

4. Save and run:
    ```bash
    python3 blink_led.py
    ```

🎉 Your Pi is now blinking a unique pattern!

---

### 🔁 Update Your Raspberry Pi

Run this to install latest updates:

```bash
sudo apt update && sudo apt upgrade -y
```

## Create a webserver      

follow this tutorial       
[click here](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/1)


---

## 🧪 Part 3: Connect the Micro:bit for Water Level Reading (45 mins)

### 🔌 Flash Your Micro:bit

Paste this into the [Micro:bit Python Editor](https://python.microbit.org) and flash:

```python
from microbit import *

while True:
    water_level = pin0.read_analog()
    print(water_level)
    sleep(200)
```

---

### 🖥️ Read Serial Data on the Raspberry Pi

1. Plug Micro:bit into Raspberry Pi via USB
2. Find the serial port:
    ```bash
    ls /dev/ttyACM*
    ```

3. Create a file:
    ```bash
    nano microbit_reader.py
    ```

4. Paste this code:

    ```python
    import serial
    from time import sleep

    PORT = "/dev/ttyACM0"
    BAUD = 115200

    try:
        s = serial.Serial(PORT, BAUD, timeout=1)
        s.reset_input_buffer()
        print(f"Connected to {PORT} at {BAUD} baud.")
    except serial.SerialException:
        print("Could not open serial port. Is the Micro:bit connected?")
        exit()

    try:
        while True:
            try:
                line = s.readline().decode('utf-8').strip()
                if line:
                    value = int(line)
                    print(f"Water Level: {value}")
            except ValueError:
                print("Received non-integer data.")
            except UnicodeDecodeError:
                print("Received undecodable data.")
            sleep(0.1)

    except KeyboardInterrupt:
        print("\nExiting...")

    finally:
        s.close()
    ```

5. Run it:
    ```bash
    python3 microbit_reader.py
    ```

You’ll see water level readings!

---

## 🌐 Part 4: Create a Flask Web Dashboard (45 mins)

### 📁 Create Flask App

```bash
mkdir microbit_web
cd microbit_web
nano app.py
```

### 💻 Paste This Code

```python
from flask import Flask
import serial

PORT = "/dev/ttyACM0"
BAUD = 115200

app = Flask(__name__)

def read_water_level():
    try:
        with serial.Serial(PORT, BAUD, timeout=1) as s:
            s.reset_input_buffer()
            line = s.readline().decode('utf-8').strip()
            return int(line)
    except Exception as e:
        print("Error reading serial:", e)
        return -1

@app.route('/')
def index():
    value = read_water_level()
    if value == -1:
        status = "Sensor Error"
    elif value > 700:
        status = "⚠️ High Flood Risk"
    elif value > 400:
        status = "🌧️ Medium Risk"
    else:
        status = "✅ Low Risk"

    return f"<meta http-equiv='refresh' content='5'><h1>River Stour Monitor</h1><p>Water Level: {value}</p><p>Status: {status}</p>"

app.run(host='0.0.0.0', port=5000)
```

---

### ▶️ Run the Server

```bash
python3 app.py
```

Then visit from your PC:
```
http://<your_pi_ip>:5000
```

You should see your live flood risk monitor!

---

## 🏁 Extensions & Challenges

- Add a graph using Chart.js or matplotlib
- Log water levels to a CSV file
- Add LED or buzzer warning when level is high
- Style the page using HTML/CSS

---

## ✅ Summary

Today, you learned how to:
- SSH into your Raspberry Pi using PuTTY
- Blink an LED with a custom sequence
- Connect a Micro:bit as a sensor device
- Read serial data and analyze water level
- Display real-time data on a live web server

🚀 Great job!


#### Get micro:bit port
unplug microbit and run:
```ls /dev/tty*```

plug microbit and rerun

Read serial from micro:bit
```python
import serial
from time import sleep

# Update this if your port is different
PORT = "/dev/ttyACM0" #!!!!CHANGE THIS!!!!
BAUD = 115200

try:
    s = serial.Serial(PORT, BAUD, timeout=1)
    s.reset_input_buffer()
    print(f"Connected to {PORT} at {BAUD} baud.")
except serial.SerialException:
    print("Could not open serial port. Is the Micro:bit connected?")
    exit()

try:
    while True:
        try:
            line = s.readline().decode('utf-8').strip()
            if line:
                value = int(line)
                print(f"Water Level: {value}")
        except ValueError:
            print("Received non-integer data.")
        except UnicodeDecodeError:
            print("Received undecodable data.")

        sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    s.close()

```
Microbit code
```python
from microbit import *

while True:
    water_level = pin0.read_analog()
    print(water_level)
    sleep(200)

```

## Webserver - water level


# 💧 Micro:bit Water Level Web App – Step-by-Step Guide for Beginners (Age 13+)

This guide helps you build a simple web app that displays **live water level data** from a Micro:bit on a webpage. You'll start with a **static page**, then use **Flask** to make it dynamic, and finally make it **update live** using JavaScript.

---

## 🧱 Project Structure

```
microbit_flask/
├── app.py         ← Your Flask Python code
└── templates/
    └── index.html ← Your webpage
```

---

## ✅ VERSION 1 — Static Placeholder Page (HTML Only)

### 🔍 What is this?
A basic HTML page that just shows a fake number (like “500”). No Python needed.

### 📄 `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Water Level</title>
</head>
<body>
    <h1>🌊 Water Level Monitor</h1>
    <p><strong>500</strong></p> <!-- Hard-coded value -->
</body>
</html>
```

### 🧠 What You Learn
- What HTML is
- How to use headings (`<h1>`) and paragraphs (`<p>`)
- How to structure a web page

Open this file in your browser to see the result.

---

## ✅ VERSION 2 — Flask + Static Value (Updates Only on Refresh)

### 🔍 What is this?
We use **Flask (Python)** to read a real water level from the Micro:bit and display it, but only when the page is refreshed.

### 📄 `app.py`

```python
from flask import Flask, render_template
import serial

app = Flask(__name__)

# Connect to Micro:bit (check your port!)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.reset_input_buffer()

@app.route('/')
def index():
    try:
        line = ser.readline().decode('utf-8').strip()
        value = int(line)
    except:
        value = "No data"
    return render_template('index.html', value=value)

if __name__ == '__main__':
    app.run(debug=True)
```

### 📄 `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Water Level</title>
</head>
<body>
    <h1>🌊 Water Level Monitor</h1>
    <p><strong>{{ value }}</strong></p>
    <p>Refresh the page to update.</p>
</body>
</html>
```

### 🧠 What You Learn
- How Flask connects Python and HTML
- How `{{ value }}` displays Python data in HTML
- How to read real-time data from a Micro:bit
- The value updates only when you reload the page

To run:
```bash
python3 app.py
```
Then go to [http://localhost:5000](http://localhost:5000)

---

## ✅ VERSION 3 — Flask + Live JavaScript Updates

### 🔍 What is this?
We add a `/data` API route and JavaScript to get **new sensor values every second**, updating the page without a reload.

### 📄 `app.py`

```python
from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

# Serial setup
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.reset_input_buffer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    try:
        line = ser.readline().decode('utf-8').strip()
        value = int(line)
    except:
        value = None
    return jsonify({'water_level': value})

if __name__ == '__main__':
    app.run(debug=True)
```

### 📄 `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Live Water Level</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding-top: 50px; }
        #level { font-size: 3em; color: navy; }
    </style>
</head>
<body>
    <h1>🌊 Water Level Monitor</h1>
    <div id="level">Loading...</div>

    <script>
        async function updateLevel() {
            try {
                const response = await fetch('/data');
                const json = await response.json();
                document.getElementById('level').textContent = json.water_level ?? 'No data';
            } catch {
                document.getElementById('level').textContent = 'Error';
            }
        }

        setInterval(updateLevel, 1000); // Every second
        updateLevel(); // Start immediately
    </script>
</body>
</html>
```

### 🧠 What You Learn
- Flask routes can send data using `/data`
- JavaScript fetches that data every second
- The page updates live — no reload needed!

---

## 🧪 Test `/data` Directly

Go to:
```
http://localhost:5000/data
```

You’ll see:
```json
{"water_level": 512}
```

This shows the browser is getting the live data.

---

## 🏁 Final Tips

- Check your Micro:bit port using `ls /dev/ttyACM*`
- You can run this app on a Raspberry Pi and access it from other devices on your network
- Want to add a graph or alerts? Try Chart.js or Bootstrap next!

Let your imagination flow — just like water! 🌊💡

