---

# 🎮 Micro:bit Lesson Pack — Tilt Maze

---

## 📌 Learning Objectives (Bloom’s Taxonomy)

By the end of this lesson, pupils will be able to:

* 🔵 **Remembering**: **Define** what a maze is and recall how the Micro:bit detects tilt using its accelerometer.
* 🟢 **Understanding**: **Describe** how tilting the Micro:bit changes the player’s movement inside the maze.
* 🟡 **Applying**: **Use** the Micro:bit accelerometer inputs to move a dot through the maze.
* 🟠 **Analysing**: **Compare** different maze layouts and identify which ones are easier or harder to solve.
* 🟣 **Creating**: **Design** their own Tilt Maze by editing the maze grid and testing it on the Micro:bit.

---

## 🕒 Lesson Flow

---

### 1️⃣ Why are Mazes Important? (10 mins)

💬 **Discussion Points:**
Ask students:

* Why do people enjoy solving mazes?
* Where do we see mazes in real life?

Examples:

* Puzzle books and magazines
* Video games (levels, dungeons)
* Real-life corn mazes or escape rooms

**Highlight:**
Mazes help us:

* Practice problem-solving
* Learn patience and planning
* Develop strategies
* Challenge ourselves in fun ways 🎮

**Introduce the Micro:bit:**
Explain that the Micro:bit is a tiny computer that can help us play mazes using:

* **Accelerometer:** Detects tilt (like a smartphone game)
* **LED screen:** Shows the maze, walls, player, and goal
* **Loops & logic:** Let us test if we’ve hit a wall or reached the goal

---

### 2️⃣ Problem Introduction & Class Discussion (10 mins)

🌟 **Tilt Maze Problem:**
We need to invent a Micro:bit game called **Tilt Maze**.

**Requirements:**

* Player dot starts at the top-left corner
* Tilt Micro:bit left, right, forward, backward to move the dot
* Walls block movement — you can’t go through them
* Reach the goal (bottom-right corner) to win
* Show a happy face 🎉 when you reach the goal

💬 **Discussion Prompt:**
Ask students:

* How can tilting the Micro:bit move the dot?
* What should happen if the player hits a wall?
* How can we clearly show where the goal is?
* How can we make the maze harder or easier?

---

### 3️⃣ Coding the Solution (20–25 mins)

💻 **Step-by-Step Build**


---

## 🎮 Tilt Maze Game – Step-by-Step Guide

This project creates a maze game using the **micro:bit**. You move a player by **tilting the micro:bit**, and the goal is to reach the **goal tile** at the end of the maze.

---

### 🔧 Step 1: Import the micro:bit module

```python
from microbit import *
```

* This line gives you access to the micro:bit's screen, accelerometer, and sleep functions.

---

### 🧱 Step 2: Create a class for the Maze Game

```python
class TiltMaze:
```

* We define a new **class** called `TiltMaze` to organize all the game logic.

---

### 🏁 Step 3: Set up the Maze and Player Position

```python
def __init__(self):
    self.player_x = 0
    self.player_y = 0
```

* The player starts at the **top-left corner** of the screen (0, 0).

```python
    self.maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 2]
    ]
```

* The maze is a **5×5 grid**.

  * `0` = empty space
  * `1` = wall
  * `2` = goal

---

### 🖼️ Step 4: Draw the Maze and Player

```python
def draw(self):
    display.clear()
```

* Clears the screen each time before drawing.

```python
    for y in range(5):
        for x in range(5):
            if self.maze[y][x] == 1:
                display.set_pixel(x, y, 3)  # wall
            elif self.maze[y][x] == 2:
                display.set_pixel(x, y, 7)  # goal
```

* Loops through the grid and lights up walls and the goal using different brightness levels.

```python
    display.set_pixel(self.player_x, self.player_y, 9)  # player
```

* The player is the **brightest pixel** (brightness 9).

---

### 🕹️ Step 5: Detect Movement by Tilting

```python
def move(self):
    x_tilt = accelerometer.get_x()
    y_tilt = accelerometer.get_y()
```

* Reads the tilt of the micro:bit using the accelerometer.

#### ➡️ Move Left or Right

```python
    if x_tilt < -300 and self.player_x > 0:
        if self.maze[self.player_y][self.player_x - 1] != 1:
            self.player_x -= 1
    elif x_tilt > 300 and self.player_x < 4:
        if self.maze[self.player_y][self.player_x + 1] != 1:
            self.player_x += 1
```

* If tilted left/right and no wall in the way, move the player.

#### ⬆️ Move Up or Down

```python
    if y_tilt < -300 and self.player_y > 0:
        if self.maze[self.player_y - 1][self.player_x] != 1:
            self.player_y -= 1
    elif y_tilt > 300 and self.player_y < 4:
        if self.maze[self.player_y + 1][self.player_x] != 1:
            self.player_y += 1
```

* If tilted forward/backward and no wall in the way, move the player.

---

### 🎯 Step 6: Check if Player Reaches the Goal

```python
def check_goal(self):
    return self.maze[self.player_y][self.player_x] == 2
```

* Returns `True` if the player is on the goal tile.

---

### 🌀 Step 7: Run the Game Loop

```python
def play(self):
    while True:
        self.move()
        self.draw()
        if self.check_goal():
            display.show(Image.HAPPY)
            break
        sleep(300)
```

* The game runs in a **loop**:

  * Move the player
  * Redraw the screen
  * If the goal is reached, show a **happy face** and stop
  * Pause briefly between movements

---

### ▶️ Step 8: Start the Game

```python
game = TiltMaze()
game.play()
```

* Creates a game object and starts it.

---

## 📝 Summary

| Symbol | Meaning     |
| ------ | ----------- |
| `0`    | Empty space |
| `1`    | Wall        |
| `2`    | Goal tile   |

| Tilt Direction | Movement                        |
| -------------- | ------------------------------- |
| Left           | Player moves left (if no wall)  |
| Right          | Player moves right (if no wall) |
| Forward        | Player moves up (if no wall)    |
| Backward       | Player moves down (if no wall)  |

---




### 4️⃣ Testing & Discussion (10–15 mins)

💬 Ask students:

* Can you solve the maze? How long does it take?
* What happens if you tilt too quickly?
* How could we make it harder?

✨ **Challenge Ideas:**

* Add a **timer** and show how fast you solved it.
* Make different maze layouts and swap them in.
* Add **traps** (cells that reset the player to start).
* Increase difficulty by requiring **fewer moves**.

---

## 🎯 Wrap-Up & Reflection

* Pupils have learned how to use the **accelerometer** to control a game.
* They explored **if statements** to check walls and goals.
* They practised **problem-solving** by navigating the maze.
* They extended learning by **designing their own maze**.

---

Would you like me to also make a **student handout version** (simplified, with just the essentials and space for them to fill in answers), or keep this as a **teacher’s guide** only?
