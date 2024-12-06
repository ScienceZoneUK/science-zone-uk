
# **Workshop: Creating a Snowflake Animation with p5.js**

In this workshop, you'll create a dynamic snowflake animation using p5.js. We'll start with a single snowflake and gradually move into creating a class for cleaner, reusable code.

---

## **Step 1: Set Up the Project**
1. Open the p5.js web editor at [editor.p5js.org](https://editor.p5js.org).
2. Create a new sketch and save it as `SingleSnowflake`.

---

## **Step 2: Create a Single Snowflake**
1. Write the following code to draw a single snowflake:

```javascript
function setup() {
  createCanvas(800, 800); // Set canvas size
  background(0);          // Black background for visibility
}

function draw() {
  background(0);          // Clear the screen each frame
  translate(width / 2, height / 2); // Center the snowflake

  stroke(255);           // White stroke for the snowflake
  noFill();
  beginShape();
  for (let i = 0; i < 6; i++) { // Draw a 6-point snowflake
    let angle = TWO_PI / 6 * i;
    let x = cos(angle) * 50; // Adjust the size of the snowflake
    let y = sin(angle) * 50;
    vertex(x, y);
    vertex(0, 0); // Add a line back to the center
  }
  endShape(CLOSE);
}
```

2. Run the code to show a stationary snowflake in the center.

---

## **Step 3: Animate the Snowflake**
1. Add movement by controlling the snowflake's vertical position with a `y` variable:

```javascript
let y = 0;

function setup() {
  createCanvas(800, 800);
  background(0);
}

function draw() {
  background(0);
  translate(width / 2, y); // Move the snowflake vertically

  stroke(255);
  noFill();
  beginShape();
  for (let i = 0; i < 6; i++) {
    let angle = TWO_PI / 6 * i;
    let x = cos(angle) * 50;
    let y = sin(angle) * 50;
    vertex(x, y);
    vertex(0, 0);
  }
  endShape(CLOSE);

  y += 2; // Move the snowflake down
  if (y > height) { // Reset when it moves out of bounds
    y = 0;
  }
}
```

---

## **Step 4: Introduce Classes**
1. Add a new tab in the editor called `Snowflake.js`.
2. Define a `Snowflake` class to encapsulate snowflake properties and behavior:

```javascript
class Snowflake {
  constructor(x, y, size) {
    this.x = x;           // x-position
    this.y = y;           // y-position
    this.size = size;     // size of the snowflake
    this.speed = 2;       // Falling speed
  }

  move() {
    this.y += this.speed;
    if (this.y > height) {
      this.y = 0;         // Reset when it goes out of bounds
    }
  }

  display() {
    push();
    translate(this.x, this.y);
    stroke(255);
    noFill();
    beginShape();
    for (let i = 0; i < 6; i++) {
      let angle = TWO_PI / 6 * i;
      let x = cos(angle) * this.size;
      let y = sin(angle) * this.size;
      vertex(x, y);
      vertex(0, 0);
    }
    endShape(CLOSE);
    pop();
  }
}
```

---

## **Step 5: Use the Class**
1. Go back to the main tab and use the `Snowflake` class:

```javascript
let snowflake;

function setup() {
  createCanvas(800, 800);
  background(0);
  snowflake = new Snowflake(width / 2, 0, 50); // Create a single snowflake
}

function draw() {
  background(0);

  snowflake.move();    // Move the snowflake
  snowflake.display(); // Display the snowflake
}
```

---

## **Step 6: Add Multiple Snowflakes**
1. Use an array to create multiple snowflakes:

```javascript
let snowflakes = [];

function setup() {
  createCanvas(800, 800);
  background(0);

  // Create multiple snowflakes
  for (let i = 0; i < 50; i++) {
    let x = random(width);
    let y = random(height);
    let size = random(10, 50);
    snowflakes.push(new Snowflake(x, y, size));
  }
}

function draw() {
  background(0);

  // Update and display all snowflakes
  for (let flake of snowflakes) {
    flake.move();
    flake.display();
  }
}
```

---

## **Step 7: Add Interactivity**
1. Add mouse interaction to spawn more snowflakes:

```javascript
function mousePressed() {
  let size = random(10, 50);
  snowflakes.push(new Snowflake(mouseX, mouseY, size));
}
```

---

## **Step 8: Experiment and Extend**
1. Encourage students to:
   - Experiment with colors, shapes, and speeds.
   - Add gravity-like effects or wind using horizontal movement.

By the end of this workshop, you'll have a dynamic snowflake animation and a solid understanding of using classes in p5.js!
