# 🦀Crab Att**ck
* A short explanation / learning objective
* The *minimal* code snippet you’d add at that stage (safe to paste into your file)
* **Common pitfalls** to watch for
* 2–3 **challenges** (easy → hard) to test understanding or extend the game

Work through the steps in order. After finishing each step, try at least one challenge before moving on.

---

# 1. Project skeleton & imports

**Goal:** create a runnable Python file and initialize Pygame.

```python
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Crab Att**ck")
clock = pygame.time.Clock()
```

**Pitfalls:** forgetting `pygame.init()` or setting a non-tuple to `set_mode()`.

**Challenges**

1. (Easy) Change the window size to 1024×768 and run.
2. (Medium) Make the window title show the current FPS (update each second).
3. (Hard) Make the window resizable and handle resizing so the game scales (partial credit: keep aspect ratio).

---

# 2. Load assets (images & sounds)

**Goal:** safely load images/sounds and handle missing files.

```python
# example paths; keep images in same folder or set correct path
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
# sounds (optional)
# laser_sound = pygame.mixer.Sound("laser.wav")
```

**Pitfalls:** wrong paths, case-sensitive filenames, not converting images for faster blit (`.convert_alpha()`).

**Challenges**

1. (Easy) Replace a PNG with a placeholder rectangle if file not found (use try/except).
2. (Medium) Convert images with `convert_alpha()` and measure any FPS difference.
3. (Hard) Add background music that loops and a toggle key to mute/unmute.

---

# 3. Player variables & draw function

**Goal:** set up player position, speed, and a function to draw the player.

```python
player_x = 370
player_y = 480
player_x_change = 0

def draw_player(x, y):
    screen.blit(player_img, (x, y))
```

**Pitfalls:** not keeping player inside bounds; drawing before screen fill.

**Challenges**

1. (Easy) Limit player so `x` stays between `0` and `screen_width - player_img.get_width()`.
2. (Medium) Add smooth acceleration: pressing arrow increases velocity; releasing decelerates.
3. (Hard) Make player rotate slightly when moving left/right (tilt effect).

---

# 4. Enemy setup (multiple enemies)

**Goal:** create lists to handle many enemies and a draw function.

```python
num_enemies = 6
enemy_imgs = [enemy_img for _ in range(num_enemies)]
enemy_x = [random.randint(0, 736) for _ in range(num_enemies)]
enemy_y = [random.randint(50, 150) for _ in range(num_enemies)]
enemy_x_change = [3 for _ in range(num_enemies)]
enemy_y_change = [40 for _ in range(num_enemies)]

def draw_enemy(i, x, y):
    screen.blit(enemy_imgs[i], (x, y))
```

**Pitfalls:** using a single enemy variable instead of lists; off-by-one errors in ranges.

**Challenges**

1. (Easy) Increase `num_enemies` to 10 and test.
2. (Medium) Give each enemy a different speed (randomize `enemy_x_change` between 1 and 5).
3. (Hard) Implement a simple formation: enemies spawn in a grid (rows & columns) rather than random Y.

---

# 5. Bullet variables & firing function

**Goal:** implement single-bullet state machine (“ready” / “fire”).

```python
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"  # "ready" or "fire"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))
```

**Pitfalls:** firing multiple bullets if not checking state; drawing bullet when state is "ready".

**Challenges**

1. (Easy) Change bullet speed to 15 and observe gameplay difference.
2. (Medium) Allow up to 3 bullets on screen at once (switch from single-state to list of bullets).
3. (Hard) Create charged shot: holding space increases bullet speed/size, but with a cooldown.

---

# 6. Input handling (KEYDOWN / KEYUP)

**Goal:** move player left/right and fire on spacebar.

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x_change = -5
        if event.key == pygame.K_RIGHT:
            player_x_change = 5
        if event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
    if event.type == pygame.KEYUP:
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            player_x_change = 0
```

**Pitfalls:** using `player_x_change` without declaring it `global` inside functions (if you wrap code into functions). Releasing one key while holding another — consider `pygame.key.get_pressed()` for multiple simultaneous keys.

**Challenges**

1. (Easy) Replace key controls with `A` (left) and `D` (right).
2. (Medium) Use `pygame.key.get_pressed()` to allow pressing both arrow keys and handle conflicts.
3. (Hard) Add a gamepad/controller input option.

---

# 7. Movement logic: player & enemies

**Goal:** update positions and enforce boundaries; enemies reverse & drop.

```python
# player
player_x += player_x_change
player_x = max(0, min(player_x, 736))

