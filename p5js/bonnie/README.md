# Bonnie's p5 journey
---
P5js is a javascript environment for drawing, animating and interacting with your computer

---



```javascript
// We setup things here but they only happen once
// This setup creates a canvas for us to draw on
function setup() {
  createCanvas(400, 400);
  
}


// Any code put in draw will happen over and over

function draw() {
  background(220);
  
}

```
### Basic circle with fill
```javascript
// We setup things here but they only happen once
// This setup creates a canvas for us to draw on
function setup() {
  createCanvas(400, 400);
  
}


// Any code put in draw will happen over and over

function draw() {
  background(220);
  fill(255,255,255)//0-255
  circle(200,200,200)
}
```

### Load an image
Save the horse png on to your computer then upload to the sketch
```javascript
let img;

// Load the image and create a p5.Image object.
function preload() {
  img = loadImage('horse.png');
}

function setup() {
  createCanvas(800, 800);
background(180)
}

function draw(){
    // Draw the image.
  image(img, mouseX, mouseY,100,100);

}
```

You can use a button press to change images

```javascript
let img;

function preload() {
  img = loadImage("horse.png");
}

function setup() {
  createCanvas(800, 800);
  background(180);
}

function draw() {
  // Draw the image at the mouse position
  image(img, mouseX, mouseY, 100, 100);
}

function keyPressed() {
  if (key === '1') {
    img = loadImage("oreo.png");
  }
}

```
