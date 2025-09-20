# 🚗 Car Race Game (Built with Pygame Fundamentals)

This project is a **Car Race Game** built step by step using Pygame fundamentals like:
- Game loop  
- Event handling  
- Display surface  
- Colors  
- FPS (Frames per second)  
- Rectangles & collision detection  

---

## 🎯 Objective
Build a simple car racing game where:
- The player moves a blue car left/right  
- Enemy cars (red) fall from the top  
- The game ends if the player crashes into an enemy  
- The score increases when enemies are dodged  

---

## 🧑‍💻 Full Code

```python
import pygame
import sys
import random
from pygame.locals import *

# Step 1: Initialize pygame
pygame.init()

# Step 2: Create Display Screen
WIDTH, HEIGHT = 400, 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Car Race Game")

# Step 3: Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Player car
RED = (255, 0, 0)   # Enemy car

# Step 4: FPS (Frames Per Second)
FPS = pygame.time.Clock()

# Step 5: Player Car (Rectangles)
car_width, car_height = 50, 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Step 6: Enemy Car (Rectangles)
enemy_width, enemy_height = 50, 100
enemy_speed = 5
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height

# Step 7: Score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Step 8: The Game Loop
while True:
    # --- Event Objects ---
    for event in pygame.event.get():
        if event.type == QUIT:  # Quit event
            pygame.quit()
            sys.exit()

    # --- Player Movement (Event Handling) ---
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # --- Enemy Movement ---
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, WIDTH - enemy_width)
        score += 1  # Player dodged enemy

    # --- Rectangles & Collision Detection ---
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):  # Crash
        game_over_text = font.render("GAME OVER!", True, RED)
        DISPLAYSURF.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # --- Drawing Section ---
    DISPLAYSURF.fill(WHITE)  # Background
    pygame.draw.rect(DISPLAYSURF, BLUE, player_rect)  # Player Car
    pygame.draw.rect(DISPLAYSURF, RED, enemy_rect)    # Enemy Car

    # Draw Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # --- Update Display ---
    pygame.display.update()

    # --- Control FPS ---
    FPS.tick(60)
```
## 🏆 Next Steps for Kids

Here are some fun challenges you can try to make your Car Race Game even more exciting! 🎮

### 🚘 Add More Enemy Cars
- Instead of just one enemy car, try adding two or three.
- This makes the game harder and more fun.
- 
```python
enemy_cars = []
for i in range(2):
    enemy_x = random.randint(0, WIDTH - car_width)
    enemy_y = random.randint(-600, -100)
    enemy_cars.append([enemy_x, enemy_y])  
```

### 🖼️ Use Car Images Instead of Rectangles
- Replace the colored rectangles with real car pictures.
- You can download free pixel cars online or draw your own.

```python 
player_img = pygame.image.load("images/player_car.png")
enemy_img = pygame.image.load("images/enemy_car.png")
```

### 🎯 Add Levels
- Make the game more challenging by increasing enemy car speed as your score goes up.
- Example: every 5 points, make cars move faster.
```python
player_img = pygame.image.load("images/player_car.png")
enemy_img = pygame.image.load("images/enemy_car.png")
```
### 🎵 Add Background Music
- Play a fun racing soundtrack while the game runs.
- Add a crash sound effect when cars collide for extra excitement.

```python
pygame.mixer.music.load("sounds/race_music.mp3")
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound("sounds/crash.wav")
```
### ✅ 4. Increasing Difficulty

We can make the game harder as the player scores more points.  
Every time the score reaches a multiple of 5, the enemy cars move faster! 🚗💨

```python
# Increase speed every 5 points
if score % 5 == 0:
    enemy_speed += 1
```

✨ Try one challenge at a time, then combine them all to make your game awesome!

### The Full code (Challgence Answer)
```python
import pygame
import sys
import random
from pygame.locals import *

# Step 1: Initialize pygame
pygame.init()

# Step 2: Create Display Screen
WIDTH, HEIGHT = 400, 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Car Race Game")

# Step 3: Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Step 4: FPS
FPS = pygame.time.Clock()

# Step 5: Load Car Images
player_img = pygame.image.load("images/player_car.png")  # Replace with your car image
enemy_img = pygame.image.load("images/enemy_car.png")    # Replace with your car image
player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))

# Step 6: Player Car
car_width, car_height = 50, 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Step 7: Multiple Enemy Cars
enemy_cars = []
for i in range(2):  # Start with 2 enemies
    enemy_x = random.randint(0, WIDTH - car_width)
    enemy_y = random.randint(-600, -100)
    enemy_cars.append([enemy_x, enemy_y])

enemy_speed = 5

# Step 8: Score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Step 9: Sounds
pygame.mixer.music.load("sounds/race_music.mp3")  # Background music
pygame.mixer.music.play(-1)  # Loop forever
crash_sound = pygame.mixer.Sound("sounds/crash.wav")

# Step 10: The Game Loop
while True:
    # --- Event Objects ---
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # --- Player Movement ---
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # --- Enemy Movement ---
    for enemy in enemy_cars:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy[1] = -car_height
            enemy[0] = random.randint(0, WIDTH - car_width)
            score += 1

            # Increase difficulty
            if score % 5 == 0:  
                enemy_speed += 1

    # --- Collision Detection ---
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for enemy in enemy_cars:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], car_width, car_height)
        if player_rect.colliderect(enemy_rect):  # Crash
            pygame.mixer.Sound.play(crash_sound)
            game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
            DISPLAYSURF.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    # --- Drawing Section ---
    DISPLAYSURF.fill(WHITE)  # Background
    DISPLAYSURF.blit(player_img, (car_x, car_y))  # Draw Player

    for enemy in enemy_cars:
        DISPLAYSURF.blit(enemy_img, (enemy[0], enemy[1]))  # Draw Enemies

    # Draw Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # --- Update Display ---
    pygame.display.update()

    # --- Control FPS ---
    FPS.tick(60)

```
