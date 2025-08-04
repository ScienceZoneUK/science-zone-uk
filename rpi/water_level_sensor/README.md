# IOT project - Sensing water levels



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

