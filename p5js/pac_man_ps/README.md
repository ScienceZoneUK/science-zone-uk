
# p5.js Particle Project with PNG Images

Welcome! This project will show you how to create a particle effect using PNG images with p5.js in the online editor.

## What You'll Need

1. Internet connection.
2. Some PNG images saved as `img1.png`, `img2.png`, and so on.

## Step-by-Step Guide

### Step 1: Open the p5.js Web Editor

1. Go to [p5.js Web Editor](https://editor.p5js.org/cuvner/sketches/XHyurb_yN).
2. Click **Sign In** if you want to save your work. If not, you can continue without signing in.

### Step 2: Set Up the Code

1. **Create a New Project** by clicking on **New** in the editor.
2. Open the file named `sketch.js` in the left-hand menu.

### Step 3: Copy and Paste the Code

#### 1. Clear any existing code in `sketch.js`.
#### 2. Copy the code below and paste it into `sketch.js`.

```javascript
let particles = [];
let images = [];
let imageCount = 3;  // Adjust this to the number of images you have

function preload() {
  for (let i = 1; i <= imageCount; i++) {
    let img = loadImage(`images/img${i}.png`);
    images.push(img);
  }
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
}

function draw() {
  background(32);
  
  for (let particleA of particles) {
    let accelerationX = 0;
    let accelerationY = 0;

    for (let particleB of particles) {
      if (particleA !== particleB) {
        let distanceX = particleB.position.x - particleA.position.x;
        let distanceY = particleB.position.y - particleA.position.y;
        let distance = sqrt(distanceX * distanceX + distanceY * distanceY);
        distance = max(distance, 1);
        let force = (distance - 320) * particleB.mass / distance;
        accelerationX += force * distanceX;
        accelerationY += force * distanceY;
      }
    }

    particleA.velocity.x = particleA.velocity.x * 0.99 + accelerationX * particleA.mass;
    particleA.velocity.y = particleA.velocity.y * 0.99 + accelerationY * particleA.mass;
  }

  for (let particle of particles) {
    particle.updatePosition();
    particle.display();
  }
}

class Particle {
  constructor(x, y, mass) {
    this.position = createVector(x, y);
    this.velocity = createVector(0, 0);
    this.mass = mass;
    this.image = random(images);
  }

  updatePosition() {
    this.position.add(this.velocity);
    if (this.position.x > width) this.position.x = 0;
    if (this.position.x < 0) this.position.x = width;
    if (this.position.y > height) this.position.y = 0;
    if (this.position.y < 0) this.position.y = height;
  }

  display() {
    let size = this.mass * 500;
    image(this.image, this.position.x, this.position.y, size, size);
  }
}

function addNewParticle() {
  let mass = random(0.003, 0.03);
  let newParticle = new Particle(mouseX, mouseY, mass);
  particles.push(newParticle);
}

function mouseClicked() {
  addNewParticle();
}

function mouseDragged() {
  addNewParticle();
}
```

### Step 4: Download the Images

To use the images for the particles:

1. Download the project repository using the **Download** button.
2. Unzip the folder. Inside, you’ll find example images named `img1.png`, `img2.png`, etc.
3. Upload these images to your project in the p5.js editor by clicking the **Upload File** button.

### Step 5: Run the Code

1. Click the **Play** button at the top of the editor.
2. Now, click or drag on the canvas to add particles made from your images!

---

### How It Works

- **`preload()`**: This function loads the images into memory before starting.
- **`setup()`**: Sets up the canvas where particles move around.
- **`draw()`**: Continuously updates the positions and forces of each particle.
- **`Particle` Class**: This class holds data about each particle and controls how it moves and displays.

---

### Example

Check out a live example of a particle project [here](https://editor.p5js.org/cuvner/full/7n9lmC4YC).

Enjoy exploring your particle project and feel free to try new images or change the movement rules to see what happens!

