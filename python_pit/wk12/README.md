
# 🐍 Python Functions + Alarm Clock Worksheet  
## Age: 11–13 | Theme: Writing Functions, Using Returns  

---

## 🔑 CHEAT SHEET

| Concept              | Example                         | Description                              |
|----------------------|----------------------------------|-------------------------------------------|
| Define a function    | `def say_hi():`                 | Start of a function                       |
| Return something     | `return "Hello"`                | Sends back a value                        |
| Call a function      | `say_hi()`                      | Runs the function                         |
| Store return value   | `message = say_hi()`            | Saves the output                          |
| Input from user      | `input("Type here: ")`          | Ask the user to type something            |
| If statement         | `if x == y:`                    | Checks if something is true               |

---

## 🧠 TASK 1: THREE FUNCTIONS (WARM-UP)

Fill in the blanks to complete the program.

```python
# A. Write a function that says hello
def greet():
    return _______

# B. Write a function that asks for your name
def get_name():
    return _______("What is your name? ")

# C. Write a function that combines the message
def make_message(name):
    return "Nice to meet you, " + _______

# D. Now run your functions!
print(greet())
name = get_name()
message = make_message(name)
print(_______)
```

---

## ⏰ TASK 2: MAKE A SIMPLE ALARM CLOCK

Your goal: Ask for the current time and the alarm time, and then print a message if it's time to wake up.

You **must use 3 functions** and return values.

---

### ✅ Scaffold

```python
# 1. Ask the user for the current time
def get_current_time():
    # Ask for input and return it
    return ____________________________

# 2. Ask the user to set an alarm
def get_alarm_time():
    return ____________________________

# 3. Compare the current time and alarm
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

## ⭐️ CHALLENGE

- Can you make the program repeat using a `while` loop?
- Can you make the computer beep? Try `print("\a")`  
- Add your own funny alarm message


## Horse racing game

Copy the blocks one by code to build program. 


1) Import the libraries

```python
import turtle
import time
import random
```

2) Set up the screen

```python
# Set up the screen
screen = turtle.Screen()
screen.title("🐎 Horse Race!")
screen.bgcolor("lightgreen")
```

3) Place a finish line

```python
# Draw the finish line
finish_line = 200
line = turtle.Turtle()
line.penup()
line.goto(finish_line, -100)
line.pendown()
line.left(90)
line.forward(200)
line.hideturtle()
```

4) Draw a horse

```python
# Create the horse
horse = turtle.Turtle()
horse.shape("square")
horse.color("brown")
horse.penup()
horse.goto(-200, 0)
```

5) Loop that moves the horse

```python
# Move the horse forward until it crosses the finish line
while horse.xcor() < finish_line:
    step = random.randint(5, 15)  # random step for fun
    horse.forward(step)
    time.sleep(0.1)
```

6) Horse crosses finish line, print message

```python
# Print message when done
horse.write("🏁 Finished!", align="left", font=("Arial", 16, "bold"))

# Keep window open
turtle.done()
```

7) Play game, use debug and step-into to help you understand whats happening

## Add user interactivity
Replace the game logic while loop with this function.    
The screen object is then setup to listen for a space bar input.

```python
# Function to move the horse when spacebar is pressed
def move_horse():
    if horse.xcor() < finish_line:
        step = random.randint(5, 15)
        horse.forward(step)
        if horse.xcor() >= finish_line:
            horse.write("🏁 Finished!", align="left", font=("Arial", 16, "bold"))

# Connect the spacebar to the move_horse function
screen.listen()
screen.onkey(move_horse, "space")

# Keep window open
turtle.done()

```




