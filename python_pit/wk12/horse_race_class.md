
# 🐍 Python Workshop: Learning Classes with Turtle 🐢

## 👩‍🏫 Audience
**Ages:** 12–14  
**Duration:** 1.5 hours  
**Skills Practiced:** Variables, Functions, Lists, Dictionaries, Classes  

---

## 🧠 Starter Challenge: Code Ladder (15–20 min)

Try each level! If you're stuck, check [W3Schools Python](https://www.w3schools.com/python/).

### 🔢 1. Variables
```python
name = "Alex"
age = 12
print(f"My name is {name} and I am {age} years old.")
```
✅ Task: Change the name and age to your own and print a new message.

---

### 🧮 2. Functions
```python
def greet(name):
    print("Hello " + name + "!")

greet("Sam")
```
✅ Task: Modify it to include age and say how old the person is.

---

### 🎨 3. Lists
```python
colors = ["red", "blue", "green"]
for color in colors:
    print(color)
```
✅ Task: Add more colors and print: `"I like the color [color]!"`

---

### 🧾 4. Dictionaries
```python
student = {"name": "Lola", "age": 13, "hobby": "drawing"}
print(student["name"])
```
✅ Task: Add "favourite_food" and print all the key-value pairs using a loop.

---

## 🖼️ Activity 1: Andy Warhol Pop Art Circles (25 min)

Use the `turtle` module to draw art with no lines, only **circles**!         
Before you start, have a read of the turtle [documentation](https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions).

### 🧪 Try this:

Import libraries
```python
#import the turtle library
```
Lets setup the turtle screen. Create a screen object    
and colour it black.
```python
# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
```

Now lets create a turtle object, set the shape, lift the    
pen and set drawing colour.
```python
circle_turtle = turtle.Turtle()
circle_turtle.shape("circle")
circle_turtle.penup()
circle_turtle.color("hotpink")
```

We are going to draw a 3x3 grid using a for loop with range.     
The centre of the grid is 0, we start the x axis at -100 and finish at 100.       
Repeat this for the y axis. We use the turtle methods of goto() and stamp()     
to move and imprint the shape onto the canvas. 
```python
# Draw grid of circles
for x in range(-100, 101, 100):
    for y in range(-100, 101, 100):
        circle_turtle.goto(x, y)
        circle_turtle.stamp()

screen.exitonclick()
```

✅ Modify it:
1. Make a bigger grid.
2. Try a different color list and cycle through it.
3. Add random positions or a background color.
4. Make the grid appear hand drawn

---

## 🐎 Activity 2: Horse Race with a Class (35 min)

We will use a **custom class** to create horses and make them race!

---

---

## 📚 Class Documentation

```
Horse(name, color, y_pos)
    → Makes a horse with color and Y position

.move()
    → Moves horse forward randomly

.get_position()
    → Gets how far the horse has run

.celebrate()
    → Shows a message if this horse wins

.draw_lane()
    → Draws a race lane for this horse
```

---

### 1. Create a project folder called horse_race_class

### 2. Save the Horse class from this repo into your project folder

### 3. Now Use the Class in a Race
- Import the turtle and Horse class.
```python
from horse_race import Horse
from turtle import Screen
```
- Setup the turtle screen.
```python
# Setup screen
screen = turtle.Screen()
screen.title("Horse Race")
screen.bgcolor("white")
```
- Create instances of the horse class.
```python
# Create horses
horse1 = Horse("Lightning", "blue", 50)
horse2 = Horse("Thunder", "red", -50)
```
- The class provides horse lanes, just call the method .draw_lane().
```python
# Draw lanes
horse1.draw_lane()
horse2.draw_lane()
```
- Use a loop to move the horses until they pass the finish.
```python
# Race!
while horse1.get_position() < 200 and horse2.get_position() < 200:
    horse1.move()
    horse2.move()
```
- Write a message to celebrate the winning horse.
```python
# Who won?
if horse1.get_position() > horse2.get_position():
    horse1.celebrate()
else:
    horse2.celebrate()

turtle.done()
```



🎯 Tip: When stuck, search on [W3Schools Python](https://www.w3schools.com/python/).  
Happy coding!
