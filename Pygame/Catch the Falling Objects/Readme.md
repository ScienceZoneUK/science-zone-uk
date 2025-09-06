# 🎮 Catch the Falling Objects
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/3f55f0e5-981d-4a48-a058-c277cbb82541" />

## Explanation
Imagine a game where you have a basket at the bottom of the screen, and falling objects are dropping from the sky. Your job is to catch the falling objects before they hit the ground.

## The Code Explanation
### Setting Up the Game
```python

import pygame
import random
import sys

pygame.init()

# Window size
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

clock = pygame.time.Clock()

```
- pygame.init() initializes all Pygame modules.
 - screen sets up the game window.
 - clock is used to control the frame rate.

### Creating the Player
```python
basket_width = 80
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10
```
- basket_x, basket_y: starting position of the basket.
- basket_speed: how fast the player moves left/right.

### Creating the Falling Objects (3)
```python
object_size = 30

# Object 1
obj1_x = random.randint(0, WIDTH - object_size)
obj1_y = random.randint(-300, 0)
obj1_speed = 5

# Object 2
obj2_x = random.randint(0, WIDTH - object_size)
obj2_y = random.randint(-300, 0)
obj2_speed = 4

# Object 3
obj3_x = random.randint(0, WIDTH - object_size)
obj3_y = random.randint(-300, 0)
obj3_speed = 6
```
 - Three falling objects are defined (obj1, obj2, obj3) with:
 - x, y: random start positions.
 - speed: how fast the object falls.

   ### Creating Score and Lives
```python
score = 0
lives = 3
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)
```
- Tracks the score and remaining lives.
- font objects for displaying text.

  ### Creating the Game Loop
 ```python
running = True
game_over = False

while running:
    screen.fill(WHITE)

    # -------------------
    # EVENTS
    # -------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```
 - The loop runs until the player loses their life (Game Over).
- Each frame, the screen is cleared with a white background.

### Moving the Player 
```python
    # MOVE BASKET
    # -------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed
        if basket_x < 0:
            basket_x = 0
    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed
        if basket_x > WIDTH - basket_width:
            basket_x = WIDTH - basket_width
```
- Moves the player left/right.
- Prevents the basket from leaving the screen using boundary checks

  ### Moving the Falling Objects
```python
     # MOVE OBJECTS
    # -------------------
    def move_object(obj_x, obj_y, obj_speed):
        obj_y += obj_speed
        missed = 0

        # Collision check
        if (basket_y < obj_y + object_size and
            basket_y + basket_height > obj_y and
            basket_x < obj_x + object_size and
            basket_x + basket_width > obj_x):
            return random.randint(0, WIDTH - object_size), random.randint(-300, 0), obj_speed + 0.5, 1, missed

        # Missed object
        if obj_y > HEIGHT:
            missed = 1
            return random.randint(0, WIDTH - object_size), random.randint(-300, 0), obj_speed, 0, missed

        return obj_x, obj_y, obj_speed, 0, missed

    if not game_over:
        points = 0
        missed = 0
        obj1_x, obj1_y, obj1_speed, p, m = move_object(obj1_x, obj1_y, obj1_speed)
        points += p
        missed += m
        obj2_x, obj2_y, obj2_speed, p, m = move_object(obj2_x, obj2_y, obj2_speed)
        points += p
        missed += m
        obj3_x, obj3_y, obj3_speed, p, m = move_object(obj3_x, obj3_y, obj3_speed)
        points += p
        missed += m

        score += points
        lives -= missed

        if lives <= 0:
            game_over = True
```
- Collision detection: checks if the basket catches the object.
 - Missed objects: deduct a life if the object reaches the bottom.
 - Object respawn: resets the object to the top after being caught or missed.
 - Speed increase: each caught object slightly increases speed.
 - Updates score and lives based on caught or missed objects.

   ### Drawing the Player and the Falling Objects
```python
 # -------------------
    # DRAW BASKET
    # -------------------
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # -------------------
    # DRAW OBJECTS
    # -------------------
    pygame.draw.rect(screen, RED, (obj1_x, obj1_y, object_size, object_size))
    pygame.draw.rect(screen, RED, (obj2_x, obj2_y, object_size, object_size))
    pygame.draw.rect(screen, RED, (obj3_x, obj3_y, object_size, object_size))
```
- Draws the basket and falling objects.
  ### Draw the Score and Life
```python
  # -------------------
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
```
- Also displays score and lives

  ### Create and Display Game Over