# enemy loop (simplified)
for i in range(num_enemies):
    enemy_x[i] += enemy_x_change[i]
    if enemy_x[i] <= 0:
        enemy_x_change[i] = abs(enemy_x_change[i])
        enemy_y[i] += enemy_y_change[i]
    elif enemy_x[i] >= 736:
        enemy_x_change[i] = -abs(enemy_x_change[i])
        enemy_y[i] += enemy_y_change[i]
```

**Pitfalls:** hardcoding 736 when screen width or sprite width changes. Better compute `screen_width - sprite.get_width()`.

**Challenges**

1. (Easy) Replace `736` with `screen.get_width() - enemy_img.get_width()`.
2. (Medium) Increase enemy drop distance as levels progress.
3. (Hard) Implement sinusoidal horizontal movement for a subset of enemies.

---

# 8. Bullet movement & reset

**Goal:** move bullet while fired and reset when off-screen or on hit.

```python
if bullet_state == "fire":
    fire_bullet(bullet_x, bullet_y)
    bullet_y -= bullet_y_change

if bullet_y <= 0:
    bullet_y = 480
    bullet_state = "ready"
```

**Pitfalls:** forgetting to reset `bullet_y` → next fire starts where previous left off; drawing bullet before background fill.

**Challenges**

1. (Easy) Make bullet come from the center-top of the player sprite (adjust offsets).
2. (Medium) Add a small muzzle flash sprite when firing (display for 3 frames).
3. (Hard) Implement different bullet types (fast small, slow big) with different behaviours.

---

# 9. Collision detection

**Goal:** detect bullet-enemy collisions and respond.

```python
def is_collision(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < 27

# in enemy loop:
if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
    bullet_y = 480
    bullet_state = "ready"
    score_value += 1
    enemy_x[i] = random.randint(0, 736)
    enemy_y[i] = random.randint(50, 150)
```

**Pitfalls:** collision threshold too small/large; using sprite rectangle collision gives different behaviour.

**Challenges**

1. (Easy) Print collision coordinates to console for debugging.
2. (Medium) Replace distance check with rectangle-based collision using `pygame.Rect` and `colliderect`.
3. (Hard) Add hit effects: explosion animation and temporary invulnerability for enemies.

---

# 10. Score display & fonts

**Goal:** show score on-screen and format it.

```python
score_value = 0
font = pygame.font.Font(None, 32)

def show_score(x=10, y=10):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))
```

**Pitfalls:** not calling `font = pygame.font.Font()` after `pygame.init()` (fonts require init), or using very large font sizes that don't fit.

**Challenges**

1. (Easy) Display score with leading zeros (e.g., 005).
2. (Medium) Keep high score saved to a file and load it at start.
3. (Hard) Add animated score popups at the enemy position when you score (floating numbers).

---

# 11. Game over condition

**Goal:** stop the game when enemies reach the player line and show “GAME OVER”.

```python
over_font = pygame.font.Font(None, 64)

def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))

# inside enemy loop
if enemy_y[i] > 440:
    for j in range(num_enemies):
        enemy_y[j] = 2000  # push off-screen
    game_over_text()
    # optionally: running = False  to end loop
```

**Pitfalls:** writing text outside visible area; not stopping enemy updates leads to confusing visuals.

**Challenges**

1. (Easy) Display the final score under GAME OVER.
2. (Medium) Add a restart prompt and implement restart logic (reset positions, score).
3. (Hard) Add lives (3 lives) and show hearts; only game over when lives reach 0.

---

# 12. Main game loop & cleanup

**Goal:** put everything together and ensure clean exit.

```python
running = True
while running:
    clock.tick(60)  # cap FPS
    screen.fill((0, 0, 0))  # draw background

    # handle events (see step 6)
    # update player (step 7)
    # update enemies (step 7)
    # move bullet (step 8)
    # check collisions (step 9)
    # draw all: player, enemies, bullet, score
    pygame.display.update()

pygame.quit()
```

**Pitfalls:** forgetting `pygame.quit()` or not capping FPS (may run too fast).

**Challenges**

1. (Easy) Lower the FPS cap to 30 and see gameplay difference.
2. (Medium) Add a pause menu (toggle with `P`) that freezes all game updates.
3. (Hard) Refactor the loop into a `Game` class with methods `handle_input()`, `update()`, `draw()`.

---

# Extra extension challenges (project-level)

* Add different enemy types (faster, armored — require two hits).
* Add levels: after you kill N enemies, spawn more with higher speed.
* Add power-ups that drop from enemies (rapid fire, shield, extra life).
* Add sound effects and an explosion animation on hit.
* Local multiplayer: split-screen or alternate turns.
* Polish: HUD with lives, high score, level number, and an attract-mode main menu.

---


* Generate **starter files** where each step is a separate file (e.g., `step_01.py`, `step_02.py`, …).
* Provide **solutions** for any challenge you pick.
* Add **comments** and inline explanations to the full working code.

Which would you like next?
