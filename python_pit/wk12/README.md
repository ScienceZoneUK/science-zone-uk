
# 🐍 Python Functions + Alarm Clock + Horse Game Worksheet  
## For Ages 11–13 | Theme: Writing Functions, Using Return Values, Turtle Graphics  

---

## 🎯 OBJECTIVES

By the end of this worksheet, you will:

- ✅ Know how to write your own functions in Python  
- ✅ Understand how to use `return` to send back values  
- ✅ Create a simple text-based alarm clock  
- ✅ Build a fun horse racing game using Turtle graphics  
- ✅ Learn how to control the game with the keyboard  

---

## 🔑 CHEAT SHEET – Things You’ll Use

| What You’re Doing        | Example                               | What It Means                                   |
|--------------------------|----------------------------------------|--------------------------------------------------|
| Start a function         | `def say_hi():`                       | You’re telling Python to make a function         |
| Return a value           | `return "Hello"`                      | This sends back something                        |
| Run the function         | `say_hi()`                            | This runs it (calls it)                          |
| Save the result          | `message = say_hi()`                  | Stores what the function returned                |
| Ask for input            | `input("What is your name?")`         | Gets text from the user                          |
| Make a decision          | `if x == y:`                          | Only do something if this is true                |
| Get real time            | `datetime.now().strftime("%H:%M")`   | Gets the computer's clock in hour:minute format |

---

## 🧠 TASK 1: Three Simple Functions

👉 Fill in the blanks to finish this small program. It uses **3 functions**.

```python
# A. Function that says hello
def greet():
    return _______

# B. Function that asks for your name
def get_name():
    return _______("What is your name? ")

# C. Function that builds a message
def make_message(name):
    return "Nice to meet you, " + _______

# D. Use your functions!
print(greet())
name = get_name()
message = make_message(name)
print(_______)
```

---

## ⏰ TASK 2: Make an Alarm Clock

This program:
- Asks the current time
- Asks the alarm time
- Prints a message if it’s time to wake up

You MUST use **3 functions** and **return values**.

### ✍️ Fill in the scaffold:

```python
def get_current_time():
    return ____________________________

def get_alarm_time():
    return ____________________________

def check_alarm(current, alarm):
    if current == alarm:
        return "⏰ WAKE UP! It's time!"
    else:
        return ____________________________

# --- MAIN PROGRAM ---
current_time = get_current_time()
alarm_time = get_alarm_time()
message = check_alarm(current_time, alarm_time)
print(__________)
```

---

## ⏰ BONUS TASK: Real-Time Alarm with Loop

This version uses the real computer time and keeps checking every few seconds.

```python
from datetime import datetime
import time

def get_current_time():
    return ____________________________

def get_alarm_time():
    return ____________________________

def check_alarm(current, alarm):
    if current == alarm:
        return "⏰ WAKE UP! It's time!"
    else:
        return ____________________________

# --- MAIN PROGRAM ---

alarm_time = get_alarm_time()

while True:
    current_time = get_current_time()
    message = check_alarm(current_time, alarm_time)

    if message == "⏰ WAKE UP! It's time!":
        print(message)
        break

    time.sleep(10)
```

---

## 🐢 HORSE RACING GAME (TURTLE)

Let’s make a race where your horse (a square) runs across the screen!

---

## 🎮 STEP-BY-STEP GAME

### 1️⃣ Import the libraries

```python
import turtle
import time
import random
```

### 2️⃣ Set up the race screen

```python
screen = turtle.Screen()
screen.title("🐎 Horse Race!")
screen.bgcolor("lightgreen")
```

### 3️⃣ Draw a finish line

```python
finish_line = 200
line = turtle.Turtle()
line.penup()
line.goto(finish_line, -100)
line.pendown()
line.left(90)
line.forward(200)
line.hideturtle()
```

### 4️⃣ Draw your horse

```python
horse = turtle.Turtle()
horse.shape("square")
horse.color("brown")
horse.penup()
horse.goto(-200, 0)
```

### 5️⃣ Make it run (automatic)

```python
while horse.xcor() < finish_line:
    step = random.randint(5, 15)
    horse.forward(step)
    time.sleep(0.1)
```

### 6️⃣ Show the finish message

```python
horse.write("🏁 Finished!", align="left", font=("Arial", 16, "bold"))
turtle.done()
```

---

## 🕹️ ADD KEYBOARD CONTROL (spacebar to move)

```python
def move_horse():
    if horse.xcor() < finish_line:
        step = random.randint(5, 15)
        horse.forward(step)
        if horse.xcor() >= finish_line:
            horse.write("🏁 Finished!", align="left", font=("Arial", 16, "bold"))

screen.listen()
screen.onkey(move_horse, "space")
turtle.done()
```

---

## 🎉 NICE JOB!

You learned how to:
- Make and use functions
- Build a text-based alarm clock
- Use your computer’s real clock
- Create a horse racing game
- Control it with the keyboard
