# 🌍 Particle Globe Workshop in p5.js

### 🎯 Audience: 13-year-olds

### ⏰ Duration: 1 Hour

### 💻 Tool: [p5.js Web Editor](https://editor.p5js.org/)

---

## 🚀 Workshop Overview:

This workshop will guide you step-by-step through creating a beautiful spinning globe of particles using p5.js, a beginner-friendly JavaScript library.

**What You'll Learn:**

- Basics of 3D drawing in p5.js
- Creating classes and objects
- Even distribution of particles (Golden Angle)
- Vectors and spherical coordinates

---

## 🛠 Step 1: Basic 3D Sphere (0–10 min)

**Explanation:**

- We start by creating a simple 3D sphere.
- WEBGL mode allows 3D drawing.

**Code (fully commented):**

```javascript
function setup() {
  createCanvas(400, 400, WEBGL); // Enable 3D drawing
}

function draw() {
  background(0); // Black background
  noStroke();    // No outlines
  fill(100, 150, 255); // Light-blue sphere

  sphere(100); // Sphere with radius 100 pixels
}
```

**Try running this!**

---

## 🧑‍💻 Step 2: Making a Particle Class (10–25 min)

**Explanation:**

- Classes help us reuse code easily.
- Create one particle and then many particles.

**Fully commented example:**

```javascript
let particle;

function setup() {
  createCanvas(400, 400, WEBGL);
  noStroke();
  fill(255, 100, 100);

  // Create a particle at position (x,y,z)
  particle = new Particle(100, 0, 0);
}

function draw() {
  background(0);

  rotateY(frameCount * 0.01); // Slowly rotate view

  particle.display(); // Display our particle
}

// Particle class definition
class Particle {
  constructor(x, y, z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  display() {
    push(); // Save the current drawing state
    translate(this.x, this.y, this.z); // Move to particle position
    sphere(10); // Draw particle as a sphere
    pop();  // Restore previous drawing state
  }
}
```

**Run and experiment!**

---

## 🌻 Step 3: Distributing Particles Evenly (Golden Angle) (25–40 min)

**Explanation (easy):**

- To spread particles evenly on a globe, we use nature's trick: the Golden Angle.
- We place particles evenly vertically and rotate each slightly.

**Fully commented example:**

```javascript
let particles = [];
let totalParticles = 200;
let globeRadius = 150;

function setup() {
  createCanvas(500, 500, WEBGL);
  noStroke();
  fill(150, 255, 100);

  let offset = 2 / totalParticles; // Vertical spacing
  let increment = PI * (3 - sqrt(5)); // Golden angle (~137.5 degrees)

  for (let i = 0; i < totalParticles; i++) {
    let y = ((i * offset) - 1) + (offset / 2); // Even vertical position
    let phi = acos(y); // Convert vertical position to latitude
    let theta = increment * i; // Longitude, rotated by golden angle

    // Convert spherical to cartesian coordinates
    let x = globeRadius * sin(phi) * cos(theta);
    let z = globeRadius * sin(phi) * sin(theta);
    let py = globeRadius * cos(phi);

    particles.push(new Particle(x, py, z));
  }
}

function draw() {
  background(0);

  rotateY(frameCount * 0.005);
  rotateX(frameCount * 0.002);

  for (let p of particles) {
    p.display();
  }
}

// Particle class
class Particle {
  constructor(x, y, z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  display() {
    push();
    translate(this.x, this.y, this.z);
    sphere(3);
    pop();
  }
}
```

**Run and observe your beautiful particle globe!**

---

## 🎨 Step 4: Experimentation (40–55 min)

Encourage participants to:

- Change particle colors (fill values)
- Adjust particle size (`sphere()`)
- Change total number of particles (`totalParticles`)
- Adjust globe radius (`globeRadius`)
- Play with rotation speeds

**Example (color changing):**

```javascript
fill(150 + 100 * sin(frameCount * 0.05), 255, 200);
```

---

## 🎤 Step 5: Showcase & Discussion (55–60 min)

Invite participants to show their screens:

- What did they create?
- What did they enjoy most?
- Any challenges they faced?

Celebrate everyone's unique creations!

---

## 📝 Recap & Key Points:

- Classes help reuse and organize code.
- Golden angle evenly distributes particles.
- Vectors and spherical coordinates place particles in 3D.
- Experimenting helps creativity!

🎉 **Congratulations! You've successfully created a Particle Globe in p5.js!** 🚀🌍

