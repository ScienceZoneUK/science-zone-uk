
# 🐢 Saturday Python Lesson Plan

## 🔥 Starter Activity: "Code Your Week"

Use **functions**, **lists**, and **dictionaries** to model the days of your week.

---

### 🟢 Easy – "List Your Week"
**Goal**: Use a list and a for loop to print your weekly plan.

```python
week = #create a list [] of week days "Monday","Tuesday",.....

for day in week:
    print("???")
```

➡️ **Extension**: Add an activity list for each day and print both.

---

### 🟡 Medium – "Weekly Schedule with Dictionary"
**Goal**: Use a dictionary to store your week with one activity per day, finish off the program.

```python
#Complete the dictionary
week = {
    "Monday": "Maths",
    "Tuesday": "Science",
    "Wednesday": "???",
    "????": "????",
   
}

for day, activity in week.items():
    print(day,activity) #Improve the print statement
```

➡️ **Extension**: Put the loop in a function, pass in the dict as a parameter, then call the function:

```python
def show_week(?????):
    for day, activity in ?????.items():
        print(f"{day}: {activity}")
```

---

### 🔴 Hard – "Custom Week Planner"
**Goal**: Let the user input their own week using a loop and a dictionary.

```python
my_week = {}

for _ in range(7):
    day = input("?????")
    activity = input(f"What do you do on {day}? ")
    my_week[day] = activity

#Add the same function as in the medium activity and call it
```

➡️ **Extension**: Turn the input into a function and let them save multiple weeks!

---

## 🎨 Activity 1: Random Walker

### 👣 Step-by-step Modelling:
Import the correct libraries
```python
import turtle as t
import random
```
initiate the class object(oops)
```python
tim = t.Turtle()
```
Initialise the variables
```python
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
```
Set up turtle parameters
```python
tim.pensize(15)
tim.speed("fastest")
```
Run a loop to draw 100 iterations
```python
for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
```

---

### ✨ Extension: Many Walkers

```python
walkers = []

for _ in range(10):
    new_turtle = t.Turtle()
    new_turtle.pensize(10)
    new_turtle.speed("fastest")
    walkers.append(new_turtle)

for _ in range(100):
    for walker in walkers:
        walker.color(random.choice(colours))
        walker.forward(20)
        walker.setheading(random.choice(directions))
```

---

## ☕ Activity 2: Coffee Machine

Use the provided `CoffeeMachine` class. Students will write a program that **uses** it.

```python
from coffee_machine import CoffeeMachine

machine = CoffeeMachine()
machine.print_menu()
choice = input("Which coffee? ").lower()

if machine.check_resources(choice):
    cost = machine.menu[choice]["price"]
    if machine.process_payment(cost):
        machine.make_coffee(choice)
```

### ✅ Learning Goals:
- Use a class
- Call functions from an object
- Understand input/output

---

## 🎨 Plenary: Make More Art

Ask: "Can code be art?"

Ideas:
- Rainbow spirals
- Circles on circles
- Trails that never lift
- Use `random` for colors, size, or angles
