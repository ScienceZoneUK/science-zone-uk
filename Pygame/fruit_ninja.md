# 🍉 Fruit Ninja — Pygame

Create your own **Fruit Ninja-style slicing game!**  
Move the mouse across the screen, slice flying fruit, and build your score 🗡️

---

## 🔵 Indentation Guide

- Level 0 → no spaces  
- Level 1 → 4 spaces  
- Level 2 → 8 spaces  

---

# Step 1 — Imports & Config  
**Indentation Level: 0**

```python id="fn1"
import pygame
import random

WIDTH, HEIGHT = 600, 600
```

**Explanation**

- Import Pygame  
- Import random  
- Set the game window size  

---

# Step 2 — Pygame Setup  
**Indentation Level: 0**

```python id="fn2"
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
```

**Explanation**

- Start Pygame  
- Create the game window  
- Create a clock for FPS  
- Create a font for the UI  

---

# Step 3 — Blade Trail List  
**Indentation Level: 0**

```python id="fn3"
blade_trail = []
```

**Explanation**

- This list stores recent mouse positions  
- These points are joined together to make the blade trail  

---

# Step 4 — Fruit List  
**Indentation Level: 0**

```python id="fn4"
fruits = []
```

**Explanation**

- This list stores all active fruits  
- Each fruit will contain a rectangle and a vertical speed  

---

# Step 5 — Game State Variables  
**Indentation Level: 0**

```python id="fn5"
game_started = False
score = 0
spawn_timer = 0
```

**Explanation**

- `game_started` controls the start screen  
- `score` counts sliced fruits  
- `spawn_timer` controls when new fruits appear  

---

# Step 6 — Spawn Fruit Function  
**Indentation Level: 0 → 1**

```python id="fn6"
def spawn_fruit():
    x = random.randint(50, WIDTH - 100)

    fruit_rect = pygame.Rect(
        x,
        HEIGHT,
        50,
        50
    )

    fruits.append([fruit_rect, -12])
```

**Explanation**

- Pick a random x-position  
- Create a fruit at the bottom of the screen  
- Store the fruit rectangle and vertical speed together  
- `-12` makes the fruit shoot upward  

---

# Step 7 — Start The Game Loop  
**Indentation Level: 0 → 1**

```python id="fn7"
running = True

while running:
    screen.fill((30, 20, 40))
```

**Explanation**

- Start the main game loop  
- Fill the screen with a dark dojo-style background  

---

# Step 8 — Mouse Position  
**Indentation Level: 1**

```python id="fn8"
    mx, my = pygame.mouse.get_pos()
```

**Explanation**

- Get the current mouse position  
- Store it in `mx` and `my`  

---

# Step 9 — Mouse Hitbox  
**Indentation Level: 1**

```python id="fn9"
    mouse_rect = pygame.Rect(
        mx - 5,
        my - 5,
        10,
        10
    )
```

**Explanation**

- Create a tiny rectangle around the mouse  
- This rectangle is used for slice collision  

---

# Step 10 — Quit Event  
**Indentation Level: 1 → 2**

```python id="fn10"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**Explanation**

- Allow the player to close the game window  

---

# Step 11 — Start Input  
**Indentation Level: 2**

```python id="fn11"
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True
```

**Explanation**

- Any keyboard key can start the game  
- A mouse click can also start the game  
- Once started, the game logic begins running  

---

# Step 12 — Track The Mouse Trail  
**Indentation Level: 1**

```python id="fn12"
    blade_trail.append((mx, my))
```

**Explanation**

- Add the current mouse position to the blade trail  

---

# Step 13 — Limit Trail Length  
**Indentation Level: 1 → 2**

```python id="fn13"
    if len(blade_trail) > 6:
        blade_trail.pop(0)
```

**Explanation**

- Keep only the newest six mouse positions  
- Remove the oldest point  
- This makes a short moving trail  

---

# Step 14 — Game Logic Gate  
**Indentation Level: 1**

```python id="fn14"
    if game_started:
```

**Explanation**

- Fruit spawning and movement only happen after the game starts  

---

# Step 15 — Spawn Timer  
**Indentation Level: 2**

```python id="fn15"
        spawn_timer += 1

        if spawn_timer >= 60:
            spawn_timer = 0
            spawn_fruit()
```

**Explanation**

- Count one frame at a time  
- Spawn one fruit every 60 frames  
- At 60 FPS, this is about one fruit per second  

---

# Step 16 — Loop Through Fruits  
**Indentation Level: 2**

```python id="fn16"
        for f in fruits[:]:
```

**Explanation**

- Loop through a copy of the fruit list  
- This lets us safely remove fruits during the loop  

---

# Step 17 — Get Fruit Rectangle  
**Indentation Level: 3**

```python id="fn17"
            f_rect = f[0]
```

**Explanation**

- The first item in each fruit list is its rectangle  

---

# Step 18 — Move The Fruit  
**Indentation Level: 3**

```python id="fn18"
            f_rect.y += f[1]
```

**Explanation**

- Move the fruit using its vertical speed  
- Negative speed moves upward  
- Positive speed moves downward  

---

# Step 19 — Add Gravity  
**Indentation Level: 3**

```python id="fn19"
            f[1] += 0.5
```

**Explanation**

- Increase the fruit's vertical speed  
- This slowly pulls the fruit back down  

---

# Step 20 — Slice Collision  
**Indentation Level: 3**

```python id="fn20"
            if mouse_rect.colliderect(f_rect):
                score += 1
                fruits.remove(f)
```

**Explanation**

- Check if the mouse hitbox touches the fruit  
- Add 1 to the score  
- Remove the sliced fruit  

---

# Step 21 — Remove Missed Fruit  
**Indentation Level: 3**

```python id="fn21"
            elif f_rect.y > HEIGHT + 50:
                fruits.remove(f)
