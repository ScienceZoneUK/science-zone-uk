🚀 Perfect choice — a **Mini Space Invaders** game for the BBC Micro:bit is a brilliant project for teaching **loops, coordinates, collision detection, and timing** in a fun arcade-style way!
Below is the full **Teacher’s Guide**, **learning objectives**, **lesson flow**, and **complete code** for a simplified, easy-to-build version.

---

# 👾 **Micro:bit Game: Space Invaders (Mini Version)**

---

## 🎯 **Learning Objectives (Bloom’s Taxonomy)**

| Bloom’s Level        | Learning Objective                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| 🔵 **Remembering**   | Pupils will be able to **recall** how to use the `display.set_pixel()` function to draw on the LED grid.   |
| 🟢 **Understanding** | Pupils will be able to **explain** how movement and position are controlled using `x` and `y` coordinates. |
| 🟡 **Applying**      | Pupils will be able to **use** loops and conditions to move a ship and shoot bullets.                      |
| 🟠 **Analysing**     | Pupils will be able to **detect** collisions between bullets and enemies.                                  |
| 🔴 **Evaluating**    | Pupils will be able to **test** and **adjust** speed and difficulty to improve gameplay.                   |
| 🟣 **Creating**      | Pupils will be able to **design** new levels or add extra enemies and effects.                             |

---

## 🕹️ **Game Description**

In this **mini Space Invaders**, the player controls a ship on the **bottom row** of the Micro:bit.
Tilt the Micro:bit **left/right** to move, and press **button A** to shoot.
A single “invader” moves across the top — if you hit it with your shot, you win!
If it reaches the edge and gets too close, you lose 👾💥

---

## ⏱️ **Lesson Flow (Teacher Guide)**

---

### 1️⃣ **Introduction (10 mins)**

💬 Ask students:

* What happens in *Space Invaders*?
* How does a player move and shoot?
* What does “collision” mean in a game?

📌 **Explain:**
We’ll make a simplified version with:

* One moving **enemy**
* One **player ship**
* A **bullet** that can be fired to destroy the invader

---

### 2️⃣ **The Problem (5 mins)**

We need a game that:

* Lets the player move left/right with tilt
* Fires bullets upward with button A
* Detects a hit when the bullet reaches the invader
* Ends with a victory or defeat message

💬 Discussion prompts:

* How can we make the invader move automatically?
* What happens when it reaches the screen edge?

---

## 🧠 **Step-by-Step Coding Guide**

---

## ✅ Step 1: Import what we need

```python
from microbit import *
import random
```

💡 **What this does:**

* `from microbit import *` gives us access to all the Micro:bit’s features — LEDs, buttons, accelerometer, etc.
* `import random` lets us create random numbers, which we’ll use to place the enemy in a random starting position.

🎓 **Think about:**
Why is random useful in games? (Answer: It makes each game different and fun!)
---

## ✅ Step 2: Set starting positions

```python
player_x = 2
player_y = 4
bullet_x = -1
bullet_y = -1
enemy_x = random.randint(0, 4)
enemy_y = 0
enemy_direction = 1
game_over = False
```

💡 **What this does:**
We’re setting up where everything starts on the LED grid (which is 5×5).

| Variable               | Meaning                                                     | Example       |
| ---------------------- | ----------------------------------------------------------- | ------------- |
| `player_x`, `player_y` | Where the player’s ship is. Starts at bottom centre.        | `(2, 4)`      |
| `bullet_x`, `bullet_y` | Where the bullet is. `-1` means “no bullet yet.”            | `( -1, -1 )`  |
| `enemy_x`, `enemy_y`   | Where the enemy is. Random x position on top row.           | `(random, 0)` |
| `enemy_direction`      | Controls if the enemy is moving right (`1`) or left (`-1`). | `1`           |
| `game_over`            | Keeps track if the game has ended.                          | `False`       |

🎮 Visual:

```
0  . . 👾 . .
1  . . . . .
2  . . . . .
3  . . . . .
4  . . 🚀 . .
```


---

## ✅ Step 3: Main game loop

```python
while not game_over:
    display.clear()
```

💡 **What this does:**
The loop keeps the game running **over and over** until `game_over = True`.
At the start of every frame, we **clear the screen** to redraw everything fresh.

🎓 **Tip:**
All games use loops — they’re what make things move!

---

## ✅ Step 4: Move player using tilt

```python
    x_reading = accelerometer.get_x()
    if x_reading < -200:
        player_x = max(0, player_x - 1)
    elif x_reading > 200:
        player_x = min(4, player_x + 1)
```

💡 **What this does:**
The Micro:bit reads how much you’re tilting it left or right.

* If you tilt **left**, the car moves left.
* If you tilt **right**, it moves right.

`max(0, …)` and `min(4, …)` stop it from going off-screen.

🎓 **Hint:**
Try printing `x_reading` to see what values you get when you tilt!

---

## ✅ Step 5: Shoot with Button A

