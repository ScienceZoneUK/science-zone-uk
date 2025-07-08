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

  for (let i = 0; i < totalSeeds; i++) {
    let angle = i * goldenAngle; // Rotate by golden angle each time
    let radius = sqrt(i) * 8; // Radius grows slightly for each seed

    let x = width / 2 + radius * cos(angle);
    let y = height / 2 + radius * sin(angle);

    seeds.push(new Seed(x, y));
  }
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

