# 🐦 Flappy Bird — Pygame

Create your own **Flappy Bird-style game!**  
Press **SPACE** to flap, fly through pipes, and avoid crashing 🐤

---

## 🔵 Indentation Guide

- Level 0 → no spaces  
- Level 1 → 4 spaces  
- Level 2 → 8 spaces  

---

# Step 1 — Imports & Config  
**Indentation Level: 0**

```python id="fb1"
import pygame
import random

WIDTH, HEIGHT = 400, 600
PIPE_W = 70
PIPE_GAP = 150
```

**Explanation**

- Import Pygame and random  
- Set the window size  
- `PIPE_W` controls pipe width  
- `PIPE_GAP` controls the space between top and bottom pipes  

---

# Step 2 — Pygame Setup  
**Indentation Level: 0**

```python id="fb2"
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
```

**Explanation**

- Start Pygame  
- Create the game window  
- `clock` controls FPS  
- `font` is used for text  

---

# Step 3 — Game State Controller  
**Indentation Level: 0**

```python id="fb3"
game_started = False
```

**Explanation**

- The game starts paused  
- The bird will not fall until the player presses SPACE  
- This gives the player time to get ready  

---

# Step 4 — Bird Variables  
**Indentation Level: 0**

```python id="fb4"
bird_rect = pygame.Rect(50, 250, 40, 40)
bird_vy = 0
gravity = 0.8
jump_power = -12
```

**Explanation**

- `bird_rect` stores the bird position and hitbox  
- `bird_vy` is the bird's vertical speed  
- `gravity` pulls the bird down  
- `jump_power` pushes the bird up  

---

# Step 5 — Pipe & Score Variables  
**Indentation Level: 0**

```python id="fb5"
pipes = []
pipe_speed = 5
pipe_timer = 0
score = 0
```

**Explanation**

- `pipes` stores all pipe rectangles  
- `pipe_speed` controls how fast pipes move left  
- `pipe_timer` controls when new pipes spawn  
- `score` counts pipe sets survived  

---

# Step 6 — Spawn Pipe Pair Function  
**Indentation Level: 0 → 1**

```python id="fb6"
def spawn_pipe_pair():
    top_h = random.randint(50, HEIGHT - PIPE_GAP - 50)
    top_rect = pygame.Rect(WIDTH, 0, PIPE_W, top_h)

    bottom_y = top_h + PIPE_GAP
    bottom_h = HEIGHT - bottom_y
    bottom_rect = pygame.Rect(WIDTH, bottom_y, PIPE_W, bottom_h)

    pipes.append(top_rect)
    pipes.append(bottom_rect)
```

**Explanation**

- Creates one top pipe and one bottom pipe  
- The gap between them is where the bird flies  
- Both pipes start at the right side of the screen  
- The two pipe rectangles are added to the `pipes` list  

---

# Step 7 — Spawn First Pipes  
**Indentation Level: 0**

```python id="fb7"
spawn_pipe_pair()
```

**Explanation**

- Create the first pipe pair before the game starts  

---

# Step 8 — Game Loop  
**Indentation Level: 0 → 1**

```python id="fb8"
running = True

while running:
    screen.fill((0, 150, 255))
```

**Explanation**

- Main game loop  
- Blue background looks like sky  

---

# Step 9 — Inputs  
**Indentation Level: 1 → 2**

```python id="fb9"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_started:
                game_started = True

            bird_vy = jump_power
```

**Explanation**

- Close button exits the game  
- SPACE starts the game if it has not started yet  
- SPACE also makes the bird jump upward  

---

# Step 10 — Game Logic Gate  
**Indentation Level: 1**

```python id="fb10"
    if game_started:
```

**Explanation**

- The main physics only runs after the game starts  
- This is why the bird does not fall on the start screen  

---

# Step 11 — Move Bird  
**Indentation Level: 2**

```python id="fb11"
        bird_vy += gravity
        bird_rect.y += bird_vy
```

**Explanation**

- Gravity increases downward speed  
- The bird moves based on its vertical speed  
- Negative speed moves up  
- Positive speed moves down  

---

# Step 12 — Move Pipes  
**Indentation Level: 2 → 3**

```python id="fb12"
        for p in pipes[:]:
            p.x -= pipe_speed

            if p.right < 0:
                pipes.remove(p)
```

**Explanation**

- Move every pipe left  
- Remove pipes after they leave the screen  
- `pipes[:]` is a safe copy, so we can remove items while looping  

---

# Step 13 — Bird Boundary Collision  
**Indentation Level: 2**

```python id="fb13"
        if bird_rect.top < 0 or bird_rect.bottom > HEIGHT:
            running = False
```

**Explanation**

- Game ends if the bird flies above the screen  
- Game ends if the bird falls below the screen  

---

# Step 14 — Pipe Collision  
**Indentation Level: 2 → 3**

```python id="fb14"
        for p in pipes:
            if bird_rect.colliderect(p):
                running = False
```

**Explanation**

- Check if the bird hits any pipe  
- `colliderect()` checks rectangle collision  
- If the bird touches a pipe, game over  

---

# Step 15 — Pipe Spawn Timer  
**Indentation Level: 2**

```python id="fb15"
        pipe_timer += 1

        if pipe_timer >= 80:
            pipe_timer = 0
            spawn_pipe_pair()
            score += 1
```

**Explanation**

- Count frames using `pipe_timer`  
- Every 80 frames, create a new pipe pair  
- Add 1 score each time a new pair is spawned  

---

# Step 16 — Draw Pipes  
**Indentation Level: 1 → 2**

