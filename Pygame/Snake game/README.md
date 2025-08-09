# 🐍 Let's Learn Pygame and Make a Snake Game!

## 🎮 What is Pygame?
Pygame is like a **toolbox for making games in Python**.  
It gives you ready-made tools to:
- 🎨 Draw shapes, pictures, and text on the screen
- 🎵 Play sounds and music
- 🎹 Use the keyboard and mouse to control your game
- 🕒 Control time and movement in the game

Think of Pygame as a set of LEGO blocks 🧱 — you can snap them together to build your own game world!

---

## 🐍 What is the Snake Game in Pygame?
The **Snake Game** is a classic computer game where:
1. You control a snake that moves around the screen.
2. Your job is to eat food (🍎) to grow longer.
3. But be careful! If you hit the wall or bite your own tail, you lose.

In Pygame, we can:
- Draw the snake as green squares
- Draw the food as red squares
- Make the snake move when we press arrow keys
- Check if the snake eats the food or crashes

---

## 🎯 Objective of the Snake Game
- **Eat the food** to get points and grow longer.
- **Don’t crash** into walls or your own tail.
- Try to get the **highest score** possible before the snake crashes!

---

## 💻 How to Install Pygame in VS Code
1. **Install Python**  
   Download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
   When installing, tick the box that says **"Add Python to PATH"**.

