# Micro:bit Workshop: Build Your Own Snake Game!

**Age Group:** 13-year-old young developers

**Duration:** 1.5 hours

**Tools:** 
- [MicroPython Editor](https://python.microbit.org/v/3)
- [Microbit API Documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/index.html)

---

## 👋 Welcome!
Hey there, coder! Ready to make your own video game on a tiny computer? 🎮🐍

In this workshop, you’ll learn how to build the legendary **Snake** game using your **Micro:bit** and a bit of Python code. It’s fun, a little tricky, and 100% awesome when you get it working.

---

## 🧠 What You'll Learn (Your Coding Superpowers!)
By the end of this, you’ll be able to:
- Use **variables** to store info
- Control the **LED screen**
- Use **lists** to track your snake
- Make things happen with **loops** and **if statements**
- Use **buttons and gestures** to control the game
- Add **random apples** to eat and grow
- Think like a programmer!

---

## 🐍 Why Snake?
Snake is a perfect game to build:
- It’s simple (just a grid and a snake).
- It teaches important logic and movement rules.
- You get to see your code come to life!
- It’s fun to play — and you can make it your own!

---

## 💻 Get Set Up
1. Plug in your Micro:bit.
2. Go to: [python.microbit.org/v/3](https://python.microbit.org/v/3)
3. Start a **new project**.

---

## ✅ Step-by-Step Coding Activities

### 🧩 STEP 1: Start Your Snake
```python
# Start the snake with one square in the center of the 5x5 grid
snake = [[2, 2]]

# Print the position to the serial monitor
print(snake)
```

---

### 💡 STEP 2: Show the Snake
```python
from microbit import *

snake = [[2, 2]]  # Start position of the snake

def draw_snake():
    display.clear()  # Clear the screen
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)  # Light each body segment

draw_snake()  # Call the function to draw the snake
```

---

### 🔁 STEP 3: Make It Move!
Try this code
```python
from microbit import *

snake = [[2, 5]]  # Snake starts at the bottom center

def draw_snake():
    display.clear()
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)

direction = [0, -1]  # initially moving up

while True:
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, head)
    snake.pop()
    draw_snake()
    sleep(500)
```

The snake goes up until it hits the top, then you get and **error**.     
We need to fix this with modulo!

#### 🔢 Modulo ( % ) Explained:
Using Modulo in the Snake Game

In a Snake game on the Micro:bit’s **5×5 grid**, the modulo operator (`%`) helps the snake **wrap around the edges**.

### 📦 What is Modulo?

```python
a % b
```

Returns the **remainder** after dividing `a` by `b`.

### 🔁 Examples:

```python
print(6 % 5)   # 1
print(-1 % 5)  # 4
print(3 % 5)   # 3
```

- `6 % 5` → 1 (goes just past the edge, wraps to 1)
- `-1 % 5` → 4 (off the left edge, wraps to the right)
- `3 % 5` → 3 (still in range)
- `? % 5` → ? is the position of the snake(could be x or y) and 5 is the wrap value(max pixel no.)

### 🧭 Wrapping the Snake

Instead of writing:

```python
if x > 4: x = 0
if x < 0: x = 4
```

Use:

```python
x = (x + dx) % 5
y = (y + dy) % 5
```

✅ This keeps `x` and `y` always between 0–4 — perfect for looping around the grid!

## 🧠 Explanation: How the Snake Moves

This loop runs forever, moving the snake step by step:

```python
while True:
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    head = wrap(head)
    snake.insert(0, head)
    snake.pop()
    draw_snake()
    sleep(500)
```

### 🐍 What Each Line Does

#### 🔁 `while True:`
Keep going forever — this is the **main game loop**!

---

#### 🧭 `head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]`
- The snake's **head is the first block** in the `snake` list.
- This line **moves the head one step** in the current direction (left, right, up, or down).

---

#### 🔄 `head = wrap(head)`
- If the head goes **off the edge**, wrap it around to the other side of the screen.

---

#### 🆕 `snake.insert(0, head)`
- Adds the new head to the **front** of the snake.
- The snake looks like it's moving forward!

---

#### ❌ `snake.pop()`
- Removes the **last block** (the tail).
- This keeps the snake the same length unless it eats food.

---

#### 💡 `draw_snake()`
- Lights up the LEDs to **show the snake** on the Micro:bit.

---

#### 💤 `sleep(500)`
- Wait 500 milliseconds (half a second) before doing it all again.
- This controls the **speed** of the game.

---

### 🔁 In short:
1. Move head  
2. Wrap if needed  
3. Add new head  
4. Remove tail  
5. Show it  
6. Wait a bit...

...and repeat!

Try this code snippet:
```python

from microbit import *

snake = [[2, 4]]  # Snake starts in the bottom center
# REMEMBER leds are indexed 0 - 4, top - bottom & left - right

direction = [0, -1]  # initially moving up

head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
#snake[0] is the head
#snake[0][0] is snake segment x pos
#snake[0][1] is snake segment y pos
display.set_pixel(head[0], head[1], 9)  # Light up the snake body
pos = "snake head position: "
print(pos) #[2,4]
print(head)
print('\n')
#######CHALLENGE#########
challenge = "TRY THE CHALLENGE\n"
this = "CAN YOU PRINT --> head x pos?"
print(challenge + this)

```



#### ✅ Test Code: Snake Slithering Forever
```python
from microbit import *

snake = [[2, 2]]  # Start in the center of the screen
direction = [0, -1]  # Initial movement direction (up)

def draw_snake():
    display.clear()  # Clear the screen
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)  # Light up the snake body

def wrap(position):
    return [position[0] % 5, position[1] % 5]  # Keep snake inside screen using modulo

while True:
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]  # Calculate new head position
    head = wrap(head)  # Wrap around edges if needed
    snake.insert(0, head)  # Add new head to the snake
    snake.pop()  # Remove the tail
    draw_snake()  # Show updated snake
    sleep(500)  # Wait so it doesn't move too fast
```

---

### 🕹️ STEP 4: Control the Snake

#### 🎯 Test 1: Try the Buttons!
```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show("A")  # Show A when button A is pressed
    if button_b.was_pressed():
        display.show("B")  # Show B when button B is pressed
```

#### 🎯 Test 2: Try the Accelerometer!
```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()  # Get the direction the Micro:bit is tilted
    display.scroll(gesture)  # Scroll the word on the screen
    sleep(500)
```

#### ✅ Full Control Code:
```python
from microbit import *

snake = [[2, 2]]  # Starting snake

direction = [0, -1]  # Starting direction (up)

def draw_snake():
    display.clear()  # Clear the display
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)  # Show the snake

def wrap(position):
    return [position[0] % 5, position[1] % 5]  # Keep the position inside screen limits

while True:
    gesture = accelerometer.current_gesture()  # Read which way the Micro:bit is tilted

    if button_a.was_pressed():
        direction = [-1, 0]  # Move left
    if button_b.was_pressed():
        direction = [1, 0]  # Move right
    if gesture == "up":
        direction = [0, -1]  # Move up
    if gesture == "down":
        direction = [0, 1]  # Move down

    head = wrap([snake[0][0] + direction[0], snake[0][1] + direction[1]])  # Move the head and wrap if needed
    snake.insert(0, head)  # Add new head to the snake
    snake.pop()  # Remove tail
    draw_snake()  # Draw updated snake
    sleep(400)  # Control the speed
```

---

### 🍏 STEP 5: Add Apples!

#### 🧪 Test Code:
```python
import random
print(random.randint(0, 4))  # Show random number from 0–4
```

#### ✅ Full Apple Code:
```python
import random
from microbit import *

snake = [[2, 2]]  # Starting snake position
apple = [random.randint(0, 4), random.randint(0, 4)]  # Random apple location
direction = [0, -1]  # Start direction

def draw_snake_and_apple():
    display.clear()  # Clear screen
    display.set_pixel(apple[0], apple[1], 5)  # Draw apple
    for segment in snake:
        display.set_pixel(segment[0], segment[1], 9)  # Draw each snake body part

def wrap(position):
    return [position[0] % 5, position[1] % 5]  # Wrap around the screen

while True:
    gesture = accelerometer.current_gesture()  # Read tilt direction
    if button_a.was_pressed(): direction = [-1, 0]  # Go left
    if button_b.was_pressed(): direction = [1, 0]  # Go right
    if gesture == "up": direction = [0, -1]  # Go up
    if gesture == "down": direction = [0, 1]  # Go down

    head = wrap([snake[0][0] + direction[0], snake[0][1] + direction[1]])  # New head position
    snake.insert(0, head)  # Add new head

    if head == apple:
        apple = [random.randint(0, 4), random.randint(0, 4)]  # Eat apple and place new one
    else:
        snake.pop()  # No apple = stay same size

    draw_snake_and_apple()  # Draw everything
    sleep(400)  # Control speed
```

---

## 🚩 CHALLENGES (For Coding Legends 💪)
- Add **game over** if the snake hits itself.
- Add a **score tracker** using the serial or LEDs.
- Make **apples disappear** after a few seconds.
- Speed up the snake as it gets longer.

---

## 🤔 REFLECTION TIME
- What did you enjoy most about coding Snake?
- What surprised you?
- What would you change if you made “Super Snake 2.0”?

---

## 🌟 YOU DID IT!
You built a game from scratch – using logic, loops, and creativity. You’re officially a Micro:bit game developer. Great job, coder! 🎉

🐍✨🎮

