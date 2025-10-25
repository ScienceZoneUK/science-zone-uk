---

# 🌀 Mouse Maze — p5.js Handout

---

## 🎯 **Goal**

Build a **maze game** where you guide your mouse through a path to the goal —
**but don’t touch the walls**, or you’ll have to start over! 🧱🐭🎯

---

## 🧠 **What You’ll Learn**

✅ How to **draw shapes** to make a maze
✅ How to use the **mouse position** (`mouseX`, `mouseY`)
✅ How to **detect collisions** (when the mouse hits a wall)
✅ How to make a **win message** when you reach the goal

---

## 🧩 **New Coding Words**

| Word                | What It Means                                                         |
| ------------------- | --------------------------------------------------------------------- |
| **mouseX / mouseY** | The current position of your mouse on the screen.                     |
| **rect()**          | Draws a rectangle (used for maze walls).                              |
| **fill()**          | Sets the color of shapes.                                             |
| **if**              | Checks if something is true, then runs some code.                     |
| **dist()**          | Measures distance between two points (great for detecting closeness). |

---

## 💻 **Step-by-Step Instructions**

### 🟢 **Step 1 — Set Up Your Canvas**

Start your maze game with this:

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
```

🧠 **What’s happening:**
This creates a blank grey background where we’ll draw the maze and goal.

---

### 🧱 **Step 2 — Draw Your Maze Walls**

Let’s make some simple walls using `rect()`:

```javascript
function draw() {
  background(220);

  fill(100); // wall color
  noStroke();

  // walls (x, y, width, height)
  rect(0, 0, 400, 20);    // top wall
  rect(0, 380, 400, 20);  // bottom wall
  rect(0, 0, 20, 400);    // left wall
  rect(380, 0, 20, 400);  // right wall
  rect(100, 100, 200, 20);
  rect(100, 100, 20, 200);
  rect(280, 180, 20, 200);
}
```

🪄 You can add more walls to make your maze harder!

---

### 🎯 **Step 3 — Add a Start and Goal**

Let’s make the start green and the goal red:

```javascript
// Start area
fill(0, 255, 0);
rect(30, 30, 40, 40);

// Goal area
fill(255, 0, 0);
rect(330, 330, 40, 40);
```

---

### 🐭 **Step 4 — Add the Player (the Mouse)**

Draw a circle at your mouse’s position:

```javascript
fill(50, 50, 255);
ellipse(mouseX, mouseY, 20, 20);
```

Now you can move your mouse around the maze!

---

### 🚨 **Step 5 — Detect Collisions with Walls**

We’ll restart the maze if the mouse touches a wall.
Add this *after* you draw the player:

```javascript
if (
  (mouseX > 100 && mouseX < 300 && mouseY > 100 && mouseY < 120) ||  // top wall
  (mouseX > 100 && mouseX < 120 && mouseY > 100 && mouseY < 300) ||  // left wall
  (mouseX > 280 && mouseX < 300 && mouseY > 180 && mouseY < 380)
) {
  background(255, 0, 0);
  fill(255);
  textSize(32);
  text("Oops! You hit a wall!", 60, 200);
  noLoop(); // stops the game
}
```

🧩 **What’s happening:**
If the mouse enters the area where a wall is drawn, the game stops and shows an “Oops!” message.

---

### 🏁 **Step 6 — Check for Winning**

Now let’s make the player *win* when reaching the goal:

```javascript
if (mouseX > 330 && mouseX < 370 && mouseY > 330 && mouseY < 370) {
  background(0, 255, 0);
  fill(0);
  textSize(32);
  text("You Win! 🎉", 120, 200);
  noLoop(); // stop the game
}
```

---

### 🔄 **Step 7 — Restart the Game**

Let’s restart when the player clicks the mouse:

```javascript
function mousePressed() {
  loop(); // start again
}
```

Now you can click to play again after winning or hitting a wall!

---

## 🕹️ **Play Your Game!**

✅ Move your mouse carefully through the maze.
✅ Avoid the gray walls.
✅ Reach the red goal square to win!
✅ Click to restart if you lose.

---

## 🌈 **Bonus Challenges**

1. 🌀 Design your own maze layout with more walls!
2. 🎨 Add background colors or images.
3. 💥 Add a sound when you hit a wall or win (with `p5.sound`).
4. ⏱️ Add a timer or score counter!
5. 🐱 Replace the mouse circle with a cute character (like a cat or robot).

---

## 💬 **Reflection**

* How does the computer know when you hit a wall?
* What would happen if you made the maze walls thinner or thicker?
* How could you make the game harder or easier?

---
