# 🐍 Snake Game Workshop (Ages 9+)

A fun, hands-on project using p5.js to build the classic Snake game while learning about programming concepts through clear steps and questions.

---

## ✅ Step 1: Draw the Grid and Snake Head

**Goal:** Create the canvas, show the grid, and place the snake’s head.

🧠 _Big Idea:_ The canvas is made of little squares — we will move the snake one square at a time.    

Lets start by thinking about the game snake, who has played it?    
Update you p5 sketch with this full code and don't forget to call the function.            

```js
// 🐍 Snake Game Starter Code

function setup() {
  createCanvas(800, 800); // Creates a square canvas that's 800 by 800 pixels
  frameRate(5);           // Slow the game down to 5 frames per second
}

function draw() {
  background(220); // Light gray background


// Call the drawGrid() function

}


// 🟢 STEP 1: Draw the grid using horizontal and vertical lines
function drawGrid() {
  for (let x = 0; x < width; x += gridSize) {
    for (let y = 0; y < height; y += gridSize) {
      noFill();
      stroke(200); // Light gray grid lines
      rect(x, y, gridSize, gridSize);
    }
  }
}

```

NOw lets add the snake head, delete all your previous code and paste this:     

```js
// 🐍 Snake Game Starter Code

let gridSize = 40; // Each square in our grid is 40x40 pixels
let snakeHead;     // This will hold the snake's head position
let vel;           // This will hold the snake's velocity (movement speed)
let snake = [];    // This will become the snake's body
let food;          // This will store the food location

function setup() {
  createCanvas(800, 800); // Creates a square canvas that's 800 by 800 pixels
  frameRate(5);           // Slow the game down to 5 frames per second

  // 🟢 STEP 1: Start the snake head at the top-left of the grid
  snakeHead = createVector(0, 0);
}

function draw() {
  background(220); // Light gray background

  // 🟢 STEP 1: Draw the snake head
  fill(0); // Black fill for the snake
  rect(snakeHead.x, snakeHead.y, gridSize, gridSize);

  // 🟢 STEP 1: Show the grid to help us see movement steps
  drawGrid();

  // ⏩ STEP 2: Move the snake head using a velocity (coming soon)

  // ⏩ STEP 3: Add arrow key controls (coming soon)

  // ⏩ STEP 4: Wrap around the edges of the screen (coming soon)

  // ⏩ STEP 5: Store the snake body in a list (coming soon)

  // ⏩ STEP 6: Spawn food and eat it to grow (coming soon)
}

// 🟢 STEP 1: Draw the grid using horizontal and vertical lines
function drawGrid() {
  for (let x = 0; x < width; x += gridSize) {
    for (let y = 0; y < height; y += gridSize) {
      noFill();
      stroke(200); // Light gray grid lines
      rect(x, y, gridSize, gridSize);
    }
  }
}

```

**Ask:**
- What is the size of each square?
- Where does the snake start?
- Can you change where the snake head appears?

---

## ✅ Step 2: Move the Snake in One Direction

**Goal:** Make the snake move automatically in one direction using a velocity vector.

🧠 _Big Idea:_ A **velocity** is like an arrow showing where and how fast to move.    

At the top add:
```js
let vel;
```
In setup add these
```js
  vel = createVector(gridSize, 0); // Move right
  frameRate(5); // Slow it down
```
In draw add:
```js
  snakeHead.add(vel); // Move the snake head
```

**Ask:**
- What happens if you change vel to move up?
- What direction is (20, 0)?

---

## ✅ Step 3: Use Arrow Keys to Change Direction

**Goal:** Use arrow keys to steer the snake.

🧠 _Big Idea:_ We change the direction of velocity when a key is pressed.    

At the bottom add this whole new function:
```js
function keyPressed() {
  if (keyCode === RIGHT_ARROW) vel.set(gridSize, 0);
  else if (keyCode === LEFT_ARROW) vel.set(-gridSize, 0);
  else if (keyCode === UP_ARROW) vel.set(0, -gridSize);
  else if (keyCode === DOWN_ARROW) vel.set(0, gridSize);
}
```

**Ask:**
- Which way is (-gridSize, 0)?
- What happens if you press left and then right?

---

## ✅ Step 4: Wrap the Snake Around the Screen

**Goal:** Make the snake appear on the other side when it reaches the edge.

🧠 _Big Idea:_ We check if the snake went off the canvas, and wrap it around.    

In draw add the wrap logic:

```js
  if (snakeHead.x >= width) snakeHead.x = 0;
  if (snakeHead.x < 0) snakeHead.x = width - gridSize;
  if (snakeHead.y >= height) snakeHead.y = 0;
  if (snakeHead.y < 0) snakeHead.y = height - gridSize;

```

**Ask:**
- What happens when snakeHead.x is too big?
- What does snakeHead.x = 0 do?

---

## ✅ Step 5: Store the Snake Body

**Goal:** Track the snake’s body with an array. Add a new head, remove the tail.

🧠 _Big Idea:_ We use an **array** to store body parts.     

At the top add this:    
```js
let snake = [];
```
In setup add the 3 segments:     
```js
  snake.push(createVector(0, 0));
  snake.push(createVector(-gridSize, 0));
  snake.push(createVector(-2 * gridSize, 0));
```

In draw add the snake movement logic:     
```
  let head = snake[0].copy();
  head.add(vel);
  snake.unshift(head);  // Add new head
  snake.pop();          // Remove tail
```
We need to change how we draw the snake, we are now drawing the array that holds the snake segments:      
```js
  for (let part of snake) {
    rect(part.x, part.y, gridSize, gridSize);
  }
```

**Ask:**
- What does .unshift() mean?
- Why do we .pop() the last piece?

---

## ✅ Step 6: Add Food and Eat It to Grow

**Goal:** Spawn food. If snake touches it, grow by not removing the tail.

🧠 _Big Idea:_ If head position matches food, we keep the tail and move the food.      

At the bottom lets add a function to spawn food:     
```js
function placeFood() {
  let cols = width / gridSize;
  let rows = height / gridSize;
  food = createVector(floor(random(cols)) * gridSize, floor(random(rows)) * gridSize);
}
```
In draw lets add a square at the food location
```js
  fill('red');
  rect(food.x, food.y, gridSize, gridSize);

```

In draw above the food square add the ate food check positions:      
```js

  let ateFood = head.x === food.x && head.y === food.y;
```
In draw lets now check if food was not eaten, if it was add a body segment:         
```js
  if (!ateFood) {
    snake.pop(); // Remove tail only if no food
  } else {
    placeFood();
  }
```



**Ask:**
- What does placeFood() do?
- Why do we not pop when food is eaten?

---

## ✅ Step 7: Review – How Each Part Moves

🧠 _Big Idea:_ Each frame:
- A new head is created using velocity.
- It is added to the front.
- The last segment is removed (unless eating).

**Ask:**
- Can you explain how the body grows?
- Can you explain the order of .unshift() and .pop()?

---
