
# 🐢 Saturday Python Lesson Plan

## 🔥 Starter Activity: "Code Your Own Schedule"

Use **functions**, **lists**, **dictionaries** and **loops** to model a daily schedule.

---

### 🟢 Easy – "List Your Activities"
**Goal**: Use a list and a for loop to print your daily activities.

```python
schedule = #create a list [] of activities "Wake up","Watch instagram reels",.....

for activity in schedule:
    print("???")
```

➡️ **Extension**: Add a new list storing the time for each activity and print both.

---

### 🟡 Medium – "Daily Schedule with Dictionary"
**Goal**: Use a dictionary to store your schedule with each activity having a time, finish off the program.

```python
#Complete the dictionary
schedule = {
    "Wake up": "8am",
    "Watch instagram reels": "8:01am",
    "Breakfast": "???",
    "????": "????",
    #add as many activities as you can think of!
}

for activity, time in schedule.items():
    print(activity,time) #Improve the print statement
```

➡️ **Extension**: Put the loop in a function, pass in the dict as a parameter, then call the function:

```python
def show_schedule(?????):
    for activity, time in ?????.items():
        print(f"{activity}: {time}")
```

---

### 🔴 Hard – "Custom Schedule Planner"
**Goal**: Let the user input their own schedule using a loop and a dictionary.

```python
my_schedule = {}

for ???? in range(?):
    activity = input("?????")
    time = input(f"What time do you {day}?")
    my_schedule[activity] = time

#Add the same function as in the medium activity and call it
```

➡️ **Extension**: Turn the input into a function and let them save multiple schedules!

---

## 🎨 Activity 1: Making a flag with Turtle
![Alt text](https://www.101computing.net/wp/wp-content/uploads/flag-template-split-2.png "Flag Coordinates")

![Alt text](https://www.101computing.net/wp/wp-content/uploads/flag-template-split-3.png "Flag Coordinates")

### 👣 Step-by-step Modelling:
Import the correct libraries
```python
import turtle as t
```

initiate the class object(oops)
```python
terry = t.Turtle()
```

Set up turtle parameters
```python
terry.shape("arrow")
terry.speed(10)
window = turtle.Screen()
window.bgcolor("#DDDDDD")
```

Run a loop to draw 100 iterations
```python
#Draw the frame for the flag
terry.color("white")
terry.pensize(2)
terry.fillcolor("white")
#Position the pen in the bottom left corner
terry.penup()
terry.goto(-180, -120)
terry.pendown()
terry.begin_fill()
terry.goto(180,-120)
terry.goto(180,120)
terry.goto(-180,120)
terry.goto(-180, -120)
terry.end_fill()  
  
#Draw the blue stripe
terry.color("blue")
terry.pensize(2)
terry.fillcolor("blue")

terry.penup()
terry.goto(-180, -120)
terry.pendown()
terry.begin_fill()
terry.goto(-60,-120)
terry.goto(-60,120)
terry.goto(-180,120)
terry.goto(-180, -120)
terry.end_fill()  

#Draw the red stripe
terry.color("red")
terry.pensize(2)
terry.fillcolor("red")

terry.penup()
terry.goto(60, -120)
terry.pendown()
terry.begin_fill()
terry.goto(180,-120)
terry.goto(180,120)
terry.goto(60,120)
terry.goto(60, -120)
terry.end_fill()  
```

---

## ☕ Activity 2: Android Robot
You need to copy and save the class AndroidRobot.py ( in wk13 repository) into your python folder to be able to use it. 

### ☕ Android Robot Class Documentation

The `AndroidRobot` class simulates an humanoid robot. You can use it in your own Python programs to simulate having a robot workforce.

---

### 📦 What the Class Can Do

### `AndroidRobot.charge(amount)`
Charges the robot's battery by a specified amount.

**Example:**
```python
AndroidRobot.charge(10)
```

---

### `AndroidRobot.work(task):`
Make the robot perform a task, this will also reduce the robots battery.

**Example:**
```python
AndroidRobot.work("Heavy Lifting")
```

---

### `AndroidRobot.report_status():`
Returns the current status and battery level of the robot.


**Example:**
```python
AndroidRobot.report_status()
```

---

### `AndroidRobot.self_destruct()`
The robot will self destruct making it unable to run any other method.

**Example:**
```python
AndroidRobot.self_destruct()
```

---

### `AndroidRobot.power_on()`
The robot will power on changing it's status.

**Example:**
```python
AndroidRobot.power_on()
```

---

### `AndroidRobot.shut_down()`
The robot will shut down changing it's status and preventing it from performing a task.

**Example:**
```python
AndroidRobot.shut_down()
```

---



Use the provided `AndroidRobot` class.  Write a program that **uses** it.

```python
from AndroidRobot import AndroidRobot

# Step 1: Make your robot (look at the AndroidRobot class file to see how to intialise the robot)

# Step 2: Ensure the robot is powered on

# Step 3: Check the robot's status

# Step 4: Make the robot get to work performing multiple tasks until the battery runs out

# Step 5: Shut down the robot and charge it

# Step 6: Say goodbye to the robot and destroy it
```

## 🎯 Bonus Challenges

- Make the program **loop** so it endlessly performs tasks.
- Add a new method to the AndroidRobot class
- Have multiple robots all perfoming different tasks 
