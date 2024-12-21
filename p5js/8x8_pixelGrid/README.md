## Create your own 8x8 pixel drawings

First open up [p5js](https://editor.p5js.org/)

Delete setup and draw functions

Then copy the code below into a completely BLANK sketch

```javascript
// Define images and their colors
const slides = [
  {
    colors: {
      R: [255, 0, 0],      // Red
      C: [0, 255, 255]     // Cyan
    },
    image: [
      'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
      'R', 'C', 'C', 'C', 'C', 'C', 'C', 'R',
      'R', 'C', 'R', 'R', 'R', 'R', 'C', 'R',
      'R', 'C', 'R', 'C', 'C', 'R', 'C', 'R',
      'R', 'C', 'R', 'C', 'C', 'R', 'C', 'R',
      'R', 'C', 'R', 'R', 'R', 'R', 'C', 'R',
      'R', 'C', 'C', 'C', 'C', 'C', 'C', 'R',
      'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'
    ]
  },
  {
    colors: {
      d: [150, 128, 98],   // Brown
      c: [200, 103, 207],  // Magenta
      b: [161, 222, 158],  // Light Green
      a: [66, 99, 65],     // Dark Green
      x: [255, 255, 255]   // White
    },
    image: [
      'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
      'd', 'c', 'x', 'a', 'a', 'c', 'x', 'd',
      'a', 'c', 'c', 'a', 'b', 'c', 'c', 'a',
      'a', 'c', 'c', 'b', 'b', 'c', 'c', 'a',
      'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
      'a', 'a', 'b', 'a', 'a', 'b', 'a', 'a',
      'a', 'a', 'b', 'a', 'a', 'b', 'a', 'a',
      'b', 'b', 'b', 'a', 'a', 'b', 'b', 'b'
    ]
  },
//**************👇👇👇👇ADD YOUR CODE HERE👇👇👇👇*************
 {
  colors: {
      w: [255, 255, 255],  // white
    },
 image: [
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
    ] 
 },
];



let slideIndex = 0; // Start with the first slide
let pixelGrid;

function setup() {
  createCanvas(400, 400); // Create canvas
  noStroke();
  pixelGrid = new PixelGrid(); // Initialize the PixelGrid class
}

function draw() {
  background(0); // Black background

  // Render the current slide
  const currentSlide = slides[slideIndex];
  pixelGrid.setImage(currentSlide.image, currentSlide.colors);
  pixelGrid.drawGrid();
}

// Automatically move to the next slide every 3 seconds
setInterval(() => {
  slideIndex = (slideIndex + 1) % slides.length; // Loop through slides
}, 3000);


// PixelGrid Class
class PixelGrid {
  constructor() {
    this.gridSize = 8; // Grid size (8x8)
    this.image = [];   // Image matrix
    this.colors = {};  // Color palette
  }

  setImage(newImage, newColors) {
    this.image = newImage; // Update the image
    this.colors = newColors; // Update the colors
  }

  drawGrid() {
    let squareSize = width / this.gridSize; // Size of each square
    for (let row = 0; row < this.gridSize; row++) {
      for (let col = 0; col < this.gridSize; col++) {
        let colorKey = this.image[row * this.gridSize + col]; // Get the color key
        let color = this.colors[colorKey]; // Retrieve the corresponding RGB value
        fill(color); // Set the fill color
        rect(col * squareSize, row * squareSize, squareSize, squareSize); // Draw the square
      }
    }
  }
}
```
