// Declare variables for shape radii
let secondsRadius;
let minutesRadius;
let hoursRadius;
let clockDiameter;

function setup() {
  createCanvas(710, 400);
  stroke(255);
  angleMode(DEGREES);

  // Set radius for each shape based on canvas dimensions
  let radius = min(width, height) / 2;
  secondsRadius = radius * 0.71;
  minutesRadius = radius * 0.6;
  hoursRadius = radius * 0.5;
  clockDiameter = radius * 1.7;

  describe('Functioning pink clock on a grey background.');
}

function draw() {
  background(230);

  // Move origin to center of canvas
  translate(width / 2, height / 2);

  // Draw the clock background
  noStroke();
  fill(244, 122, 158);
  ellipse(0, 0, clockDiameter + 25, clockDiameter + 25);
  fill(237, 34, 93);
  ellipse(0, 0, clockDiameter, clockDiameter);

  // Calculate angle for each hand
  let secondAngle=map(second(),0,60,0,360);

  

  stroke(255);

  // Second hand
  push();


  
  pop();

  // Minute hand
  push();


  
  pop();

  // Hour hand
  push();


  
  pop();

  // Tick markers around perimeter of clock
  push();
  strokeWeight(2);
  for (let ticks = 0; ticks < 60; ticks += 1) {
    point(0, -secondsRadius);
    rotate(6);
  }
  pop();
}
