
# 🌐 Raspberry Pi Pico W: Web Server Lesson for 12-Year-Olds

Welcome to your first **web server** lesson using **CircuitPython** and the **Raspberry Pi Pico W**! This guide is designed for beginners aged 12+ and focuses on **Physical Computing** and **Web Concepts**.
![Alt text](./images/conceptmap.png)

---

## 🧠 Step 1: Whiteboard Concept Pool

Use a whiteboard or notebook to explore these topics before coding:

🌐 Web Server Concepts on the Pico W
1. Microcontroller

    A small computer on a chip.

    Runs simple programs and connects to sensors, lights, and Wi-Fi.

2. CircuitPython

    A version of Python made for microcontrollers.

    We write code like normal Python, and it runs directly on the Pico.

3. Wi-Fi Connection

    Pico W has built-in Wi-Fi.

    We can connect it to the internet using our home Wi-Fi.

    Needs a username (SSID) and password.

4. IP Address

    Like a house address, but for devices on Wi-Fi.

    Pico gets its own IP when it connects.

    We use this to talk to the Pico from a web browser.

5. Socket

    A digital walkie-talkie for sending and receiving data.

    We make a socket to listen for people trying to visit our Pico's page.

6. Port 80

    The default “door” for web traffic.

    When your browser loads a website, it talks to port 80 unless told otherwise.

7. HTTP Request

    When you type an address in a browser, it sends a "request" to that device.

    Example: "Hey, Pico! Show me your page!"

8. HTTP Response

    Pico replies: "Here’s my web page!"

    Sent as HTML text — what browsers turn into real pages.

9. HTML

    The language web pages are written in.

    Even Pico can send HTML as text for browsers to show.

10. Server Loop

    Our Pico keeps checking: “Is anyone there?”

    When someone visits, it sends the webpage and waits for the next visitor.

---

## 🛠️ Step 2: Setup

1. Install CircuitPython on your Pico W.
2. Open **Thonny** and select the Pico W as the interpreter.
3. Install the libraries:
   - `adafruit_requests`
   - `socketpool`

4. Create a `secrets.py` file with your Wi-Fi:

```python
# secrets.py
secrets = {
    'ssid': 'YOUR_WIFI_NAME',
    'password': 'YOUR_WIFI_PASSWORD'
}
```

---

## 🔎 Step 3: Test Wi-Fi Connection

Create a new `code.py` and run this:

```python
import wifi
from secrets import secrets

print("Connecting to Wi-Fi...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected!")
print("My IP address is", wifi.radio.ipv4_address)
```

👉 **Check Thonny's shell** for output!

---

## 🧪 Step 4: Test Socket Creation

```python
import wifi
import socketpool
from secrets import secrets

wifi.radio.connect(secrets["ssid"], secrets["password"])
print("IP:", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
print("SocketPool created!")
```

---

## 🕸️ Step 5: Build a Tiny Web Server
You will need to download [THIS](https://learn.adafruit.com/elements/3130634/download?type=zip)

```python
import wifi
import socketpool
from adafruit_httpserver.server import Server, Request, Response
from secrets import secrets

# Connect to Wi-Fi
print("Connecting to WiFi...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to", secrets["ssid"])
print("IP address:", wifi.radio.ipv4_address)

# Create server
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

# Start server
server.start(str(wifi.radio.ipv4_address))


print("Go to: http://", wifi.radio.ipv4_address)
```

Now open a browser and go to that address! You’ll get an error — we haven’t sent a response yet! 👇

---

## 🌍 Step 6: Send a Web Page

Add to the above:

```python
# Define a route and response
@server.route("/")
def base(request: Request):
    return Response(request, body="Hello from Pico W!")

# Start server
server.start(str(wifi.radio.ipv4_address))

# Loop forever
while True:
    try:
        server.poll()
    except Exception as e:
        print("Error:", e)
```

---

## ✅ Final Challenge!

Change the message in the HTML! For example:

```python
html = "<html><body><h1>You’re awesome, coder!</h1></body></html>"
```

Can you:
- Make a second HTML page?
- Add buttons or links?

---

## 🧠 Review Questions

- What does `server.accept()` do?
- What is an IP address?
- What happens if you change the port from 80 to 8080?

---

## 🎉 Great Work!

You've created a tiny **web server** running on a **microcontroller**! This is a BIG deal — you're now a **physical computing web wizard**!

