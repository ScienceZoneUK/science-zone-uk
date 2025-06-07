# 🧭 Vectors for Young Coders! (Ages 9–11)

Welcome to this creative coding workshop using **p5.js**!  
We'll learn how **vectors** help us draw, follow the mouse, and make fun interactive sketches — all using **arrows and math** in disguise!

---

## 🧠 What Is a Vector?

A **vector** is like a magic arrow that tells you:

- 🧭 **Where to go** (direction)
- 📏 **How far to go** (length, called magnitude)

In p5.js, we use vectors to **combine X and Y into one smart object**. This makes it super easy to move things, point them, or follow something like your mouse.

---

## 💡 Why Use Vectors?

- Easier to move things on screen
- Makes direction, distance, and pointing simple
- Used in games, motion, bouncing, following, and rotation!

---

## ✏️ Step-by-Step Vector Sketches

### 🔹 Step 1: Draw a Simple Line (No Vectors Yet)

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  // Draw a line from point A to B using x and y
  let x1 = 100;
  let y1 = 100;
  let x2 = 300;
  let y2 = 300;

  strokeWeight(4);
  stroke(0);
  line(x1, y1, x2, y2);
}
```

---

### 🔹 Step 2: Use Vectors to Draw the Same Line

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  // Create smart points using vectors
  let start = createVector(100, 100);
  let end = createVector(300, 300);

  strokeWeight(4);
  stroke(0);
  line(start.x, start.y, end.x, end.y);
}
```

---

### 🔹 Step 3: Line Follows the Mouse

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let start = createVector(width / 2, height / 2);
  let end = createVector(mouseX, mouseY);

  strokeWeight(4);
  line(start.x, start.y, end.x, end.y);
}
```

Now the line **follows your mouse** like it's alive!

---

### 🔹 Step 4: Show Vector Length (Magnitude)

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let start = createVector(width / 2, height / 2);
  let mouse = createVector(mouseX, mouseY);
  let dir = p5.Vector.sub(mouse, start); // direction vector
  let distance = dir.mag();              // length of the vector

  strokeWeight(4);
  line(start.x, start.y, mouse.x, mouse.y);

  fill(0);
  noStroke();
  textSize(16);
  text("Distance: " + nf(distance, 1, 2), 10, 20);
}
```

---

### 🔹 Step 5: Fixed-Length Line That Points at Mouse

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let start = createVector(width / 2, height / 2);
  let mouse = createVector(mouseX, mouseY);

  let dir = p5.Vector.sub(mouse, start); // direction
  dir.setMag(100);                       // fixed length

  let end = p5.Vector.add(start, dir);   // new end point

  strokeWeight(4);
  line(start.x, start.y, end.x, end.y);
}
```

Even if the mouse is far away, the line stays **100 pixels long** — like a compass needle!

---

### 🔹 Step 6: Grid of Tiny Lines

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let spacing = 40;

  for (let x = 0; x < width; x += spacing) {
    for (let y = 0; y < height; y += spacing) {
      strokeWeight(2);
      line(x, y, x + 10, y); // short horizontal line
    }
  }
}
```

---

### 🔹 Step 7: Grid of Lines That Follow the Mouse

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  let spacing = 40;

  for (let x = 0; x < width; x += spacing) {
    for (let y = 0; y < height; y += spacing) {

      let start = createVector(x, y);
      let target = createVector(mouseX, mouseY);
      let dir = p5.Vector.sub(target, start);
      dir.setMag(20);

      let end = p5.Vector.add(start, dir);

      stroke(0);
      strokeWeight(2);
      line(start.x, start.y, end.x, end.y);
    }
  }
}
```

Now you have a magical **field of lines that all point at your mouse**! 🎯

---

## 🧪 Workshop Summary

| Step | What You Learn                        |
|------|----------------------------------------|
| 1    | Basic line with x, y coordinates       |
| 2    | Use vectors to store points            |
| 3    | Make line follow your mouse            |
| 4    | Measure vector length with `.mag()`    |
| 5    | Fix vector length with `.setMag()`     |
| 6    | Create a grid with `for` loops         |
| 7    | Make each grid line follow the mouse   |

---

## 🎉 Now You're a Vector Wizard!

Keep going! Try:
- Turning lines into arrows
- Adding color based on direction
- Making tentacles or hair follow your mouse!

Happy coding! 🧑‍💻✨
