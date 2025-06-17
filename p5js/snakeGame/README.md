
# 🐍 Build Your Own Snake Game in p5.js

Welcome! In this step-by-step guide, you'll learn how to build a Snake game using p5.js — starting from a single moving square to a full growing snake that eats food!

We use a teaching technique called **semantic wave pedagogy** — we start simple, go deeper, and come back up to do cool things with what we’ve learned.

---

## 🟩 Wave 1: Make the Snake Move

### 🎯 Goal
Make a square (the snake head) move using arrow keys. Wrap the logic in a class.

### ✅ Steps

1. Create a `Snake` class
2. Store position (`segments`) and movement direction (`vel`)
3. Use arrow keys to change direction
4. Move the square by adding velocity
5. Draw it on screen

### 💻 Code

```js
let snake;

function setup() {
  createCanvas(400, 400);
  frameRate(5);
  snake = new Snake();
}

function draw() {
  background(220);
  snake.update();
  snake.show();
}

function keyPressed() {
  snake.changeDirection(keyCode);
}

class Snake {
  constructor() {
    this.segments = [createVector(100, 100)];
    this.vel = createVector(20, 0);
  }

  update() {
    // Move the head
    this.segments[0].add(this.vel);

    // Wrap the head around screen edges
    let head = this.segments[0];

    if (head.x >= width) head.x = 0;
    if (head.x < 0) head.x = width - 20;
    if (head.y >= height) head.y = 0;
    if (head.y < 0) head.y = height - 20;
  }

  show() {
    fill(0);
    rect(this.segments[0].x, this.segments[0].y, 20, 20);
  }

  changeDirection(keyCode) {
    if (keyCode === RIGHT_ARROW) this.vel.set(20, 0);
    else if (keyCode === LEFT_ARROW) this.vel.set(-20, 0);
    else if (keyCode === UP_ARROW) this.vel.set(0, -20);
    else if (keyCode === DOWN_ARROW) this.vel.set(0, 20);
  }
}

```

---

## 🍎 Wave 2: Add Food

### 🎯 Goal
Place a red square (food) and detect if the snake eats it.

### ✅ Steps

1. Add a `food` variable inside the class
2. Create a method `placeFood()` to randomise its position
3. Check if the snake’s head touches the food
4. Move the food after it's eaten
5. Draw the food

### 🔍 Additions to Your Class

```js
placeFood() {
  let cols = floor(width / 20);
  let rows = floor(height / 20);
  this.food = createVector(floor(random(cols)) * 20, floor(random(rows)) * 20);
}

checkEat() {
  let head = this.segments[0];
  if (head.x === this.food.x && head.y === this.food.y) {
    console.log("Yum!");
    this.placeFood();
  }
}

showFood() {
  fill(255, 0, 0);
  rect(this.food.x, this.food.y, 20, 20);
}
```

### 🧠 In draw():

```js
snake.update();
snake.checkEat();
snake.show();
snake.showFood();
```

---

## 🐍 Wave 3: Make the Snake Grow

### 🎯 Goal
Grow the snake when it eats food.

### ✅ Steps

1. Start with 3 segments
2. When food is eaten, add a new tail segment
3. Make each segment follow the one before it

### 🔁 Updated `update()` method

```js
update() {
  for (let i = this.segments.length - 1; i > 0; i--) {
    this.segments[i] = this.segments[i - 1].copy();
  }
  this.segments[0].add(this.vel);
}
```

### 🟢 Update `checkEat()` to grow:

```js
if (head.x === this.food.x && head.y === this.food.y) {
  let tail = this.segments[this.segments.length - 1].copy();
  this.segments.push(tail);
  this.placeFood();
}
```

### 🛠 Start with 3 segments:

```js
this.segments = [
  createVector(100, 100),
  createVector(80, 100),
  createVector(60, 100)
];
```

---

## 🎉 You Did It!

Now you have:
- A moving snake 🐍
- Food to eat 🍎
- Snake that grows 🪴

From here, you can:
- Add a score
- Make the snake die if it hits itself
- Add sound or graphics

Happy coding!

---
