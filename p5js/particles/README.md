# 🐟 Particle Systems Workshop: Feed the Fish!

## 🎓 Audience
**Age:** 10-year-olds  
**Duration:** 1 Hour  
**Language:** JavaScript (p5.js)

## 🎯 Goal
Create an interactive sketch where kids feed a fish by launching food particles using code. They will:
- Learn what vectors are
- Understand how movement and gravity work
- Use classes to manage objects
- Fire particles on mouse press
- Learn how to use arrays to store multiple particles

---

## ✅ 1. Setup and Draw One Particle Using Vectors
We start by drawing one particle using a vector for position.

```js
let pos;
```
```js
function setup() {
  createCanvas(400, 400);
  pos = createVector(200, 200); // Starting position as a vector
}
```
```js
function draw() {
  background(220);
  ellipse(pos.x, pos.y, 20); // Access x and y from the vector
}
```

**Concept:**
- A vector is a way to store two values (x and y) together.
- We use `createVector(x, y)` to create it.
- We can access `pos.x` and `pos.y` to draw the particle.

**Concept:** A particle is just a small shape we can move later.

---

## ✅ 2. Make the Particle Move
We use **vectors** for movement.

```js
let pos;
```
```js
let vel;
```
```js
function setup() {
  createCanvas(400, 400);
  pos = createVector(100, 100);
  vel = createVector(2, 1);
}
```
```js
function draw() {
  background(220);
  pos.add(vel); // Position changes with velocity
  ellipse(pos.x, pos.y, 20);
}
```

**Concept:**
- `pos` is where the particle is.
- `vel` is how it moves.
- `pos.add(vel)` moves it each frame.

---

## ✅ 3. Add Gravity
We use another vector to pull the particle down:

```js
let gravity;
```
```js
function setup() {
  createCanvas(400, 400);
  pos = createVector(100, 100);
  vel = createVector(2, 0);
  gravity = createVector(0, 0.2);
}
```
```js
function draw() {
  background(220);
  vel.add(gravity); // Gravity affects velocity
  pos.add(vel);     // Velocity affects position
  ellipse(pos.x, pos.y, 20);
}
```

**Concept:** Gravity is a constant force pulling things down.

---

## ✅ 4. Create a Particle Class
We make a class to create many food particles:

```js
class Particle {
  constructor(x, y, vx, vy) {
    this.pos = createVector(x, y);
    this.vel = createVector(vx, vy);
    this.gravity = createVector(0, 0.2);
  }

  update() {
    this.vel.add(this.gravity);
    this.pos.add(this.vel);
  }

  show() {
    fill(255, 150, 150);
    noStroke();
    ellipse(this.pos.x, this.pos.y, 10);
  }
}
```

**Concept:** Classes are like cookie cutters. One class can create many particles!

---

## ✅ 5. Build the Array Step-by-Step
We need to store particles so we can update and draw them all.

**Step 1: Create an empty array**
```js
let food = []; // this will hold all the food particles
```

**Step 2: Add one particle on mouse press**
```js
function mousePressed() {
  let p = new Particle(0, 0, 3, 1); // fire from top-left
  food.push(p); // add to the array
}
```

**Step 3: Loop through the array to update and show each particle**
```js
function draw() {
  background(220);

  for (let i = 0; i < food.length; i++) {
    food[i].update();
    food[i].show();
  }
}
```

**Concept:**
- An array is like a list. Each particle goes into the list.
- We use a `for` loop to go through every item in the list and do something with it.

---

## ✅ 6. Fire Multiple Particles
Change `mousePressed()` to this:

```js
function mousePressed() {
  for (let i = 0; i < 5; i++) {
    let vx = random(2, 4);
    let vy = random(0, 2);
    let p = new Particle(0, 0, vx, vy);
    food.push(p);
  }
}
```

**Concept:** A loop creates 5 food flakes with different speeds!

---

## ✅ 7. Draw the Fish
Create a function to draw the fish:

```js
function drawFish() {
  fill(255, 150, 0);
  noStroke();
  ellipse(mouseX, height - 20, 60, 30); // fish body
  triangle(mouseX - 30, height - 20, mouseX - 45, height - 10, mouseX - 45, height - 30); // tail
  fill(0);
  ellipse(mouseX + 15, height - 25, 5); // eye
}
```

Call it at the end of `draw()`:

```js
function draw() {
  background(220);

  for (let i = 0; i < food.length; i++) {
    food[i].update();
    food[i].show();
  }

  drawFish();
}
```

**Concept:** Writing your own function helps you reuse drawing code easily. You "call" the function to use it.

---

## 📄 Complete Code

```js
let food = [];

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  for (let i = 0; i < food.length; i++) {
    food[i].update();
    food[i].show();
  }

  drawFish();
}

function mousePressed() {
  for (let i = 0; i < 5; i++) {
    let vx = random(2, 4);
    let vy = random(0, 2);
    let p = new Particle(0, 0, vx, vy);
    food.push(p);
  }
}

function drawFish() {
  fill(255, 150, 0);
  noStroke();
  ellipse(mouseX, height - 20, 60, 30);
  triangle(mouseX - 30, height - 20, mouseX - 45, height - 10, mouseX - 45, height - 30);
  fill(0);
  ellipse(mouseX + 15, height - 25, 5);
}

class Particle {
  constructor(x, y, vx, vy) {
    this.pos = createVector(x, y);
    this.vel = createVector(vx, vy);
    this.gravity = createVector(0, 0.2);
  }

  update() {
    this.vel.add(this.gravity);
    this.pos.add(this.vel);
  }

  show() {
    fill(255, 150, 150);
    noStroke();
    ellipse(this.pos.x, this.pos.y, 10);
  }
}
```

---

## 🧰 Extension Ideas
- Add a **score** when the food hits the fish
- Add a **bubble sound** when particles fire
- Add **color changes** to the fish when fed

---

## 📃 Image Placeholder
To include in your markdown folder:
```
/images/fish-diagram.png
```

You can show: fish, gravity arrow, particle trails.
