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

# 🎯 Space Game Challenges for You 🚀

Here are some fun challenges to level up your game:

1. 💥 **Add a Score Counter**  
   - Objective: Track points every time you hit an enemy.  
   - Hint: Use a variable like `score` and increase it when bullets hit aliens.
     
```python
# Add this at the top with other settings
score = 0
font = pygame.font.SysFont("Arial", 24)

# Inside collision check (when bullet hits enemy)
score += 1

# Inside drawing section (before pygame.display.update)
score_text = font.render(f"Score: {score}", True, WHITE)
win.blit(score_text, (10, 10))
```

2. 🐢➡️⚡ **Make Enemies Faster Over Time**  
   - Objective: Increase difficulty as the game progresses.  
   - Hint: Gradually increase the alien movement speed or reduce the delay between their actions.
```python
# Inside game loop, after moving enemies
enemy_speed = 3 + score // 5  # Increase speed every 5 points
```
     

3. 💀 **Add a Game Over Screen**  
   - Objective: Show a "Game Over" screen when an enemy reaches the bottom.  
   - Hint: Check if any alien’s `y` position >= screen height and then stop the game loop.  
```python
game_over = False

# Inside enemy movement loop
for enemy in enemies:
    enemy[1] += enemy_speed
    if enemy[1] > HEIGHT:  # Enemy touched bottom
        game_over = True

# At the end of game loop
if game_over:
    win.fill(BLACK)
    game_over_text = font.render("GAME OVER! Press Q to Quit", True, RED)
    win.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.update()

    # Wait for player to quit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    continue  # Skip rest of loop
```
4. 🛸 **Change the Spaceship to an Image**  
   - Objective: Replace the rectangle spaceship with a fun picture.  
   - Hint: Use `pygame.image.load("spaceship.png")` and `screen.blit()` instead of drawing a rectangle.  
``` python
# Load images (instead of rectangles)
ship_img = pygame.image.load("images/spaceship.png")
enemy_img = pygame.image.load("images/enemy.png")
bullet_img = pygame.image.load("images/bullet.png")

# Resize images
ship_img = pygame.transform.scale(ship_img, (ship_width, ship_height))
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Draw instead of rectangles
win.blit(ship_img, (ship_x, ship_y))
for bullet in bullets:
    win.blit(bullet_img, (bullet[0], bullet[1]))
for enemy in enemies:
    win.blit(enemy_img, (enemy[0], enemy[1]))
```
5. 🔊 **Add Sound Effects**  
   - Objective: Make the game more exciting with shooting and explosion sounds.  
   - Hint: Use `pygame.mixer.Sound("laser.wav").play()` when shooting and `pygame.mixer.Sound("explosion.wav").play()` when an alien is hit.  
```python
# Load sounds
shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")

# When shooting
if keys[pygame.K_SPACE]:
    bullets.append([ship_x + ship_width // 2, ship_y])
    shoot_sound.play()

# When enemy is destroyed
explosion_sound.play()
```
  # 💻 Full code with the challenge answers
  ```python
import pygame
import random
import sys

# Step 1: Turn on pygame
pygame.init()

# Step 2: Game settings
WIDTH, HEIGHT = 500, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Ship Game")

# Step 3: Load images (Challenge 4 - Replace shapes with images)
ship_img = pygame.image.load("images/spaceship.png")
ship_img = pygame.transform.scale(ship_img, (40, 40))

enemy_img = pygame.image.load("images/alien.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 40))

bullet_img = pygame.image.load("images/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Step 4: Load sounds (Challenge 5 - Add sound effects)
shoot_sound = pygame.mixer.Sound("sounds/laser.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")

# Step 5: Spaceship
ship_width, ship_height = 40, 40
ship_x = WIDTH // 2 - ship_width // 2
ship_y = HEIGHT - ship_height - 10
ship_speed = 5

# Step 6: Bullets
bullets = []
bullet_speed = 7

# Step 7: Enemies
enemies = []
enemy_size = 40
enemy_speed = 3

# Step 8: Score (Challenge 1 - Add score counter)
score = 0
font = pygame.font.SysFont("Arial", 24)

# Step 9: Clock
clock = pygame.time.Clock()
running = True
game_over = False

# Step 10: Game loop
while running:
    clock.tick(30)  # 30 frames per second
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        # Move spaceship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship_x > 0:
            ship_x -= ship_speed
        if keys[pygame.K_RIGHT] and ship_x < WIDTH - ship_width:
            ship_x += ship_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:  # limit bullets on screen
                bullets.append([ship_x + ship_width // 2 - 5, ship_y])
                shoot_sound.play()  # Challenge 5: Shooting sound
        
        # Move bullets
        for bullet in bullets:
            bullet[1] -= bullet_speed
        bullets = [b for b in bullets if b[1] > 0]
        
        # Add enemies
        if random.randint(1, 30) == 1:
            enemies.append([random.randint(0, WIDTH-enemy_size), 0])
        
        # Move enemies (Challenge 2 - Speed increases with score)
        for enemy in enemies:
            enemy[1] += enemy_speed + score // 20  # <-- faster as score grows
        
        # Collision check (bullets vs enemies)
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if (bullet[0] > enemy[0] and bullet[0] < enemy[0] + enemy_size and
                    bullet[1] > enemy[1] and bullet[1] < enemy[1] + enemy_size):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    explosion_sound.play()  # Challenge 5: Explosion sound
                    score += 10  # Challenge 1: Score increases
                    break
        
        # Check if enemy reaches bottom (Challenge 3 - Game Over condition)
        for enemy in enemies:
            if enemy[1] > HEIGHT - enemy_size:
                game_over = True
        
        # Draw everything
        win.fill(BLACK)
        win.blit(ship_img, (ship_x, ship_y))   # Challenge 4: Draw spaceship image
        for bullet in bullets:
            win.blit(bullet_img, (bullet[0], bullet[1]))  # Challenge 4: Bullet image
        for enemy in enemies:
            win.blit(enemy_img, (enemy[0], enemy[1]))     # Challenge 4: Alien image
        
        # Draw score (Challenge 1 - Display score on screen)
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))
    
    else:
        # Game Over Screen (Challenge 3 - Show message when player loses)
        win.fill(BLACK)
        game_over_text = font.render("GAME OVER - Press R to Restart", True, WHITE)
        win.blit(game_over_text, (60, HEIGHT//2))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset everything
            score = 0
            bullets = []
            enemies = []
            ship_x = WIDTH // 2 - ship_width // 2
            game_over = False
    
    pygame.display.update()

pygame.quit()
sys.exit()


```
