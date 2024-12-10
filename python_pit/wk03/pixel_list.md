
# 🐢 Drawing Pixel Art with Python Turtle 🎨

Welcome, future Python artist! 👋 In this project, we’ll use Python’s **Turtle** module to create colorful pixel art. Turtle lets you draw amazing shapes and pictures by controlling a virtual "pen" on your screen. Today, we’re going to recreate an 8x8 pixel crocodile design. 🐊

---

## 🌟 What Will You Learn?

- **Colors**: How to use RGB colors in Python.
- **Grids**: How to draw shapes in a grid layout.
- **Turtle Graphics**: How to use the Turtle module for fun and creative coding.

By the end of this project, you'll have a colorful piece of pixel art to show off!

---

## 🌈 What’s the Plan?

We’ll break it down into these steps:
1. **Set up the screen and Turtle**: Create the canvas where we’ll draw.
2. **Define colors**: Choose the colors for the crocodile.
3. **Draw the grid**: Use Turtle to draw each pixel in the right place.

Let’s get started!

---

## 🛠️ Step-by-Step Guide

### 1. **Set Up Your Python Environment**
You can use an online Python IDE like [Replit](https://replit.com/) or install Python on your computer. Make sure the Turtle module is available—it comes pre-installed with Python!

### 2. **Code Walkthrough**
Here’s how the code works:

#### import the turtle class
```python
import turtle
```

#### Define the Colors
```python
a = (255, 255, 255)  # White
c = (0, 0, 0)        # Black
f = (25, 25, 112)    # MidnightBlue
m = (34, 139, 34)    # ForestGreen
```
These are the colors we’ll use in the crocodile’s design. The numbers are **RGB values** that tell Python how much red, green, and blue to mix.

---

#### Create the Pixel Image
```python
image = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c, c, c, c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m,
]
```
This is a grid (8x8) of colors that represents the crocodile. Each `m`, `c`, `f`, and `a` corresponds to a color.

---

#### Draw the Grid
```python
rows, cols = 8, 8  # Dimensions of the grid
pixel_size = 20    # Size of each pixel

start_x = -cols * pixel_size // 2 # Centers the grid horizontally '//' floors the division by making an interger
start_y = rows * pixel_size // 2 # Centers the grid Vertically

for row in range(rows):
    for col in range(cols):
        color = image[row * cols + col]
        t.goto(start_x + col * pixel_size, start_y - row * pixel_size)
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(pixel_size)
            t.right(90)
        t.end_fill()
```
This part:
1. Moves the Turtle to the correct position.
2. Draws a square for each pixel.
3. Fills the square with the correct color.

---

### 🧑‍🎨 Do It Yourself: Create Your Own Pixel Art

Want to make your own masterpiece? Follow this plan:

### Pseudocode
1. Choose your colors and assign them names.
2. Create a grid for your design (e.g., 8x8 or larger).
3. Write a loop to draw each pixel in the grid.

### Code Snippets:
#### Example: A Smiley Face
```python
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

smiley = [
    white, white, yellow, yellow, yellow, yellow, white, white,
    white, yellow, white, yellow, yellow, white, yellow, white,
    yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
    yellow, black, yellow, yellow, yellow, yellow, black, yellow,
    yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
    white, yellow, black, yellow, yellow, black, yellow, white,
    white, yellow, yellow, yellow, yellow, yellow, yellow, white,
    white, white, yellow, yellow, yellow, yellow, white, white,
]
```
🎯 **Challenge:** Create a pixel art design of your favorite character or animal!

---

## 🎉 Wrapping Up

Amazing job! You’ve learned:
- How to use Turtle to create pixel art.
- How to represent images as grids of colors.
- How to bring your designs to life with loops and Turtle graphics.

Python Turtle is just the beginning of your coding creativity—keep exploring and making cool things!

---

## 📚 Learn More
Here are some fun resources to try next:
- [Turtle Academy](https://turtleacademy.com/) - Learn more about Turtle Graphics.
- [Code.org](https://code.org/) - Fun coding activities for beginners.
- [Pixel Art Maker](https://www.pixilart.com/) - Design pixel art for your next Turtle project!

Keep being awesome, and happy coding! 🚀
