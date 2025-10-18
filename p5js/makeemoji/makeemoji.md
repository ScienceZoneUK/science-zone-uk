# 😀 Make Your Own Emoji — p5.js Handout

---

## 🎯 **Goal**

Create your very own emoji face that **changes expressions and colors** when you press keys on your keyboard!

You’ll make your emoji **happy**, **sad**, **surprised**, or **angry** — and then customize it with your own ideas.

---

## 🧰 **You’ll Need**

* A computer with internet access
* Go to 👉 [https://editor.p5js.org](https://editor.p5js.org)
* A love for silly faces 😜

---

## 🧠 **What You’ll Learn**

✅ Drawing shapes (`ellipse`, `arc`, `line`)
✅ Changing colors (`fill`, `color`)
✅ Using **variables** to store information
✅ Responding to **key presses** (`keyPressed()`)
✅ Making choices with **if / else** statements

---

## 💻 **Step-by-Step Instructions**

### 🟡 **Step 1 — Set Up Your Canvas**

Every p5.js sketch starts with `setup()` and `draw()`.
Type this in first:

```javascript
function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(255);
}
```

📝 **What’s happening:**
You made a white drawing area that updates every frame.

---

### 😀 **Step 2 — Draw the Face**

Now, add a yellow face to the middle:

```javascript
fill(255, 220, 0); // yellow
noStroke();
ellipse(width / 2, height / 2, 250, 250);
```

🪞 **Try This:**
Change the last two numbers (`250, 250`) to make your emoji bigger or smaller!

---

### 👀 **Step 3 — Add Eyes**

Add these lines below your face:

```javascript
fill(0);
ellipse(width / 2 - 50, height / 2 - 40, 30, 30);
ellipse(width / 2 + 50, height / 2 - 40, 30, 30);
```

📝 **What’s happening:**
The eyes are two black circles placed to the left and right of the face center.

---

### 😁 **Step 4 — Add a Mouth**

Use an **arc** to make a smile:

```javascript
noFill();
stroke(0);
strokeWeight(8);
arc(width / 2, height / 2 + 40, 120, 80, 0, PI);
```

🪞 **Try This:**
Change the numbers and see what happens to your smile!

---

### 🎭 **Step 5 — Add Moods**

Now, let’s make the face **change moods** when you press a key!

At the top of your sketch, add:

```javascript
let faceColor;
let mood = "happy";
```

Inside `setup()`:

```javascript
faceColor = color(255, 220, 0);
```

Then update your `draw()` like this:

```javascript
function draw() {
  background(255);
  fill(faceColor);
  noStroke();
  ellipse(width / 2, height / 2, 250, 250);

  fill(0);
  ellipse(width / 2 - 50, height / 2 - 40, 30, 30);
  ellipse(width / 2 + 50, height / 2 - 40, 30, 30);

  noFill();
  stroke(0);
  strokeWeight(8);

  if (mood === "happy") {
    arc(width / 2, height / 2 + 40, 120, 80, 0, PI);
  } else if (mood === "sad") {
    arc(width / 2, height / 2 + 90, 120, 80, PI, TWO_PI);
  } else if (mood === "surprised") {
    noStroke();
    fill(0);
    ellipse(width / 2, height / 2 + 50, 40, 60);
  } else if (mood === "angry") {
    line(width / 2 - 70, height / 2 - 70, width / 2 - 30, height / 2 - 50);
    line(width / 2 + 70, height / 2 - 70, width / 2 + 30, height / 2 - 50);
    arc(width / 2, height / 2 + 60, 120, 80, PI, TWO_PI);
  }
}
```

---

### 🎨 **Step 6 — Change Mood with Keys**

Add this function at the bottom of your sketch:

```javascript
function keyPressed() {
  if (key === '1') {
    mood = "happy";
    faceColor = color(255, 220, 0);
  } else if (key === '2') {
    mood = "sad";
    faceColor = color(100, 150, 255);
  } else if (key === '3') {
    mood = "surprised";
    faceColor = color(255, 230, 150);
  } else if (key === '4') {
    mood = "angry";
    faceColor = color(255, 100, 100);
  }
}
```

Now press:

* `1` → 😀 Happy
* `2` → 😢 Sad
* `3` → 😮 Surprised
* `4` → 😡 Angry

---

## 🌈 **Bonus Challenges**

✅ Add a tongue when the emoji is happy.
✅ Add sunglasses when pressing the **S** key.
✅ Add a random color mode when pressing the **spacebar**.
✅ Draw extra shapes (hearts, eyebrows, hats, etc.)!

---

## 💬 **Reflection**

* What happens if you change the face color?
* How does the code know which mood to draw?
* Can you make your emoji blink or wink?

---

Would you like me to turn this into a **printable PDF handout** (with spaces for notes and little icons next to each step)? It’s great for classroom or at-home use.
