# CircleShape Class

The `CircleShape` class is a versatile tool for creating smooth, curvy shapes using unevenly spaced points around a circle. This class is perfect for creative coding projects, especially when working with [p5.js](https://p5js.org/).

## Features

- Create smooth, closed shapes using cubic Bézier curves.
- Accept an array of 12 offsets to dynamically adjust point positions.
- Automatically handles tangent calculations for smooth transitions between points.
- Easily customizable for different radii and offsets.

## Installation

To use this class, download the `CircleShape.js` file and include it in your p5.js project.

[Download CircleShape.js](https://raw.githubusercontent.com/yourusername/your-repo/main/CircleShape.js)

## Usage

1. Add the `CircleShape.js` file to your p5.js project folder.
2. Include the file in your `index.html`:

```html
<script src="CircleShape.js"></script>
```

3. Create and use the class in your sketch:

### Example

```javascript
function setup() {
  createCanvas(400, 400);
  background(220);
  noFill();
  strokeWeight(2);
  stroke(0);

  // Define 12 offsets
  let offsets = [
    10, -20, 15, 5, -10, 20, -15, 25, -30, 10, -5, 15,
  ];

  // Create the CircleShape instance
  let curvyCircle = new CircleShape(width / 2, height / 2, 100, offsets);

  // Draw the shape
  curvyCircle.drawShape();
}
```

### CircleShape Class

Below is the full implementation of the `CircleShape` class. You can copy this code into a separate `CircleShape.js` file.

```javascript
class CircleShape {
  constructor(cx, cy, baseRadius, offsets) {
    this.cx = cx; // Center X
    this.cy = cy; // Center Y
    this.baseRadius = baseRadius; // Base radius of the circle
    this.offsets = offsets; // Array of 12 offsets
    this.points = []; // Points for the shape
    this.calculatePoints(); // Generate points
  }

  calculatePoints() {
    this.points = [];
    let segments = 12;
    let angleStep = TWO_PI / segments;

    for (let i = 0; i < segments; i++) {
      let angle = angleStep * i;
      let radius = this.baseRadius + (this.offsets[i] || 0); // Base radius + offset
      let x = this.cx + radius * cos(angle);
      let y = this.cy + radius * sin(angle);
      this.points.push({ x, y });
    }
  }

  drawShape() {
    beginShape();
    for (let i = 0; i < this.points.length; i++) {
      let curr = this.points[i];
      let next = this.points[(i + 1) % this.points.length]; // Wrap to the first point
      let prev = this.points[(i - 1 + this.points.length) % this.points.length]; // Wrap to the last point

      // Calculate tangent directions for control points
      let tangent1 = {
        x: (next.x - prev.x) * 0.3,
        y: (next.y - prev.y) * 0.3,
      };
      let cp1 = { x: curr.x + tangent1.x, y: curr.y + tangent1.y };

      let tangent2 = {
        x: (curr.x - next.x) * 0.3,
        y: (curr.y - next.y) * 0.3,
      };
      let cp2 = { x: next.x + tangent2.x, y: next.y + tangent2.y };

      if (i === 0) {
        vertex(curr.x, curr.y);
      }
      bezierVertex(cp1.x, cp1.y, cp2.x, cp2.y, next.x, next.y);
    }
    endShape(CLOSE);
  }
}
```

## Customization

- **Offsets**: Adjust the `offsets` array to control the irregularity of the shape.
- **Base Radius**: Change the `baseRadius` to scale the overall size of the shape.
- **Center**: Modify `cx` and `cy` to position the shape on the canvas.

## License

Feel free to use this class for personal and educational projects. If you use it in a public project, credit is appreciated!
