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