```python  
   # GAME OVER SCREEN
    # -------------------
    if game_over:
        over_text = game_over_font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 30))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game
            score = 0
            lives = 3
            obj1_y = random.randint(-300, 0)
            obj2_y = random.randint(-300, 0)
            obj3_y = random.randint(-300, 0)
            obj1_speed = 5
            obj2_speed = 4
            obj3_speed = 6
            basket_x = WIDTH // 2 - basket_width // 2
            game_over = False
```
- Displays a Game Over message.
- Press R to restart the game
 - Resets all game variables to start fresh.
### Frame Update
```python 
  pygame.display.flip()
    clock.tick(30)
```
- Updates the display each frame.
 - Limits the game to 30 frames per second.
 ### Quit Game
   ```python 
pygame.quit()
sys.exit()
```
- Cleanly exits Pygame and Python.

  ## Full Code
 ```python
  import pygame
import random
import sys

# -------------------
# SETUP
# -------------------
pygame.init()

# Window size
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 50, 50)
BLUE  = (50, 50, 255)
GREEN = (50, 255, 50)

# -------------------
# BASKET (PLAYER)
# -------------------
basket_width = 80
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

# -------------------
# FALLING OBJECTS (3 OBJECTS)
# -------------------
object_size = 30

# Object 1
obj1_x = random.randint(0, WIDTH - object_size)
obj1_y = random.randint(-300, 0)
obj1_speed = 5

# Object 2
obj2_x = random.randint(0, WIDTH - object_size)
obj2_y = random.randint(-300, 0)
obj2_speed = 4

# Object 3
obj3_x = random.randint(0, WIDTH - object_size)
obj3_y = random.randint(-300, 0)
obj3_speed = 6

# -------------------
# SCORE AND LIVES
# -------------------
score = 0
lives = 3
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)

# -------------------
# MAIN LOOP
# -------------------
running = True
game_over = False

while running:
    screen.fill(WHITE)

    # -------------------
    # EVENTS
    # -------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------
    # MOVE BASKET
    # -------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed
        if basket_x < 0:
            basket_x = 0
    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed
        if basket_x > WIDTH - basket_width:
            basket_x = WIDTH - basket_width

    # -------------------
    # MOVE OBJECTS
    # -------------------
    def move_object(obj_x, obj_y, obj_speed):
        obj_y += obj_speed
        missed = 0

        # Collision check
        if (basket_y < obj_y + object_size and
            basket_y + basket_height > obj_y and
            basket_x < obj_x + object_size and
            basket_x + basket_width > obj_x):
            return random.randint(0, WIDTH - object_size), random.randint(-300, 0), obj_speed + 0.5, 1, missed

        # Missed object
        if obj_y > HEIGHT:
            missed = 1
            return random.randint(0, WIDTH - object_size), random.randint(-300, 0), obj_speed, 0, missed

        return obj_x, obj_y, obj_speed, 0, missed

    if not game_over:
        points = 0
        missed = 0
        obj1_x, obj1_y, obj1_speed, p, m = move_object(obj1_x, obj1_y, obj1_speed)
        points += p
        missed += m
        obj2_x, obj2_y, obj2_speed, p, m = move_object(obj2_x, obj2_y, obj2_speed)
        points += p
        missed += m
        obj3_x, obj3_y, obj3_speed, p, m = move_object(obj3_x, obj3_y, obj3_speed)
        points += p
        missed += m

        score += points
        lives -= missed

        if lives <= 0:
            game_over = True

    # -------------------
    # DRAW BASKET
    # -------------------
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # -------------------
    # DRAW OBJECTS
    # -------------------
    pygame.draw.rect(screen, RED, (obj1_x, obj1_y, object_size, object_size))
    pygame.draw.rect(screen, RED, (obj2_x, obj2_y, object_size, object_size))
    pygame.draw.rect(screen, RED, (obj3_x, obj3_y, object_size, object_size))

    # -------------------
    # DRAW SCORE AND LIVES
    # -------------------
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # -------------------
    # GAME OVER SCREEN
    # -------------------
    if game_over:
        over_text = game_over_font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 30))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game
            score = 0
            lives = 3
            obj1_y = random.randint(-300, 0)
            obj2_y = random.randint(-300, 0)
            obj3_y = random.randint(-300, 0)
            obj1_speed = 5
            obj2_speed = 4
            obj3_speed = 6
            basket_x = WIDTH // 2 - basket_width // 2
            game_over = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
 ```
