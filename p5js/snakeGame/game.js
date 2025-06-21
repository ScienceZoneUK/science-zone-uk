// 🐍 Snake Game Starter Code

let gridSize = 40; // Each square in our grid is 40x40 pixels
let snakeHead; // This will hold the snake's head position
let vel; // This will hold the snake's velocity (movement speed)
let snake = []; // This will become the snake's body
let food; // This will store the food location

function setup() {
  createCanvas(800, 800); // Creates a square canvas that's 800 by 800 pixels
  frameRate(3); // Slow the game down to 5 frames per second

  // 🟢 STEP 1: Start the snake head at the top-left of the grid
  snake.push(createVector(0, 0));
  snake.push(createVector(-gridSize, 0));
  snake.push(createVector(-2 * gridSize, 0));

  vel = createVector(40, 0);
  placeFood();
}

function draw() {
  background(220);

  drawGrid();

  // Move the snake: create new head
  let head = snake[0].copy();
  head.add(vel);
  snake.unshift(head); // Add new head to the front

  // Check for food collision
  let ateFood = head.x === food.x && head.y === food.y;

  if (!ateFood) {
    snake.pop(); // Remove tail unless we ate food
  } else {
    placeFood();
  }

  // Wrap around screen
  if (head.x >= width) head.x = 0;
  if (head.x < 0) head.x = width - gridSize;
  if (head.y >= height) head.y = 0;
  if (head.y < 0) head.y = height - gridSize;

  // Draw snake
  fill(0);
  for (let part of snake) {
    rect(part.x, part.y, gridSize, gridSize);
  }

  // Draw food
  fill('red');
  rect(food.x, food.y, gridSize, gridSize);

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

function keyPressed() {
  if (keyCode === RIGHT_ARROW) vel.set(gridSize, 0);
  else if (keyCode === LEFT_ARROW) vel.set(-gridSize, 0);
  else if (keyCode === UP_ARROW) vel.set(0, -gridSize);
  else if (keyCode === DOWN_ARROW) vel.set(0, gridSize);
}

function placeFood() {
  let cols = width / gridSize;
  let rows = height / gridSize;
  food = createVector(floor(random(cols)) * gridSize, floor(random(rows)) * gridSize);
}
