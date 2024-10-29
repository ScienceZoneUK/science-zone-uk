
# p5.js 3D Terrain Generation

This project is a simple p5.js 3D terrain generation sketch where you can create dynamic landscapes using Perlin noise. The terrain will scroll continuously, and users can modify the terrain in real-time using keyboard controls.

## Getting Started

### 1. Setup

1. Open the p5.js Web Editor: https://editor.p5js.org/
2. Click "New Sketch" to start a new project.
3. Replace the content of the `sketch.js` file with the following code:

```javascript
// Terrain grid variables
let cols, rows;
let scale = 20;    // Size of each grid cell
let w = 1400;      // Width of the terrain
let h = 1000;      // Height of the terrain
let flying = 0;    // Controls the moving effect

// 2D array to store terrain heights
let terrain = [];

// Function to initialize the terrain array
function initializeTerrain() {
  for (let x = 0; x < cols; x++) {
    terrain[x] = [];
    for (let y = 0; y < rows; y++) {
      terrain[x][y] = 0; // Set default height to 0
    }
  }
}

// Function to generate terrain heights using Perlin noise
function generateTerrain() {
  flying -= 0.05;
  let yOff = flying;

  for (let y = 0; y < rows; y++) {
    let xOff = 0;
    for (let x = 0; x < cols; x++) {
      terrain[x][y] = map(noise(xOff, yOff), 0, 1, -100, 100);
      xOff += 0.1;
    }
    yOff += 0.1;
  }
}

// Function to render the terrain
function renderTerrain() {
  rotateX(PI / 3);
  translate(-w / 2, -h / 2);

  for (let y = 0; y < rows - 1; y++) {
    beginShape(TRIANGLE_STRIP);
    for (let x = 0; x < cols; x++) {
      let terrainColor;
      if (terrain[x][y] < 0) {
        terrainColor = color(0, 0, 255);
      } else if (terrain[x][y] < 50) {
        terrainColor = color(0, 255, 0);
      } else {
        terrainColor = color(100, 100, 100);
      }
      fill(terrainColor);
      stroke(0);

      vertex(x * scale, y * scale, terrain[x][y]);
      vertex(x * scale, (y + 1) * scale, terrain[x][y + 1]);

      if (terrain[x][y] > 50) {
        push();
        translate(x * scale, y * scale, terrain[x][y]);
        drawTree();
        pop();
      }
    }
    endShape();
  }
}

// Function to draw a simple tree
function drawTree() {
  fill(139, 69, 19);
  noStroke();
  box(2, 10, 2);

  fill(34, 139, 34);
  translate(0, -6, 0);
  sphere(5);
}

// Function to handle user controls
function handleControls() {
  if (keyIsPressed) {
    if (keyCode === UP_ARROW) {
      scale += 1;
    } else if (keyCode === DOWN_ARROW) {
      scale = max(5, scale - 1);
    } else if (keyCode === LEFT_ARROW) {
      flying -= 0.01;
    } else if (keyCode === RIGHT_ARROW) {
      flying += 0.01;
    } else if (key === 'S' || key === 's') {
      saveTerrain();
    }
  }
}

// Function to save the terrain as an image
function saveTerrain() {
  saveCanvas('myTerrain', 'png');
}

// p5.js setup function
function setup() {
  createCanvas(1000, 1000, WEBGL);
  cols = w / scale;
  rows = h / scale;

  initializeTerrain();
}

// p5.js draw function
function draw() {
  background(200, 200, 255);
  stroke(0);
  noFill();

  handleControls();
  generateTerrain();
  renderTerrain();
}
```

4. Once you paste the code, hit the **Play** button to run the sketch.

### 2. Controls

- **Up Arrow:** Increase grid size (zoom in).
- **Down Arrow:** Decrease grid size (zoom out).
- **Left Arrow:** Slow down terrain movement.
- **Right Arrow:** Speed up terrain movement.
- **S Key:** Save the terrain as an image (PNG).

### 3. Features

- **Dynamic Terrain**: The terrain is generated using Perlin noise, making it appear natural and fluid.
- **Modular Code**: The code is organized into functions, making it easy to modify and extend.
- **Interactive Controls**: Modify terrain size and speed with keyboard controls.
- **Save Terrain**: Press 'S' to save the current view of the terrain as a PNG image.

---

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code.

