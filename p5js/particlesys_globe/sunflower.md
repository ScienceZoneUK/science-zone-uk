# 🌻 Sunflower Seeds Workshop in p5.js

### 🎯 Audience: 13-year-olds

### ⏰ Duration: 1 Hour

### 💻 Tool: [p5.js Web Editor](https://editor.p5js.org/)

---

## 🚀 Workshop Overview:

In this workshop, we'll learn how nature creates beautiful patterns, specifically sunflower seed arrangements, using particles, vectors, and the Golden Angle in p5.js.

**What You'll Learn:**

- Basics of 2D drawing in p5.js
- Creating particle classes and objects
- Using vectors for positioning
- The Golden Angle and its application in nature-inspired designs

---

## 🛠 Step 1: Basic Setup (0–10 min)

**Explanation:**

- We start by setting up a basic 2D canvas.

**Code (fully commented):**

```javascript
function setup() {
  createCanvas(500, 500); // Set up a square drawing canvas
  angleMode(DEGREES); // Use degrees for easier understanding
}

function draw() {
  background(255); // White background
}
```

**Try running this!**

---

## 🧑‍💻 Step 2: Creating a Particle Class (10–20 min)

**Explanation:**

- Classes allow us to easily create and manage multiple similar objects.

**Fully commented example:**

```javascript
class Seed {
  constructor(x, y) {
    this.pos = createVector(x, y); // Store position using vectors
  }

  display() {
    fill(100, 50, 0); // Brown color for seeds
    noStroke();
    ellipse(this.pos.x, this.pos.y, 8, 8); // Draw seed as a small ellipse
  }
}

let seed;

function setup() {
  createCanvas(500, 500);
  angleMode(DEGREES);
  seed = new Seed(width / 2, height / 2); // Center seed
}

function draw() {
  background(255);
  seed.display();
}
```

**Run and experiment!**

---

## 🌻 Step 3: Golden Angle Explained (20–30 min)

**Explanation:**

- The Golden Angle (~137.5 degrees) helps evenly space elements in nature, like seeds in sunflowers.
- It ensures seeds are optimally placed to receive sunlight and nutrients.

**Code snippet to illustrate:**

```javascript
let goldenAngle = 137.5; // Golden angle
```

---




## 🌼 Step 4: Distributing Seeds Using the Golden Angle (30–45 min)

**Fully commented example:**

```javascript
let seeds = [];
let totalSeeds = 300;
let goldenAngle = 137.5;

function setup() {
  createCanvas(500, 500);
  angleMode(DEGREES);

//ADD the golden angle here
//
//


}

function draw() {
  background(255);

  for (let s of seeds) {
    s.display();
  }
}

class Seed {
  constructor(x, y) {
    this.pos = createVector(x, y);
  }

  display() {
    fill(100, 50, 0);
    noStroke();
    ellipse(this.pos.x, this.pos.y, 8, 8);
  }
}
```

# 🌻 Sunflower Seed Spiral Code Explained (p5.js)

This document explains the core code used to place sunflower seeds using vectors and the **Golden Angle** in p5.js.

---

## 🔁 Code Block

```javascript
for (let i = 0; i < totalSeeds; i++) {
  let angle = i * goldenAngle; // Rotate by golden angle each time
  let radius = sqrt(i) * 8;    // Radius grows slightly for each seed

  let x = width / 2 + radius * cos(angle);
  let y = height / 2 + radius * sin(angle);

  seeds.push(new Seed(x, y));
}
```

---

## 🧠 What This Does (Plain English)

This loop adds seeds one by one, arranging them in a spiral pattern inspired by how sunflower seeds naturally grow.

---

## 🔍 Line-by-Line Breakdown

### `for (let i = 0; i < totalSeeds; i++) {`

Runs a loop `totalSeeds` times. Each loop places one seed.

---

### `let angle = i * goldenAngle;`

Each new seed is rotated from the last by the **Golden Angle** (\~137.5°).

**Why?**

- This rotation spaces seeds evenly.
- The Golden Angle is irrational in degrees, so seeds never exactly overlap.
- Nature uses this pattern in flowers, pinecones, and more!

---

### `let radius = sqrt(i) * 8;`

Determines how far each seed is from the center.

**Why use square root?**

- Keeps seeds tightly packed in the middle.
- Gently spreads them out further as `i` increases.
- The `* 8` is a scaling factor (you can change this).

---

### `let x = width / 2 + radius * cos(angle);`

### `let y = height / 2 + radius * sin(angle);`

Converts from polar coordinates (radius + angle) to screen (x, y) coordinates.

- `width/2`, `height/2`: Center of canvas
- `cos(angle)`, `sin(angle)`: Trigonometry to find position around the circle
- This places seeds in a spiral around the center

---

### `seeds.push(new Seed(x, y));`

Creates a new `Seed` object and adds it to the list.

**Why a class?**

- It helps manage each seed as a separate object.
- Makes it easy to display, animate, or interact with each one.

---

## ✅ Summary

This pattern mimics how sunflowers grow:

- Seeds are evenly rotated by the Golden Angle
- They grow out from the center with increasing radius
- The result is a **beautiful spiral pattern** seen in nature

You just programmed nature’s math magic 🌻✨



**Run to see a sunflower seed arrangement!**

---

## 🎨 Step 5: Creative Experimentation (45–55 min)

Encourage participants to:

- Adjust the number of seeds (`totalSeeds`)
- Change seed size and colors
- Experiment with different angles and spacing

---

## 🎤 Step 6: Showcase & Discussion (55–60 min)

Participants share their designs:

- What creative patterns emerged?
- Discuss the beauty and logic of natural patterns.

Celebrate everyone's creativity and discoveries!

---

## 📝 Recap & Key Points:

- Nature-inspired coding with the Golden Angle
- Classes and vectors help manage many objects
- Creative coding lets you explore and understand natural phenomena

🎉 **Congratulations! You've successfully created sunflower seed patterns in p5.js!** 🌻🌼

