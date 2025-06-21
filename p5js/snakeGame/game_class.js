let game;

function setup() {
  createCanvas(800, 800);
  frameRate(3);
  game = new SnakeGame();
}

function draw() {
  game.update();
  game.show();
}

function keyPressed() {
  game.handleInput(keyCode);
}

class SnakeGame {
  constructor() {
    this.gridSize = 40;
    this.snake = [
      createVector(0, 0),
      createVector(-this.gridSize, 0),
      createVector(-2 * this.gridSize, 0)
    ];
    this.vel = createVector(this.gridSize, 0);
    this.placeFood();
  }

  update() {
    background(220);
    this.drawGrid();

    // Move the snake
    let head = this.snake[0].copy();
    head.add(this.vel);
    this.snake.unshift(head);

    // Check for food
    let ateFood = head.x === this.food.x && head.y === this.food.y;
    if (!ateFood) {
      this.snake.pop();
    } else {
      this.placeFood();
    }

    // Wrap around screen
    if (head.x >= width) head.x = 0;
    if (head.x < 0) head.x = width - this.gridSize;
    if (head.y >= height) head.y = 0;
    if (head.y < 0) head.y = height - this.gridSize;
  }

  show() {
    // Draw snake
    fill(0);
    for (let part of this.snake) {
      rect(part.x, part.y, this.gridSize, this.gridSize);
    }

    // Draw food
    fill('red');
    rect(this.food.x, this.food.y, this.gridSize, this.gridSize);
  }

  handleInput(keyCode) {
    if (keyCode === RIGHT_ARROW) this.vel.set(this.gridSize, 0);
    else if (keyCode === LEFT_ARROW) this.vel.set(-this.gridSize, 0);
    else if (keyCode === UP_ARROW) this.vel.set(0, -this.gridSize);
    else if (keyCode === DOWN_ARROW) this.vel.set(0, this.gridSize);
  }

  placeFood() {
    let cols = width / this.gridSize;
    let rows = height / this.gridSize;
    this.food = createVector(
      floor(random(cols)) * this.gridSize,
      floor(random(rows)) * this.gridSize
    );
  }

  drawGrid() {
    for (let x = 0; x < width; x += this.gridSize) {
      for (let y = 0; y < height; y += this.gridSize) {
        noFill();
        stroke(200);
        rect(x, y, this.gridSize, this.gridSize);
      }
    }
  }
}
