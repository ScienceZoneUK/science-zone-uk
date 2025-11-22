
# 🌼🌿 **Interactive Garden — p5.js Handout**

---

## 🎯 **Goal**

Create your own **digital garden** where you can **click to plant flowers**, **grow grass**, **add bugs**, and watch your world come alive!

---

## 🧠 **What You’ll Learn**

* How to use **mousePressed()** to make things happen
* How to **store and draw many flowers**
* How to use **random()** for fun surprises
* How to build your own little ecosystem

---

## 🧩 **New Coding Words**

| Word               | Meaning                                                        |
| ------------------ | -------------------------------------------------------------- |
| **mousePressed()** | Runs when you click the mouse.                                 |
| **array**          | A list to store all your flowers.                              |
| **object**         | A little bundle of information (like a flower’s size & color). |
| **random()**       | Picks a random number — great for nature!                      |

---

# 💻 **Step-by-Step Instructions**

---

## 🌱 **Step 1 — Set Up Your Canvas**

```javascript
let flowers = [];

function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(120, 200, 120); // green grass
}
```

---

## 🌷 **Step 2 — Add a Flower When You Click**

Under your code, add:

```javascript
function mousePressed() {
  let newFlower = {
    x: mouseX,
    y: mouseY,
    size: random(20, 50),
    petalColor: color(random(255), random(255), random(255)),
    centerColor: color(255, 200, 0)
  };

  flowers.push(newFlower);
}
```

🌼 Each click adds a new flower to your garden!

---

## 🌸 **Step 3 — Draw All the Flowers**

Inside `draw()`, add:

```javascript
for (let i = 0; i < flowers.length; i++) {
  let f = flowers[i];

  // petals
  fill(f.petalColor);
  ellipse(f.x - f.size/2, f.y, f.size, f.size);
  ellipse(f.x + f.size/2, f.y, f.size, f.size);
  ellipse(f.x, f.y - f.size/2, f.size, f.size);
  ellipse(f.x, f.y + f.size/2, f.size, f.size);

  // center
  fill(f.centerColor);
  ellipse(f.x, f.y, f.size, f.size);
}
```

Now your flowers appear **every time you click**!

---

## 🐞 **Step 4 — Add a Cute Bug That Moves**

Add this near the top:

```javascript
let bugX = 0;
let bugY = 350;
```

Then in `draw()`:

```javascript
// draw the bug
fill(0);
ellipse(bugX, bugY, 20, 15);
ellipse(bugX - 10, bugY, 10, 8);

// move the bug
bugX += 1;

if (bugX > width) {
  bugX = -20; // loop around
}
```

Now a little bug crawls across the garden!

---

## ☀️ **Step 5 — Add a Sun in the Sky**

Add this to `draw()`:

```javascript
fill(255, 255, 0);
ellipse(350, 50, 60, 60);
```

---

# 🕹️ **Try It Out**

* Click anywhere to plant a flower
* Watch the bug walk by
* Enjoy your growing digital garden!

---

# 🌈 **Bonus Challenges**

1. **🌻 Make special flowers** with different shapes
2. **🐝 Add a flying bee** that moves in wiggly motion
3. **💧 Add falling raindrops** to water the plants
4. **🌙 Add night mode** when you press a key
5. **🌳 Add trees**, mushrooms, or rocks
6. **🎵 Add relaxing garden sounds** (with `p5.sound`)

---

# 💬 Reflection Questions

* What kinds of objects did you add to your garden?
* How does `mousePressed()` make your program interactive?
* What random features made your garden look more natural?

---

