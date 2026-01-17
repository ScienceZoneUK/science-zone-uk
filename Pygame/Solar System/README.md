# 🌍 Lesson 3 – Textured Solar System 

**Make real planets with images AND a spinning sun!**

By the end of this session, I will be able to:

* Load images as **textures**
* Wrap textures around spheres
* Make planets **orbit**
* Make the **sun spin**
* Build a mini **solar system**

---

# Step 1 – Imports & Setup

```python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
```

### What this does:

* Pygame = window & input
* OpenGL = 3D drawing
* GLU = sphere tools

---

# Step 2 – Rotation Variables

```python
sun_angle = 0
earth_angle = 0
mars_angle = 0
```

### What this does:

* These numbers control **movement**
* Bigger number = faster spin

---

# Step 3 – Load Texture Function

```python
def load_texture(filename):
    textureSurface = pygame.image.load(filename)
    textureData = pygame.image.tostring(textureSurface, "RGB", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB,
        width, height, 0,
        GL_RGB, GL_UNSIGNED_BYTE, textureData
    )

    return texID
```

### What this does:

* Loads an image file
* Sends it to OpenGL
* Turns it into a **texture ID**
* That ID is used to paint planets 🎨

---

# Step 4 – Draw Textured Planet

```python
def draw_textured_planet(radius, texID):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texID)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    glRotatef(-90, 1, 0, 0)
    gluSphere(quadric, radius, 40, 40)

    glDisable(GL_TEXTURE_2D)
```

### What this does:

* Turns textures ON
* Attaches the image
* Draws a sphere
* Rotates it upright (fixes poles!)
* Turns textures OFF

---

# Step 5 – Build the Solar System

```python
def SolarSystem():
    global earth_angle, mars_angle, sun_angle

    # SUN
    glPushMatrix()
    glRotatef(sun_angle, 0, 1, 0)
    draw_textured_planet(1, sun_tex)
    glPopMatrix()

    # EARTH
    glPushMatrix()
    glRotatef(earth_angle, 0, 1, 0)
    glTranslatef(3, 0, 0)
    draw_textured_planet(0.5, earth_tex)
    glPopMatrix()

    # MARS
    glPushMatrix()
    glRotatef(mars_angle, 0, 1, 0)
    glTranslatef(5, 0, 0)
    draw_textured_planet(0.4, mars_tex)
    glPopMatrix()

    earth_angle += 1
    mars_angle += 0.5
    sun_angle += 0.3
```

### What this does:

* Sun spins in place ☀️
* Earth goes around sun 🌍
* Mars goes around sun 🔴
* Each planet has its own speed

---

# Step 6 – Main Program

```python
def main():
    global sun_tex, earth_tex, mars_tex

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Textured Solar System")

    gluPerspective(45, display[0]/display[1], 0.1, 50)
    glTranslatef(0, 0, -12)
    glEnable(GL_DEPTH_TEST)

    sun_tex = load_texture("sun.jpg")
    earth_tex = load_texture("earth.jpg")
    mars_tex = load_texture("mars.jpg")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        SolarSystem()
        pygame.display.flip()

    pygame.quit()
```

---

# Step 7 – Start Program

```python
if __name__ == "__main__":
    main()
```

---

# 🧠 Key Concepts

| Concept    | Meaning         |
| ---------- | --------------- |
| Texture    | Image skin      |
| Sphere     | Planet          |
| Orbit      | Go around       |
| Spin       | Rotate          |
| Angle      | Movement number |

---

# 🚀 Easy Challenges

1. Speed up Earth

```python
earth_angle += 5
```

2. Slow sun

```python
sun_angle += 0.1
```

3. Change planet size

```python
draw_textured_planet(0.8, earth_tex)
```

4. Swap textures

* Make Mars look like Earth 😆

---

# 🌟 Medium Challenges

* Add a **Moon**
* Make Saturn (big!)
* Add stars background
