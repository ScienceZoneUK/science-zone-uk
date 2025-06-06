# 🐱 Cat Eyes That Follow Your Mouse – p5.js Workshop (Ages 13+)

Welcome to the **p5.js Cat Eyes Workshop**! In this fun and creative coding session, you’ll learn how to use **vectors** to make spooky **cat eyes** that follow your mouse around the screen. 😺

---

## 🎯 What You'll Learn

- How to use `createVector()` and `p5.Vector.sub()` in p5.js
- How to make objects (eyes!) that follow your mouse
- How to use classes to create reusable code
- How to build a grid of animated eyes

---

## 🧱 Workshop Steps

### ✅ Step 1: A Line Follows the Mouse

- Learn the basics of vectors
- Use `createVector()` to find direction
- Draw a line from the center to your mouse

```js
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let origin = createVector(width / 2, height / 2);
  let mouse = createVector(mouseX, mouseY);
  let dir = p5.Vector.sub(mouse, origin);
  dir.setMag(50);

  strokeWeight(4);
  stroke(0);
  line(origin.x, origin.y, origin.x + dir.x, origin.y + dir.y);
}
```

---
