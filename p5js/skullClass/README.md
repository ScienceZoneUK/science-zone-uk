
# Skull Grid Project

This project creates a 3D grid of rotating, bouncing skulls with a neon green glow using p5.js. The code demonstrates how to use classes in p5.js, with the `Skull` class in a separate file from the main sketch.

## Project Setup

### Step 1: Set Up the Project Folder and Files

1. Create a new folder called `skullGridProject`.
2. Inside this folder, create three files:
   - `index.html` (to set up the p5.js environment)
   - `sketch.js` (the main file to run the p5.js code)
   - `Skull.js` (to store the `Skull` class code)

---

### Step 2: Set Up the `index.html` File

1. Open **index.html**.
2. Inside the file:
   - Add the HTML structure with `<html>`, `<head>`, and `<body>` tags.
   - Inside `<head>`, add a `<script>` tag to link the p5.js library.
   - Inside `<body>`, add `<script>` tags to link `Skull.js` and `sketch.js` in the correct order.

Example code for `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Skull Grid</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
</head>
<body>
  <!-- Link the Skull class file -->
  <script src="Skull.js"></script>
  <!-- Link the main sketch file -->
  <script src="sketch.js"></script>
</body>
</html>
```

---

### Step 3: Create the `Skull` Class in `Skull.js`

1. Open **Skull.js**.
2. In this file:
   - Define a **class** called `Skull`.
   - Inside the class, create a **constructor** with `x` and `y` as inputs, setting up `position`, `rotationSpeed`, and `bounceSpeed` for each skull.
   - Write an **update** function that changes the skull's rotation and bounce.
   - Write a **display** function that draws the skull on the screen.

Example code snippet for `Skull.js`:

```javascript
class Skull {
  constructor(x, y) {
    this.position = { x: x, y: y };  // Set the position
    this.rotationSpeed = 0.03;       // Set a rotation speed
    this.bounceSpeed = 0.05;         // Set a bounce speed
  }

  update() {
    // Imagine this rotates and bounces the skull
  }

  display() {
    // Imagine this displays the skull model
  }
}
```

---

### Step 4: Write the Main Code in `sketch.js`

1. Open **sketch.js**.
2. In this file:
   - Define variables for the skull model, an array for skulls, and layout values.
   - Write a **preload** function to load the skull model file.
   - Write a **setup** function to create the canvas and add skulls to a grid.
   - Write a **draw** function to update and display each skull.

Example code snippet for `sketch.js`:

```javascript
let skullModel; // This variable will hold the 3D model
let skulls = []; // This array will hold all the skulls

function preload() {
  skullModel = loadModel('tinker.obj'); // Load the skull model before setup
}

function setup() {
  createCanvas(windowWidth, windowHeight, WEBGL); // Create a 3D canvas
  for (let i = 0; i < 5; i++) { // Loop to create rows
    for (let j = 0; j < 5; j++) { // Loop to create columns
      skulls.push(new Skull(i * 100, j * 100)); // Add a new skull to the array
    }
  }
}

function draw() {
  background(0); // Clear the screen to black
  for (let skull of skulls) {
    skull.update(); // Move the skull
    skull.display(); // Show the skull
  }
}
```

---

### Step 5: Run the Program

1. Open `index.html` in a web browser to see your 3D skull grid animation.

### Project Summary

- **index.html**: Links all files and loads p5.js.
- **Skull.js**: Defines the `Skull` class, managing each skull’s behavior.
- **sketch.js**: Contains the main code for setup, drawing, and updating the grid of skulls.

Now you have a 3D animation using a class in a separate file, showing a grid of skulls with movement and a neon green glow!

