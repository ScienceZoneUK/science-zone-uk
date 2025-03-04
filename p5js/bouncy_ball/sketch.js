let vel;
let pos;
let gravity;

function setup() {
  createCanvas(400, 400);
  vel = createVector(0, 1);
  pos = createVector(200, 0);
  gravity = createVector(0.2, 0);
}

function draw() {
  background(220);
  circle(pos.x, pos.y, 50);
  pos.add(vel);
}
