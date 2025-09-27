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

✅ **Step 3.1: Setup & Player Start**

```python
from microbit import *

player_x = 0
player_y = 0

while True:
    display.clear()
    display.set_pixel(player_x, player_y, 9)  # Draw player
    sleep(300)
```

✅ **Step 3.2: Add a Maze**

```python
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 2]
]

for y in range(5):
    for x in range(5):
        if maze[y][x] == 1:
            display.set_pixel(x, y, 3)   # wall = dim
        elif maze[y][x] == 2:
            display.set_pixel(x, y, 7)   # goal = bright
```

✅ **Step 3.3: Tilt to Move**

```python
x_tilt = accelerometer.get_x()
y_tilt = accelerometer.get_y()

if x_tilt < -300 and player_x > 0 and maze[player_y][player_x - 1] != 1:
    player_x -= 1
elif x_tilt > 300 and player_x < 4 and maze[player_y][player_x + 1] != 1:
    player_x += 1

if y_tilt < -300 and player_y > 0 and maze[player_y - 1][player_x] != 1:
    player_y -= 1
elif y_tilt > 300 and player_y < 4 and maze[player_y + 1][player_x] != 1:
    player_y += 1
```

✅ **Step 3.4: Winning the Game**

```python
if maze[player_y][player_x] == 2:
    display.show(Image.HAPPY)
    break
```

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