```python id="fb16"
    for p in pipes:
        pygame.draw.rect(screen, (0, 180, 0), p)
```

**Explanation**

- Draw every pipe as a green rectangle  

---

# Step 17 — Draw Bird  
**Indentation Level: 1**

```python id="fb17"
    pygame.draw.rect(screen, (255, 215, 0), bird_rect)
```

**Explanation**

- Draw the bird as a yellow rectangle  

---

# Step 18 — Start Text  
**Indentation Level: 1 → 2**

```python id="fb18"
    if not game_started:
        start_txt = font.render("PRESS SPACE TO FLY", True, (255, 255, 255))
        screen.blit(
            start_txt,
            (WIDTH // 2 - start_txt.get_width() // 2, HEIGHT // 2 - 50)
        )
```

**Explanation**

- If the game has not started, show instructions  
- The text is centered using its width  

---

# Step 19 — Score Text  
**Indentation Level: 1 → 2**

```python id="fb19"
    else:
        txt = font.render(f"Pipes: {score}", True, (255, 255, 255))
        screen.blit(txt, (10, 10))
```

**Explanation**

- After the game starts, show the score  
- Score appears in the top-left corner  

---

# Step 20 — Update Screen  
**Indentation Level: 1**

```python id="fb20"
    pygame.display.flip()
    clock.tick(60)
```

**Explanation**

- Refresh the display  
- Run at 60 FPS  

---

# Step 21 — Quit  
**Indentation Level: 0**

```python id="fb21"
pygame.quit()
```

**Explanation**

- Properly close Pygame  

---

# 🧠 Key Teaching Notes

## 1. Game Started Flag

The variable:

```python
game_started = False
```

controls whether the game is paused or active.

Before SPACE is pressed:

- Bird does not fall  
- Pipes do not move  
- Start text is shown  

After SPACE is pressed:

- Gravity starts  
- Pipes move  
- Score appears  

---

## 2. Gravity And Jump

The bird uses velocity:

```python
bird_vy
```

Gravity makes it fall:

```python
bird_vy += gravity
```

SPACE makes it jump:

```python
bird_vy = jump_power
```

Because `jump_power` is negative, the bird moves upward.

---

## 3. Pipe Pairs

Each pipe pair is made from two rectangles:

- Top pipe  
- Bottom pipe  

The space between them is controlled by:

```python
PIPE_GAP
```

---

## 4. Safe List Removal

When moving pipes, we use:

```python
for p in pipes[:]:
```

This loops through a copy of the list.

That means we can safely remove old pipes without breaking the loop.

---

# ⭐ Student Upgrades & Challenges

## Challenge 1 — Change Difficulty

Try changing:

```python
PIPE_GAP = 120
```

Smaller gap = harder game.

---

## Challenge 2 — Add Better Score

Instead of adding score when pipes spawn, add score when the bird passes a pipe.

Hint:

- Store whether a pipe has already been counted  
- Or count when pipe x-position passes the bird  

---

## Challenge 3 — Add Restart

When game over happens, show a restart message instead of quitting immediately.

Hint:

- Use a `game_over` variable  
- Reset bird, pipes, timer, and score  

---

## Challenge 4 — Add Images

Replace rectangles with images:

- Bird image  
- Pipe image  
- Background image  

---

# ✅ Full Final Code

```python id="fb22"
import pygame
import random

# --- CONFIG ---
WIDTH, HEIGHT = 400, 600
PIPE_W = 70
PIPE_GAP = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --- GAME STATE CONTROLLER ---
game_started = False

# --- GAME OBJECTS ---
bird_rect = pygame.Rect(50, 250, 40, 40)
bird_vy = 0
gravity = 0.8
jump_power = -12

pipes = []
pipe_speed = 5
pipe_timer = 0
score = 0


def spawn_pipe_pair():
    top_h = random.randint(50, HEIGHT - PIPE_GAP - 50)
    top_rect = pygame.Rect(WIDTH, 0, PIPE_W, top_h)

    bottom_y = top_h + PIPE_GAP
    bottom_h = HEIGHT - bottom_y
    bottom_rect = pygame.Rect(WIDTH, bottom_y, PIPE_W, bottom_h)

    pipes.append(top_rect)
    pipes.append(bottom_rect)


spawn_pipe_pair()

running = True

while running:
    screen.fill((0, 150, 255))

    # --- 1. INPUTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_started:
                game_started = True

            bird_vy = jump_power

    # --- 2. GAME LOGIC ---
    if game_started:

        bird_vy += gravity
        bird_rect.y += bird_vy

        for p in pipes[:]:
            p.x -= pipe_speed

            if p.right < 0:
                pipes.remove(p)

        if bird_rect.top < 0 or bird_rect.bottom > HEIGHT:
            running = False

        for p in pipes:
            if bird_rect.colliderect(p):
                running = False

        pipe_timer += 1

        if pipe_timer >= 80:
            pipe_timer = 0
            spawn_pipe_pair()
            score += 1

    # --- 3. DRAWING EVERYTHING ---
    for p in pipes:
        pygame.draw.rect(screen, (0, 180, 0), p)

    pygame.draw.rect(screen, (255, 215, 0), bird_rect)

    if not game_started:
        start_txt = font.render("PRESS SPACE TO FLY", True, (255, 255, 255))

        screen.blit(
            start_txt,
            (WIDTH // 2 - start_txt.get_width() // 2, HEIGHT // 2 - 50)
        )

    else:
        txt = font.render(f"Pipes: {score}", True, (255, 255, 255))
        screen.blit(txt, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```
