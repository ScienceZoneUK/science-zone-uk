Here’s a **student-friendly study guide** for a **Magic Paintbrush** project in **p5.js**, designed especially for a **7-year-old** beginner.
It mixes fun explanations, learning goals, and a simple code example — great for a classroom or at-home coding session.

---

## 🪄 Magic Paintbrush — Study Guide

### 🎯 **Goal**

Make a program that lets you **paint with your mouse**.
When you move the mouse, it draws colorful dots that change color each time — just like painting magic sparkles on the screen!

---

### 🧠 **What You’ll Learn**

* How to **set up a p5.js sketch** (`setup()` and `draw()` functions)
* How to **draw shapes** with `ellipse()`
* How to **use the mouse position** (`mouseX`, `mouseY`)
* How to **change colors** randomly with `random()`
* How to **make your own art!**

---

### 🧩 **New Coding Words**

| Word                   | What It Means                                                 |
| ---------------------- | ------------------------------------------------------------- |
| **setup()**            | Runs once at the beginning — good for setting up your canvas. |
| **draw()**             | Runs over and over — makes animation and painting possible.   |
| **ellipse()**          | Draws a circle or oval.                                       |
| **mouseX**, **mouseY** | Tell the computer where your mouse is.                        |
| **fill()**             | Changes the color used to fill shapes.                        |
| **random()**           | Picks a random number.                                        |

---

### 💻 **Step-by-Step Instructions**

1. **Start your sketch**
   Go to [editor.p5js.org](https://editor.p5js.org) and make a new sketch.

2. **Add this code:**

   ```javascript
   function setup() {
     createCanvas(400, 400);  // Create a drawing area
     background(255);          // White background
   }

   function draw() {
     // Pick a random color
     let r = random(255);
     let g = random(255);
     let b = random(255);
     fill(r, g, b);

     // No outline for our brush dots
     noStroke();

     // Draw a circle at the mouse position
     ellipse(mouseX, mouseY, 20, 20);
   }
   ```

3. **Click “Play” ▶**
   Move your mouse around the screen — ta-da! You’re painting with rainbow colors!

---

### 🎨 **Bonus Challenges**

Try these ideas after you get it working:

* 🖱️ Paint **only when the mouse is pressed** (`if (mouseIsPressed) { ... }`)
* 🌈 Make your paintbrush **bigger or smaller** using keys
* ✨ Add a **clear button** to start fresh (use `background(255)`)
* 🌟 Make sparkles fade slowly with `background(255, 10)` inside `draw()`

---

### 🗒️ **Reflection Questions**

1. What happens if you change the size of the circle?
2. What happens if you change the background color?
3. How can you make your paintbrush leave a trail that fades away?

---

