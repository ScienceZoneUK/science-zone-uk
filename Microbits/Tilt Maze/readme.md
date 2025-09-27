

# 📝 Student Handout — Micro:bit Tilt Maze

---

## 🎯 Learning Goals

By the end of this session, I will be able to:

* Define what the Micro:bit accelerometer does.
* Describe how tilting controls movement.
* Use code to move a dot in a maze.
* Design my own Tilt Maze.

---

## 1️⃣ Why are Mazes Important?

💬 Think & Discuss:

* Why do people enjoy mazes?
* Where do we see mazes in everyday life?
  ✏️ Write one idea here: ______________________________

---

## 2️⃣ Problem: Tilt Maze Game

We are inventing a game for the Micro:bit!

Requirements:

* A dot starts in the **top-left** corner.
* Tilt Micro:bit to move the dot.
* Walls block movement.
* Goal is in the **bottom-right** corner.
* 🎉 When you reach the goal → show a happy face.

💬 Discuss in pairs:

* How can tilting control the dot?
* How do we know when the player has won?
  ✏️ Write your idea: ______________________________

---

## 3️⃣ Build the Game (Coding Steps)

✅ **Step 1: Show the player**

```python
from microbit import *

player_x = 0
player_y = 0

while True:
    display.clear()
    display.set_pixel(player_x, player_y, 9)
    sleep(300)
```

👉 Flash this. Do you see your player dot?

---

✅ **Step 2: Add a Maze**

```python
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 2]
]
```

👉 Walls = 1, Empty = 0, Goal = 2

---

✅ **Step 3: Tilt to Move**

```python
x_tilt = accelerometer.get_x()
y_tilt = accelerometer.get_y()
```

👉 Try tilting left, right, forward, backward. What happens?

---

✅ **Step 4: Winning!**

```python
if maze[player_y][player_x] == 2:
    display.show(Image.HAPPY)
    break
```

👉 Run and try to solve the maze. Did you win? 🎉

---

## 4️⃣ Test & Reflect

💬 Questions:

* Was it easy or hard to solve? Why?
* What happened if you tilted too fast?
* How could you make the maze harder?

✏️ Write your idea: ______________________________

---

## 5️⃣ Challenge Time 🚀

* ⏱️ Add a timer: How fast can you solve it?
* 🧩 Design your own maze (change the numbers in the grid).
* 💥 Add traps that reset the player.
* 🎶 Add sound when you win.

✏️ Draw your maze design here:

```
[ ][ ][ ][ ][ ]  
[ ][ ][ ][ ][ ]  
[ ][ ][ ][ ][ ]  
[ ][ ][ ][ ][ ]  
[ ][ ][ ][ ][ ]  
```

---

https://forms.gle/5PwVmqqebvxiws756