2. **Open VS Code**  
   Download here: [https://code.visualstudio.com/](https://code.visualstudio.com/)

3. **Open the Terminal**  
   - Go to **View > Terminal** in VS Code.

4. **Install Pygame**  
   In the terminal, type:
   ```bash
   pip install pygame
   
# 🐍 Mini Snake Game — Step-by-Step Explanation

This is an easy, friendly explanation of how the **Mini Snake Game** code works. Read it like a recipe — each step does one simple job.

---

## 1 — `import` the tools we need
We start by telling Python which toolboxes we will use.

```python
import pygame
import random
```
- pygame is a toolbox that lets us draw, listen to the keyboard, and show a game window.
- random helps put the food in a random place so each game is different.

## 2 — Turn on Pygame
```python
pygame.init()
```
- This wakes up the Pygame toolbox so we can use it. Imagine pressing the power button on a toy.

##  Game settings: size, speed and colours
```python
WIDTH, HEIGHT = 400, 300
SNAKE_SIZE = 10
SPEED = 10
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
```
- WIDTH and HEIGHT are how big the game window is (in pixels). A pixel is a tiny dot on the screen.
- SNAKE_SIZE is how big each square of the snake is. We move the snake by this amount so it stays on a grid.
- SPEED decides how fast the game runs (higher = faster).
- The colors are given as three numbers (R, G, B). For example, (0, 255, 0) is bright green.
## 4 — Make the game window
```python
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake Game")
```
- This opens a window where the game will appear.
- The caption is the title shown at the top of the window.
  ## 5 — Start the snake and the food
 ```python
snake = [(100, 50)]
snake_dir = (SNAKE_SIZE, 0)
food = (200, 150)
 ```
- snake is a list of the pieces that make up the snake. Each piece is an (x, y) position on the screen.
- The snake starts with one piece at x=100, y=50.
- snake_dir is how much x and y change every step. (SNAKE_SIZE, 0) means "move right by one block."
- food is where the food sits on the screen.
## 6 — The clock
```python
clock = pygame.time.Clock()
```
- The clock makes sure the game runs at the same speed on different computers by controlling how many times the screen updates each second.
## 7 — The main game loop
```python
running = True
while running:
```
- This loop repeats over and over until running becomes False.
- Each loop is one frame (one step) of the game — the snake moves a little bit, we check for collisions, we draw the picture again.
  ## 8 — Check for player input (keyboard and window)
  ```python
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            snake_dir = (0, -SNAKE_SIZE)
  ```
- pygame.event.get() gives us a list of things the player did (like pressing keys or clicking the X button).
- If the player presses an arrow key, we change snake_dir so the snake will move that way.
  ## 9 — Move the snake (create a new head)
 ```python
new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
snake.insert(0, new_head)
 ```
- The snake's head is the first item in the snake list (snake[0]).
- We make a new head by adding snake_dir to the old head position — that moves the head.
- insert(0, new_head) adds the new head to the front of the list.
## 10 — Did the snake eat the food?
 ```python
if new_head == food:
    food = (random.randrange(0, WIDTH, SNAKE_SIZE),
            random.randrange(0, HEIGHT, SNAKE_SIZE))
else:
    snake.pop()
```
- If the head's position is the same as the food, it ate the food!
- We then make a new food position using random.randrange(...) which picks a number that matches the grid (so the food lines up with the snake).
- If the snake did not eat, we use pop() to remove the last piece of the tail — so the snake appears to move forward without growing.
## 11 — Did the snake hit a wall?
```python
if (new_head[0] < 0 or new_head[0] >= WIDTH or
    new_head[1] < 0 or new_head[1] >= HEIGHT):
    running = False
```
- If the head moves outside the window, the game ends — set running = False.
  ## 12 — Draw the game on the screen
 ```python
win.fill(BLACK)
for part in snake:
    pygame.draw.rect(win, GREEN, (*part, SNAKE_SIZE, SNAKE_SIZE))
pygame.draw.rect(win, RED, (*food, SNAKE_SIZE, SNAKE_SIZE))
 ```
- win.fill(BLACK) paints the background black.
- For each piece of the snake we draw a green square at its (x, y).
- We draw the food as a red square.
  ## 13 — Show the new picture and wait a little
```python
pygame.display.update()
clock.tick(SPEED)
```
- pygame.display.update() tells the computer to show everything we just drew.
- clock.tick(SPEED) pauses just enough so that the loop runs SPEED times per second. That controls how fast the snake moves.

## 14 — Close the game
```python
pygame.quit()
```
- This shuts down Pygame and closes the game window.
  # 🎯 Tiny Challenges (try these!)
  * Make it faster — change SPEED = 10 to a bigger number.
  * Change colours — pick different RGB numbers (e.g., BLUE = (0, 0, 255)).
  * Start with a longer snake — change snake = [(100, 50)] to snake = [(100,50),(90,50),(80,50)].
  * Prevent U-turns — only allow a new direction if it's not the exact opposite of the current one. (This stops the snake from instantly crashing into itself.)
  * Add a score — keep a score variable and increase it when eating food. Then draw the score using pygame.font.

## 🧩 Full Code (with simple comments)

```python
import pygame
import random

# Start Pygame (turns on the Pygame engine)
pygame.init()

# Game settings (window size, snake size and speed)
WIDTH, HEIGHT = 400, 300
SNAKE_SIZE = 10
SPEED = 10

# Colors (red, green, black as RGB numbers)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the game window and set the title
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake Game")

# The snake is a list of (x, y) positions. Start with one piece.
snake = [(100, 50)]

# Direction the snake moves each frame (x change, y change)
# Start moving right by one SNAKE_SIZE
snake_dir = (SNAKE_SIZE, 0)

# Food position (x, y)
food = (200, 150)

# Clock keeps the game running at the same speed on all computers
clock = pygame.time.Clock()

# Main game loop: the game keeps running until running = False
running = True
while running:
    # 1) Handle input (keyboard and window events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     # If user clicks the X button
            running = False
        elif event.type == pygame.KEYDOWN:
            # Arrow keys change the snake's direction
            if event.key == pygame.K_UP:
                snake_dir = (0, -SNAKE_SIZE)
            elif event.key == pygame.K_DOWN:
                snake_dir = (0, SNAKE_SIZE)
            elif event.key == pygame.K_LEFT:
                snake_dir = (-SNAKE_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                snake_dir = (SNAKE_SIZE, 0)

    # 2) Move the snake by creating a new head position
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)  # Put the new head at the front of the list

    # 3) Check if the snake ate the food
    if new_head == food:
        # Put the food somewhere new (random position aligned to the grid)
        food = (random.randrange(0, WIDTH, SNAKE_SIZE),
                random.randrange(0, HEIGHT, SNAKE_SIZE))
        # Don't remove the tail — that makes the snake grow
    else:
        # Remove the last piece of the snake (it moves forward)
        snake.pop()

    # 4) Check for wall collision (if the head goes outside the window)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False  # End the game

    # 5) Draw everything: background, snake, and food
    win.fill(BLACK)  # Fill screen with black
    for part in snake:
        # Draw each part of the snake as a green square
        pygame.draw.rect(win, GREEN, (*part, SNAKE_SIZE, SNAKE_SIZE))
    # Draw the food as a red square
    pygame.draw.rect(win, RED, (*food, SNAKE_SIZE, SNAKE_SIZE))

    # 6) Update the display and wait so the game runs at the chosen speed
    pygame.display.update()
    clock.tick(SPEED)

# Exit Pygame cleanly
pygame.quit()