```python
    if button_a.was_pressed() and bullet_y == -1:
        bullet_x = player_x
        bullet_y = player_y - 1
```

💡 **What this does:**
When Button A is pressed, a bullet is fired **from the player’s position**.
We only allow a new bullet if there isn’t one already (`bullet_y == -1`).

🎓 **Challenge:**
What would happen if you *removed* the `and bullet_y == -1` check?
(Hint: Too many bullets at once!)

---

## ✅ Step 6: Move bullet upward

```python
    if bullet_y >= 0:
        bullet_y -= 1
        if bullet_y < 0:
            bullet_x = -1
```

💡 **What this does:**
The bullet moves **up** one pixel each time the loop runs.
When it goes off the top (`y < 0`), it disappears — resetting `bullet_x` to `-1`.

🎓 **Coordinate reminder:**
The Micro:bit screen has (0,0) at the **top-left**, so *smaller y* means *up*.

---

## ✅ Step 7: Move enemy automatically

```python
    enemy_x += enemy_direction
    if enemy_x > 4 or enemy_x < 0:
        enemy_direction *= -1
        enemy_y += 1
```

💡 **What this does:**
The enemy slides left and right.
When it hits an edge, it:

1. Bounces back (by flipping its direction)
2. Moves **down** one row — getting closer to you!

🎓 **Hint:**
That `enemy_direction *= -1` trick just reverses direction (1 → -1 or -1 → 1).


---

## ✅ Step 8: Check for collision (bullet hits enemy)

```python
    if bullet_x == enemy_x and bullet_y == enemy_y:
        display.show(Image.HAPPY)
        display.scroll("You Win!")
        game_over = True
```

💡 **What this does:**
If the bullet’s position is the same as the enemy’s — boom! 💥
We show a happy face and scroll a victory message.

🎓 **Think about:**
This is called **collision detection** — it’s used in nearly every game.



---

## ✅ Step 9: Check for defeat (enemy reaches player)

```python
    if enemy_y == player_y:
        display.show(Image.SKULL)
        display.scroll("Game Over")
        game_over = True
```

💡 **What this does:**
If the enemy gets down to your row — you lose.
We show a skull and end the loop.

🎓 **Try changing:**
What if the enemy only has to reach *row 3*?
You could make the game harder or easier!

---

✅ **Step 10 – Draw everything**

```python
    display.set_pixel(player_x, player_y, 9)
    display.set_pixel(enemy_x, enemy_y, 5)
    if bullet_y >= 0:
        display.set_pixel(bullet_x, bullet_y, 7)

    sleep(300)
```

---

## 🧩 **Full Code**

```python
from microbit import *
import random

player_x = 2
player_y = 4
bullet_x = -1
bullet_y = -1
enemy_x = random.randint(0, 4)
enemy_y = 0
enemy_direction = 1
game_over = False

while not game_over:
    display.clear()

    # Move player with tilt
    x_reading = accelerometer.get_x()
    if x_reading < -200:
        player_x = max(0, player_x - 1)
    elif x_reading > 200:
        player_x = min(4, player_x + 1)

    # Shoot bullet
    if button_a.was_pressed() and bullet_y == -1:
        bullet_x = player_x
        bullet_y = player_y - 1

    # Move bullet up
    if bullet_y >= 0:
        bullet_y -= 1
        if bullet_y < 0:
            bullet_x = -1

    # Move enemy
    enemy_x += enemy_direction
    if enemy_x > 4 or enemy_x < 0:
        enemy_direction *= -1
        enemy_y += 1

    # Check hit
    if bullet_x == enemy_x and bullet_y == enemy_y:
        display.show(Image.HAPPY)
        display.scroll("You Win!")
        game_over = True

    # Check defeat
    if enemy_y == player_y:
        display.show(Image.SKULL)
        display.scroll("Game Over")
        game_over = True

    # Draw elements
    display.set_pixel(player_x, player_y, 9)
    display.set_pixel(enemy_x, enemy_y, 5)
    if bullet_y >= 0:
        display.set_pixel(bullet_x, bullet_y, 7)

    sleep(300)
```

---

## 🧩 **Extension Challenges**

| Challenge               | Description                                     |
| ----------------------- | ----------------------------------------------- |
| 🚀 **Speed Up**         | Make the enemy move faster each round.          |
| 🔫 **Double Fire**      | Let the player shoot two bullets at once.       |
| 👾 **Multiple Enemies** | Use a list to store several enemies.            |
| 🎶 **Sound Effects**    | Add firing and explosion sounds (Micro:bit v2). |
| ⭐ **Score**             | Count how many invaders are destroyed.          |

---

## 💬 **Reflection Questions**

* What happens if you increase or decrease the sleep time?
* How does the game detect a hit between the bullet and enemy?
* What could you add to make the game more exciting or harder?

---

## ✅ **Wrap-Up**

By the end of this activity, students will:

* Control objects with the accelerometer
* Manage multiple objects (player, bullet, enemy)
* Detect collisions and game-over conditions
* Build a playable **Space Invaders Mini Game** 🎮

---

