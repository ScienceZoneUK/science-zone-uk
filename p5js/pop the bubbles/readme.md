# 🫧 Pop the Bubbles — p5.js Handout

---

## 🎯 **Goal**

Make a game where colorful bubbles **float up the screen**, and you **pop them by clicking** on them! 💥
You’ll get to practice creating multiple objects and interacting with the mouse.

---

## 🧠 **What You’ll Learn**

✅ How to **draw circles that move**
✅ How to use **variables** to remember positions
✅ How to use **arrays** to store many bubbles
✅ How to check if the mouse is **touching a bubble**
✅ How to **remove bubbles** when popped

---

## 🧩 **New Coding Words**

| Word         | What It Means                                                                |
| ------------ | ---------------------------------------------------------------------------- |
| **array**    | A list that can hold many things (like many bubbles).                        |
| **object**   | A group of variables that describe one thing (like one bubble’s x, y, size). |
| **for loop** | A way to repeat code for each item in a list.                                |
| **dist()**   | Measures the distance between two points — perfect for checking clicks.      |

---

## 💻 **Step-by-Step Instructions**

### 🟢 **Step 1 — Set Up Your Canvas**

Start by making your drawing area:

```javascript
let bubbles = [];

function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(100, 150, 255); // light blue like water
}
```

---

### 🔵 **Step 2 — Make a Bubble**

Add a function that creates one bubble:

```javascript
function makeBubble(x, y, size) {
  return { x: x, y: y, size: size };
}
```

🧩 This creates a little “bubble object” that remembers where it is and how big it is.

---

### ⚪ **Step 3 — Add Some Bubbles**

Inside `setup()`, create a few random bubbles:

```javascript
for (let i = 0; i < 10; i++) {
  let x = random(width);
  let y = random(height, height + 200); // start off screen
  let size = random(20, 50);
  bubbles.push(makeBubble(x, y, size));
}
```

---

### 🫧 **Step 4 — Draw and Move the Bubbles**

Inside your `draw()` function, add this **loop**:

```javascript
for (let i = 0; i < bubbles.length; i++) {
  let b = bubbles[i];
  fill(255, 255, 255, 150);
  stroke(255);
  ellipse(b.x, b.y, b.size);

  // move upward
  b.y -= 1;

  // when bubble goes off top, reset to bottom
  if (b.y < -b.size) {
    b.y = height + b.size;
    b.x = random(width);
  }
}
```

📝 **What’s happening:**
Each bubble floats up the screen. When it leaves the top, it reappears at the bottom.

---

### 💥 **Step 5 — Pop Bubbles with the Mouse**

Now let’s make them *pop*!
Add this function at the bottom of your code:

```javascript
function mousePressed() {
  for (let i = bubbles.length - 1; i >= 0; i--) {
    let b = bubbles[i];
    let d = dist(mouseX, mouseY, b.x, b.y);
    if (d < b.size / 2) {
      // remove the bubble when clicked
      bubbles.splice(i, 1);
    }
  }
}
```

🧩 **dist()** measures how close your mouse is to the bubble’s center.
If you’re close enough (inside the circle), the bubble disappears!

---

### 🎨 **Step 6 — Add Some Sparkle (Optional)**

Change the fill color so each bubble gets a random tint:

```javascript
fill(random(200, 255), random(200, 255), 255, 150);
```

Try putting that **inside your loop** before `ellipse()` — now your bubbles sparkle with color!

---

## 🕹️ **Play Your Game!**

✅ Press ▶ to run your sketch.
✅ Watch bubbles float up.
✅ Click them to pop — gone! 💨

---

## 🌈 **Bonus Challenges**

1. 🎵 Play a *“pop”* sound when you click a bubble (with p5.sound library).
2. 💯 Add a **score counter** that goes up every time you pop one.
3. 🔁 Make **new bubbles appear** after some disappear.
4. 🌊 Add **wavy movement** (make them move left and right a bit).

---

## 💬 **Reflection**

* How does the computer know when you click a bubble?
* What happens if you change how fast the bubbles move?
* Can you make a giant “Pop All” button that clears them all?

---
