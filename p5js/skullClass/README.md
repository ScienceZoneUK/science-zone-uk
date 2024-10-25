
# Skull Grid Project (Detailed Steps)

This project creates a 3D grid of rotating, bouncing skulls with a neon green glow using p5.js. This file gives step-by-step instructions for setting up the `update()` and `display()` methods in the `Skull` class.

## Building the `update` and `display` Methods

### Step 3: Build the `update` Method

1. Inside **Skull.js**, in your `update` method:
   - Start by adding a line to increase the angle of rotation using the `rotationSpeed` property.
     - Code: `this.angle += this.rotationSpeed;`
       - This line increases the angle by a small amount each time `update` is called, making the skull rotate over time.

2. Add a bouncing effect to the skull’s position.
   - Choose a property like `zBounce` to control the bounce and set it to change using a math function, like sine, to make the movement smooth.
     - Example code: `this.position.z = Math.sin(this.zBounce) * 50;`
       - This line changes the skull’s `z` position up and down, creating a bouncing effect.

3. Increase `zBounce` by the `bounceSpeed` property so the bouncing continues over time.
   - Code: `this.zBounce += this.bounceSpeed;`

**Example for `update` method in Skull.js**:
```javascript
update() {
  // Step 1: Rotate the skull by changing its angle
  this.angle += this.rotationSpeed;

  // Step 2: Bounce the skull up and down using a math function
  this.position.z = Math.sin(this.zBounce) * 50;

  // Step 3: Increment zBounce to keep the bounce effect moving
  this.zBounce += this.bounceSpeed;
}
```

---

### Step 4: Build the `display` Method

1. In **Skull.js**, start the `display` method:
   - Use `push()` at the beginning and `pop()` at the end to isolate transformations (like position and rotation) to just this skull.
     - Code: `push();` and `pop();`

2. Move the skull to its `position` using `translate`:
   - Code: `translate(this.position.x, this.position.y, this.position.z);`
     - This line moves each skull to its unique `x`, `y`, and `z` position.

3. Rotate the skull to the angle set in the `update` function:
   - Code: `rotateY(this.angle);` (or use `rotateX` if you want rotation on multiple axes)

4. Display the skull model with the `model()` function:
   - Code: `model(skullModel);`

**Example for `display` method in Skull.js**:
```javascript
display() {
  // Step 1: Start transformation isolation
  push();
  
  // Step 2: Move skull to its position in 3D space
  translate(this.position.x, this.position.y, this.position.z);
  
  // Step 3: Rotate the skull by the angle set in update()
  rotateY(this.angle);
  
  // Step 4: Display the skull model
  model(skullModel);
  
  // Step 5: End transformation isolation
  pop();
}
```

---

## Recap

With `update()` and `display()` complete:
- `update()` controls rotation and bouncing for each skull.
- `display()` positions, rotates, and shows each skull model on the screen.
