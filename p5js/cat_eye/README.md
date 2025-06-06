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

### ✅ Step 2: One Eye Follows the Mouse

- Wrap the eye into a class
- Use vector math to move the pupil

```js
let eye;

function setup() {
  createCanvas(400, 400);
  eye = new Eye(200, 200, 60);
}

function draw() {
  background(220);
  eye.update();
  eye.display();
}

class Eye {
  constructor(x, y, r) {
    this.pos = createVector(x, y);
    this.r = r;
  }

  update() {
    this.dir = p5.Vector.sub(createVector(mouseX, mouseY), this.pos);
    this.dir.setMag(this.r / 2);
  }

  display() {
    fill(255);
    stroke(0);
    ellipse(this.pos.x, this.pos.y, this.r);
    fill(0);
    ellipse(this.pos.x + this.dir.x, this.pos.y + this.dir.y, this.r / 3);
  }
}
```
---

## 🧿 How It Works – Eye Class & Vectors (Simple Explanation)

### 🧠 What is a Class?

A **class** is like a blueprint for an object. In this case, we made a class called `Eye`. Every time we want to create a new cat eye, we use that blueprint.

Each `Eye`:
- Knows where it lives (`x`, `y`)
- Knows how big it is (`r`)
- Has functions (`update()` and `display()`) to follow the mouse and draw itself

### 🧠 What is a Vector?

A **vector** is like an arrow that tells us:
- **Where to go** (direction)
- **How far to go** (magnitude or length)

We use vectors to find the direction from the center of the eye to your mouse.

```js
this.dir = p5.Vector.sub(createVector(mouseX, mouseY), this.pos);
```

This says:  
“Make a vector from the eye to the mouse.”  
Then we **shrink** that arrow so the pupil doesn’t fly out of the eye:

```js
this.dir.setMag(this.r / 2);
```

That way, the **black pupil stays inside the eye** but still points toward your mouse.


---
