let skullModel;
let skulls = [];
let cols, rows;
let spacing = 100;

function preload() {
  // Load the skull 3D model
  skullModel = loadModel('tinker.obj');
}

function setup() {
  createCanvas(windowWidth, windowHeight, WEBGL);
  cols = floor(width / spacing);
  rows = floor(height / spacing);
  
  // Create a grid of Skull objects
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      let x = (i - cols / 2) * spacing;
      let y = (j - rows / 2) * spacing;
      skulls.push(new Skull(x, y));
    }
  }
}

function draw() {
  background(0);
  lights();
  
  // Apply neon green lighting effect
  ambientLight(0, 255, 0);
  directionalLight(0, 255, 0, 0, 0, -1);

  // Update and display each skull
  for (let skull of skulls) {
    skull.update();
    skull.display();
  }
}

class Skull {
  constructor(x, y) {
    this.position = createVector(x, y, random(-100, 100));
    this.rotationSpeed = random(0.01, 0.05);
    this.bounceSpeed = random(0.5, 2);
    this.angle = 0;
    this.zBounce = random(PI);
  }

  update() {
    // Rotate the skull
    this.angle += this.rotationSpeed;
    
    // Apply bouncing effect
    this.position.z = sin(this.zBounce) * 50;
    this.zBounce += this.bounceSpeed * 0.02;
  }

  display() {
    push();
    translate(this.position.x, this.position.y, this.position.z);
    rotateX(this.angle);
    rotateY(this.angle);
    model(skullModel);
    pop();
  }
}
