#   Micro-Bit Workshop : Treasure Hunt 🏴‍☠️

# 👋 Welcome!
Ahoy, young coder! Ready to turn your Micro:bit into a real-life treasure detector?

In this workshop, you'll create your very own Treasure Hunt game using MicroPython and two Micro:bits. You’ll use radio signals, compass directions, and some clever coding to help players track down hidden treasure. It’s exciting, a bit mysterious, and seriously rewarding when it all comes together!

# 🧠 Objectives

- You will be able to recall key MicroPython functions such as `display.scroll()`, `radio.send()`, and `compass.heading()`.
- You will be able to explain how radio signals and compass readings are used to detect proximity in the treasure hunt game.
- You will be able to write MicroPython code that uses the radio and compass to guide users in the game.
- You will be able to compare signal strength values and analyse how these affect LED brightness on the receiver.
- You will be able to assess the effectiveness of their radar design and suggest ways to improve feedback to the user.
- You will be able to develop a fully working treasure hunt game using two micro:bits and MicroPython code.

# 🗺️ Why Treasure Hunt?
Treasure Hunt is a great game to build because:

It’s simple just two Micro:bits and a bit of Python magic.

It teaches you how radio signals and compass readings work.

You’ll see your code come alive as the Micro:bit becomes a real tracker!

It’s super fun and you can customise it with sounds, lights, or challenges!

# 💻 Get Set Up
- Plug in your Micro:bit.
- Go to: python.microbit.org/v/3
- Start a new project.

# Coding Activity

## 🧩 Step 1 setting up the transmiter (treasure)
## Transmiter
```
from microbit import *
import radio
radio.config(group=1, power=1)
radio.on()

while True:
    radio.send('1')
    sleep(200)
```

##🧠 Code Breakdown – Line by Line

`from microbit import *`
👉 This brings in everything your micro:bit needs to work:
like `display`, `sleep()`, and `buttons`.

`import radio`
📡 This brings in the radio tools, so your micro:bit can send and receive messages wirelessly.

`radio.config(group=1, power=1)`
🛠 This sets up the radio system:

`group=1`
→ Think of this like a walkie-talkie channel.
Only micro:bits using the same group number can talk to each other.

`power=1`
→ This controls how far the signal goes.
`1` = short range (about 1 meter), `7 `= long range (up to 70+ meters).

`radio.on()`
🔛 This turns the radio on, so your micro:bit can start sending.

`while True:`
🔁 This starts a forever loop — your micro:bit will keep doing what’s inside this loop again and again.

`radio.send('1')`
📨 This sends the message `'1' `over the radio.

💬 We’re not sending useful data — just something the other micro:bit can listen for.

`sleep(200)`
⏱ Wait for 200 milliseconds (0.2 seconds) before repeating.

This gives the micro:bit a short pause between each message.

## ✅ What the Code Does All Together
This code turns your micro:bit into a transmitter:

* It sends a radio message every 0.2 seconds

* Any nearby micro:bit (using the same group) can listen and measure how strong the signal is

* This helps you build a project like a signal strength meter (like the bars on your phone 📶)

💡 Fun Experiments
Try these after it works:

🔋 Power the transmitter with batteries and walk around the room

👀 Watch how signal strength changes on the receiver

🛠 Change power=1 to power=7 and test the range

🎨 Add icons like display.show(Image.HEART) when sending



## Setting up the Receiver

```
from microbit import *
import radio
radio.config(group=1)
radio.on()
light = Image(5,5) # create an empty image

# function to map signal stength to LED brightness
def map(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

while True:
    message = radio.receive_full()
    if message:
        signal = message[1]
        brightness = map(signal, -98, -44, 0, 9)
        light.fill(round(brightness))
        display.show(light)

```







