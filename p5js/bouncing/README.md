# 🏀 Bouncing Ball Workshop — Follow-Along (13 Steps)

**Goal:** Make a ball fall, bounce, and stop, just like in real life.  
Computers don’t know gravity, floors, or bouncing — we’ll teach them step by step.  

![bouncing ball](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjBza3NmYzhra2piYW9meWo1bWswMTdvNmd4bjZjaWEzNWE1MWtnOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GGjE4LAJ2uzGiwdk55/giphy.gif)

---

## Step 1: Add the variables  
💡 *Context:* These go **at the very top of your sketch**, before `setup()`.  

```javascript
// TOP of sketch
let x = 200;     
let y = 0;       
let balSize = 50;
let vel = 0;     
let gravity = 0.981; 
let bounceFactor = 0.95; 
let sT = 0.01;   
```

---

## Step 2: Create the canvas  
💡 *Context:* The canvas goes inside the `setup()` function.  

```javascript
// inside setup()
function setup() {
  createCanvas(400, 400);
}
```

---

## Step 3: Make a draw loop  
💡 *Context:* The `draw()` function runs over and over. Add it **below `setup()`**.  

```javascript
// after setup()
function draw() {
  background(220); // Clear screen each frame
}
```

---

## Step 4: Add gravity  
💡 *Context:* Gravity goes **at the top of `draw()`**, so it updates every frame.  

```javascript
// inside draw(), near the top
vel += gravity;
```

---

## Step 5: Update position  
💡 *Context:* After adding gravity, update the ball’s position.  

```javascript
// inside draw(), after gravity
y += vel;
```

---

## Step 6: Draw the ball  
💡 *Context:* After updating position, draw the ball.  

```javascript
// inside draw(), after updating position
circle(x, y, balSize);
```

---

## Step 7: Add the ground  
💡 *Context:* Still inside `draw()`, after drawing the ball, check if the ball hits the bottom.  

```javascript
// inside draw(), after drawing the ball
if (y + balSize / 2 >= height) {
  y = height - balSize / 2;
  vel = -vel;
}
```

---

## Step 8: Lose energy when bouncing  
💡 *Context:* Add this inside the ground check, so it happens only on bounce.  

```javascript
// inside draw(), inside the ground check
vel *= -bounceFactor;
```

---

## Step 9: Stop tiny jitter  
💡 *Context:* Also inside the ground check, after applying bounce.  

```javascript
// inside draw(), inside the ground check
if (abs(vel) < sT) {
  vel = 0;
}
```

---

## Step 10: Add a trail  
💡 *Context:* Change the background line in `draw()`.  

```javascript
// replace background(220) with:
background(220, 20);
```

---

## Step 11: Reset the ball  
💡 *Context:* This goes **after `draw()`**, as a separate function.  

```javascript
// after draw()
function mousePressed() {
  y = 0;
  vel = 0;
}
```

---

## Step 12: Experiment!  
💡 *Context:* Try changing numbers **at the top of the sketch**:  
- `gravity = 0.3` → Moon bounce 🌕  
- `bounceFactor = 0.8` → Squishy ball 🏐  
- `bounceFactor = 0.99` → Super bouncy ball 🏀  

---

## Step 13: Stretch goal  
💡 *Context:* Balls can roll sideways too. At the **top of the sketch**, create:  

```javascript
let vx = 2;
```

Then inside `draw()`, update and bounce off the sides:  

```javascript
x += vx;

if (x - balSize / 2 <= 0 || x + balSize / 2 >= width) {
  vx = -vx;
}
```

---

# ✅ Complete Code (Steps 1–11)

Here’s the full working sketch you’ll have at the end of Step 11:

```javascript
// STEP 1: Variables
let x = 200;     
let y = 0;       
let balSize = 50;
let vel = 0;     
let gravity = 0.981; 
let bounceFactor = 0.95; 
let sT = 0.01;   

// STEP 2: Setup
function setup() {
  createCanvas(400, 400);
}

// STEP 3: Draw loop
function draw() {
  // STEP 10: Background with trail
  background(220, 20);

  // STEP 4: Gravity
  vel += gravity;

  // STEP 5: Update position
  y += vel;

  // STEP 6: Draw ball
  circle(x, y, balSize);

  // STEP 7: Ground + STEP 8: Bounce + STEP 9: Stop jitter
  if (y + balSize / 2 >= height) {
    y = height - balSize / 2;
    vel *= -bounceFactor;

    if (abs(vel) < sT) {
      vel = 0;
    }
  }
}

// STEP 11: Reset ball
function mousePressed() {
  y = 0;
  vel = 0;
}
```

---

✨ Congratulations! You’ve taught the computer about **gravity, velocity, bouncing, and stopping**. Now it’s your turn to experiment and make it your own.