```

**Explanation**

- Remove fruits after they fall below the screen  
- This keeps the list clean  

---

# Step 22 — Draw Fruits  
**Indentation Level: 1 → 2**

```python id="fn22"
    for f in fruits:
        pygame.draw.rect(
            screen,
            (255, 100, 0),
            f[0]
        )
```

**Explanation**

- Draw every fruit  
- Fruits are bright orange squares  

---

# Step 23 — Draw Blade Trail  
**Indentation Level: 1**

```python id="fn23"
    if len(blade_trail) > 1:
        pygame.draw.lines(
            screen,
            (255, 255, 255),
            False,
            blade_trail,
            6
        )
```

**Explanation**

- Join all recent mouse points  
- Draw a white trail behind the mouse  
- The final number controls line thickness  

---

# Step 24 — Start Message  
**Indentation Level: 1 → 2**

```python id="fn24"
    if not game_started:
        txt = font.render(
            "PRESS ANY KEY TO START",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2)
        )
```

**Explanation**

- Show instructions before the game starts  
- Center the text on the screen  

---

# Step 25 — Score Text  
**Indentation Level: 1 → 2**

```python id="fn25"
    else:
        score_txt = font.render(
            f"Sliced: {score}",
            True,
            (255, 255, 255)
        )

        screen.blit(score_txt, (10, 10))
```

**Explanation**

- Show the score after the game starts  
- Display it in the top-left corner  

---

# Step 26 — Update Screen  
**Indentation Level: 1**

```python id="fn26"
    pygame.display.flip()
    clock.tick(60)
```

**Explanation**

- Refresh the display  
- Run the game at 60 FPS  

---

# Step 27 — Quit Pygame  
**Indentation Level: 0**

```python id="fn27"
pygame.quit()
```

**Explanation**

- Properly close Pygame  

---

# 🧠 Key Teaching Notes

## 1. Fruit Data

Each fruit is stored like this:

```python
[fruit_rect, speed_y]
```

This means one fruit contains:

- Its position and size  
- Its vertical speed  

---

## 2. Negative And Positive Movement

A negative y-speed moves upward:

```python
-12
```

Gravity slowly increases the speed:

```python
f[1] += 0.5
```

Eventually, the speed becomes positive and the fruit falls down.

---

## 3. Mouse Hitbox

The mouse itself is only one point.

We make a small rectangle around it:

```python
mouse_rect = pygame.Rect(mx - 5, my - 5, 10, 10)
```

This makes slicing easier to detect.

---

## 4. Safe List Removal

We use:

```python
for f in fruits[:]:
```

The `[:]` creates a copy.

This lets us remove fruits without breaking the loop.

---

## 5. Blade Trail

The blade trail stores recent mouse positions:

```python
[(x, y), (x, y), ...]
```

Pygame joins them using:

```python
pygame.draw.lines()
```

---

# ⭐ Student Upgrades & Challenges

## Challenge 1 — Add Different Fruit Colors

Store a color with each fruit:

```python
[fruit_rect, speed_y, color]
```

---

## Challenge 2 — Add Different Fruit Sizes

Use random sizes:

```python
size = random.randint(30, 70)
```

---

## Challenge 3 — Add Lives

Lose one life whenever a fruit falls below the screen.

---

## Challenge 4 — Add A Bomb

Create a black bomb.

If the player slices it, end the game.

---

## Challenge 5 — Add Fruit Images

Replace orange rectangles with:

- Watermelon image  
- Apple image  
- Orange image  

---

## Challenge 6 — Increase Difficulty

Make fruits spawn faster as the score increases.

---

# ✅ Full Final Code

```python id="fn28"
import pygame
import random

# --- CONFIG ---
WIDTH, HEIGHT = 600, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --- GAME OBJECTS ---
blade_trail = []
fruits = []

# --- GAME STATE ---
game_started = False
score = 0
spawn_timer = 0


def spawn_fruit():
    x = random.randint(50, WIDTH - 100)

    fruit_rect = pygame.Rect(
        x,
        HEIGHT,
        50,
        50
    )

    fruits.append([fruit_rect, -12])


running = True

while running:
    screen.fill((30, 20, 40))

    mx, my = pygame.mouse.get_pos()

    mouse_rect = pygame.Rect(
        mx - 5,
        my - 5,
        10,
        10
    )

    # --- 1. INPUTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True

    # --- 2. TRAIL TRACKING ---
    blade_trail.append((mx, my))

    if len(blade_trail) > 6:
        blade_trail.pop(0)

    # --- 3. GAME LOGIC ---
    if game_started:
        spawn_timer += 1

        if spawn_timer >= 60:
            spawn_timer = 0
            spawn_fruit()

        for f in fruits[:]:
            f_rect = f[0]

            f_rect.y += f[1]
            f[1] += 0.5

            if mouse_rect.colliderect(f_rect):
                score += 1
                fruits.remove(f)

            elif f_rect.y > HEIGHT + 50:
                fruits.remove(f)

    # --- 4. DRAWING ---
    for f in fruits:
        pygame.draw.rect(
            screen,
            (255, 100, 0),
            f[0]
        )

    if len(blade_trail) > 1:
        pygame.draw.lines(
            screen,
            (255, 255, 255),
            False,
            blade_trail,
            6
        )

    # --- 5. UI ---
    if not game_started:
        txt = font.render(
            "PRESS ANY KEY TO START",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2)
        )

    else:
        score_txt = font.render(
            f"Sliced: {score}",
            True,
            (255, 255, 255)
        )

        screen.blit(score_txt, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```
