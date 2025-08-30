# 🚀 Space Ship Game with Pygame
## 🚀 What is the Space Ship Game?

In this game:
- You control a **spaceship** at the bottom of the screen
- You can **move left and right** using arrow keys
- You can **shoot bullets** with the spacebar
- The goal is to **hit the falling enemies** before they reach you

---

## 🎯 Objective

1. Use arrow keys to move the spaceship
2. Press spacebar to fire bullets
3. Hit enemies to score points
4. Avoid letting enemies reach the bottom

---


## Step 1 — Import and start pygame


```python
import pygame
import random
pygame.init()
```
- Brings in Pygame tools
- pygame.init() switches Pygame on

## Step 2 — Game settings


```python
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
```
- Sets window size
- Defines colours

  ## Step 3 — Create window


```python
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Ship Game")
```
- Creates a black game window
- Names it “Space Ship Game”

 ## Step 4 — Spaceship


```python
ship_width, ship_height = 40, 20
ship_x = WIDTH // 2 - ship_width // 2
ship_y = HEIGHT - 40
ship_speed = 5
```
- The spaceship is a blue rectangle
- Starts at the bottom of the screen

 ## Step 5 — Bullets


```python
bullets = []
bullet_speed = 7
```
- Bullets are stored in a list
- They move upward quickly

  ## Step 6 — Enemies


```python
enemies = []
enemy_speed = 3
enemy_size = 30
```
- Enemies are red squares
- They fall from the top


  ## Step 7 — Clock


```python
clock = pygame.time.Clock()
```
- Controls the speed of the game


  ## Step 8 — Game loop


```python
running = True
while running:
```
- Runs again and again until you quit

  ## Step 8a — Quit event


```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
- Lets you close the window

    ## Step 8b — Move spaceship


```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and ship_x > 0:
    ship_x -= ship_speed
if keys[pygame.K_RIGHT] and ship_x < WIDTH - ship_width:
    ship_x += ship_speed
if keys[pygame.K_SPACE]:
    if len(bullets) < 5:
        bullets.append([ship_x + ship_width//2, ship_y])
```
- Left/Right arrows move the ship
- Spacebar shoots bullets
- Max 5 bullets at once

## Step 8c — Move bullets


```python
for bullet in bullets[:]:
    bullet[1] -= bullet_speed
    if bullet[1] < 0:
        bullets.remove(bullet)
```
- Bullets move upward
- Removed when they leave the screen

  ## Step 8d — Add enemies


```python
if random.randint(1, 30) == 1:
    enemies.append([random.randint(0, WIDTH-enemy_size), 0])
```
- Randomly spawns new enemies at the top

 ## Step 8e — Move enemies


```python
for enemy in enemies[:]:
    enemy[1] += enemy_speed
    if enemy[1] > HEIGHT:
        enemies.remove(enemy)
```
- Enemies fall down
- Disappear when they reach the bottom

 ## Step 8f — Bullet hits enemy


```python
for bullet in bullets[:]:
    for enemy in enemies[:]:
        if (bullet[0] > enemy[0] and bullet[0] < enemy[0]+enemy_size and
            bullet[1] > enemy[1] and bullet[1] < enemy[1]+enemy_size):
            bullets.remove(bullet)
            enemies.remove(enemy)
            break
```
- If bullet touches an enemy → both disappear

 ## Step 8g — Draw spaceship


```python
pygame.draw.rect(win, BLUE, (ship_x, ship_y, ship_width, ship_height))

```
- Draws the spaceship


 ## Step 8h — Draw bullets


```python
for bullet in bullets:
    pygame.draw.rect(win, WHITE, (bullet[0], bullet[1], 4, 10))

```
- Draws small white rectangles as bullets

 ## Step 8i — Draw enemies


```python
for enemy in enemies:
    pygame.draw.rect(win, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
```
- Draws falling enemies
  
 ## Step 8j — Update screen


```python
pygame.display.update()
```
- Refreshes the screen so changes appear

  # 💻 Code Fun Activity — Space Ship Game
  
```python
import pygame
import random

# Step 1: Start pygame
pygame.init()

# Step 2: Game settings
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Step 3: Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Ship Game")

# Step 4: Spaceship setup
ship_width, ship_height = 40, 20
ship_x = WIDTH // 2 - ship_width // 2
ship_y = HEIGHT - 40
ship_speed = 5

# Step 5: Bullets
bullets = []
bullet_speed = 7

# Step 6: Enemies
enemies = []
enemy_speed = 3
enemy_size = 30

# Step 7: Clock
clock = pygame.time.Clock()

# Step 8: Main game loop
running = True
while running:
    clock.tick(30)  # 30 frames per second
    win.fill(BLACK)

    # Step 8a: Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Step 8b: Keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - ship_width:
        ship_x += ship_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # limit bullets
            bullets.append([ship_x + ship_width//2, ship_y])

    # Step 8c: Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Step 8d: Add enemies
    if random.randint(1, 30) == 1:
        enemies.append([random.randint(0, WIDTH-enemy_size), 0])

    # Step 8e: Move enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)  # enemy reached bottom!

    # Step 8f: Check bullet collisions with enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet[0] > enemy[0] and bullet[0] < enemy[0]+enemy_size and
                bullet[1] > enemy[1] and bullet[1] < enemy[1]+enemy_size):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Step 8g: Draw spaceship
    pygame.draw.rect(win, BLUE, (ship_x, ship_y, ship_width, ship_height))

    # Step 8h: Draw bullets
    for bullet in bullets:
        pygame.draw.rect(win, WHITE, (bullet[0], bullet[1], 4, 10))

    # Step 8i: Draw enemies
    for enemy in enemies:
        pygame.draw.rect(win, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Step 8j: Update screen
    pygame.display.update()

pygame.quit()

```
