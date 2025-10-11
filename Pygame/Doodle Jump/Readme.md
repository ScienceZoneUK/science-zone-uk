# <img width="40" height="40" alt="image" src="https://github.com/user-attachments/assets/28933e7b-7832-4d27-91fc-690b1046644c" /> Doodle Jump 
By the end of this session, I will be able to:

- Define what a jumping platform game is.  
- Describe how gravity and movement work in Pygame.  
- Use code to build a simple **Doodle Jump** game.  
- Test and improve the game by adding fun new features.  

---

## 1️⃣ What Is Doodle Jump?

💬 **Think & Discuss:**

- Have you ever played a game where you jump higher and higher?  
- What happens if your player falls off the screen?  
- What makes jumping games fun and exciting?  

📌 **Goal:**  
Keep your doodle jumping from one platform to another without falling!  
How high can you go? 🌟

---

## 2️⃣ The Challenge 🎮

We want to make a **Doodle Jump** game that:

- Starts when you run the program.  
- Uses **gravity** to make your doodle fall.  
- Makes your doodle **jump** when it lands on a platform.  
- Moves platforms down when your doodle goes high.  
- Ends the game when your doodle falls off the screen.  

✏️ **Write/Think:**  
What could make this game more fun or colorful?  
(Maybe clouds? Music? A rainbow background?)

---

## 3️⃣ How It Works 🧠

🪜 Your player (the doodle) is like a **rectangle** that can move left or right.  
💨 Gravity pulls the doodle down.  
🌈 When the doodle touches a platform, it **bounces back up**!  
📈 The screen scrolls as you climb higher, and you earn **points** for each new platform.  

---

## 4️⃣ Let's Build It! 🧩

1. **Create a screen** for the game (like a window).  
2. **Add your player** (a yellow square).  
3. **Add some platforms** to jump on.  
4. **Make your player jump** when it hits a platform.  
5. **Add gravity** to make the player fall.  
6. **Keep score** as your doodle climbs higher!  

---

## Code Explianation
### Import and Start Pygame
```python
import pygame
import random
import sys
```
What does it do
- import brings in tools: pygame (game tools), random (for random positions), sys (for quitting nicely).
- pygame.init() turns on Pygame — think of it as switching the game engine on.

### Create the game window
```python
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Doodle Jump - Kids Edition")
```
What this does
- Makes a window 400×600 pixels where the game will appear.
- caption shows the game title at the top of the window.

### Colors and clock
```python
WHITE = (255,255,255)
BLUE = (100,150,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
clock = pygame.time.Clock()
FPS = 60
```
What this does
- Defines colors using RGB (red, green, blue).
- Creates a clock to keep the game running at a steady speed (60 frames per second).

### The player (our doodle)
```python
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 50)
player_speed_y = 0
gravity = 0.4
jump_power = -10
```
What this does
- player is a square (50×50) in the middle near the bottom.
- player_speed_y is how fast the player is moving up/down.
- gravity pulls the player down slowly each frame.
- jump_power is how strong a bounce is (negative = up).
### Platforms (the steps to jump on)
```python
platforms = [
    pygame.Rect(100, 500, 80, 10),
    pygame.Rect(200, 400, 80, 10),
    pygame.Rect(50, 300, 80, 10),
    pygame.Rect(250, 200, 80, 10)
]
```
What this does
- Makes four green platforms at different heights.
- Each platform is a rectangle that the player can land on.

### Score and font
```python
score = 0
font = pygame.font.Font(None, 36)
```
What this does
- score keeps track of how many platforms the player passed.
- font decides how the score number looks on screen.
### Jump function
  ```python
  def jump():
    global player_speed_y
    player_speed_y = jump_power
  ```
  What this does
- A helper we could call to make the player jump. (In this program we set jump when colliding with a platform.)

### The game loop (the engine)
```python
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```
What this does
- while running keeps the game repeating many times per second.
- clock.tick(FPS) makes each loop happen at a steady speed (60 times per second).
- The for event looks for actions like closing the window.

### Move left & right
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.x -= 5
if keys[pygame.K_RIGHT]:
    player.x += 5
```
What this does
- Reads keyboard keys. If left or right arrows are held, move the player horizontally.

### Wrap-around screen edges
```python
  if player.x < -50:
    player.x = WIDTH
elif player.x > WIDTH:
    player.x = -50
```
What this does
- If the player goes off the left side, it appears at the right (and vice versa). This makes the world wrap around.

### Gravity and move by vertical speed
```python
player_speed_y += gravity
player.y += player_speed_y
```
What this does
- Each frame we add gravity to vertical speed, then move the player by that speed.
- Positive player_speed_y → moving down; negative → moving up.
### Landing on platforms (bounce)
```python
for platform in platforms:
    if player.colliderect(platform) and player_speed_y > 0:
        player_speed_y = jump_power
```
What this does
- Checks if the player's rectangle is touching a platform and moving downward.
- If yes → set vertical speed to jump_power so player bounces up.
### Scroll the world (when player gets high)
```python
if player.y < HEIGHT / 3:
player.y += abs(player_speed_y)
for platform in platforms:
platform.y += abs(player_speed_y)
if platform.y > HEIGHT:
            platforms.remove(platform)
            platforms.append(pygame.Rect(random.randint(0, WIDTH - 80), -10, 80, 10))
            score += 1
```
  What this does
- If the player moves above the top third of the screen, we move the player down a bit and push every platform down.
- Platforms that move off the bottom are removed and new ones are added at the top at random x-positions.
- Each time we create a new platform, we add 1 to score.
### Game over check
  ```python
    if player.y > HEIGHT:
    SCREEN.fill(BLACK)
    text = font.render("Game Over! Your Score: " + str(score), True, WHITE)
    SCREEN.blit(text, (30, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    running = False
   ```
    What this does
- If the player falls below the bottom of the screen → show "Game Over" and the score, pause 2 seconds, then stop the game.

### Draw everything (make it visible)
```python
SCREEN.fill(BLUE)
pygame.draw.rect(SCREEN, (255, 255, 0), player)
for platform in platforms:
pygame.draw.rect(SCREEN, GREEN, platform)
text = font.render("Score: " + str(score), True, BLACK)
SCREEN.blit(text, (10, 10))
pygame.display.flip()
```
   
What this does
- SCREEN.fill(BLUE) paints the sky.
- Draw the player (yellow) and platforms (green).
- Draw the score in the top-left.
- pygame.display.flip() updates the screen so the player sees the new frame.

# Full Code
 ```python
import pygame
import random
import sys

# Step 1: Turn on pygame
pygame.init()

# Step 2: Set up the screen
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Doodle Jump - Kids Edition")

# Step 3: Colors
WHITE = (255, 255, 255)
BLUE = (100, 150, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Step 4: Game variables
clock = pygame.time.Clock()
FPS = 60

# Step 5: Player (the doodle)
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 50)
player_speed_y = 0
gravity = 0.4
jump_power = -10

# Step 6: Platforms
platforms = [pygame.Rect(100, 500, 80, 10),
             pygame.Rect(200, 400, 80, 10),
             pygame.Rect(50, 300, 80, 10),
             pygame.Rect(250, 200, 80, 10)]

# Step 7: Score
score = 0
font = pygame.font.Font(None, 36)

# Step 8: Jumping function
def jump():
    global player_speed_y
    player_speed_y = jump_power

# Step 9: Main game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player left/right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Wrap around screen
    if player.x < -50:
        player.x = WIDTH
    elif player.x > WIDTH:
        player.x = -50

    # Apply gravity
    player_speed_y += gravity
    player.y += player_speed_y

    # Check platform collisions (bounce)
    for platform in platforms:
        if player.colliderect(platform) and player_speed_y > 0:
            player_speed_y = jump_power

    # Scroll platforms when player goes high
    if player.y < HEIGHT / 3:
        player.y += abs(player_speed_y)
        for platform in platforms:
            platform.y += abs(player_speed_y)
            if platform.y > HEIGHT:
                platforms.remove(platform)
                platforms.append(pygame.Rect(random.randint(0, WIDTH - 80), -10, 80, 10))
                score += 1  # Add points for new platforms

    # Game over check
    if player.y > HEIGHT:
        SCREEN.fill(BLACK)
        text = font.render("Game Over! Your Score: " + str(score), True, WHITE)
        SCREEN.blit(text, (30, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Draw everything
    SCREEN.fill(BLUE)
    pygame.draw.rect(SCREEN, (255, 255, 0), player)
    for platform in platforms:
        pygame.draw.rect(SCREEN, GREEN, platform)

    # Draw score
    text = font.render("Score: " + str(score), True, BLACK)
    SCREEN.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
 ```

## 🧩 Challenges Solved

✅ Add a background image  
✅ Add sound effects for jumps and falls  
✅ Make platforms move  
✅ Add a score that increases as the player goes higher  
✅ Add a “Game Over” message when the jumper falls  

---

## 🚀 Full Updated Code

```python
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Doodle Jump")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Load images
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load("doodle.png")
player_img = pygame.transform.scale(player_img, (60, 60))

# Sounds
jump_sound = pygame.mixer.Sound("jump.wav")
fall_sound = pygame.mixer.Sound("fall.wav")

# Player settings
player = pygame.Rect(200, 500, 50, 50)
player_speed_y = 0
gravity = 0.4
jump_force = -10
score = 0

# Platform settings
platforms = [pygame.Rect(100, 500, 100, 10), pygame.Rect(200, 400, 100, 10),
             pygame.Rect(50, 300, 100, 10), pygame.Rect(250, 200, 100, 10)]

# Clock
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game variables
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Move left and right
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        # Apply gravity
        player_speed_y += gravity
        player.y += player_speed_y

        # Check collision with platforms
        for platform in platforms:
            if player.colliderect(platform) and player_speed_y > 0:
                player_speed_y = jump_force
                jump_sound.play()
                score += 1

        # Move platforms down as player jumps
        if player.y < 250:
            player.y += abs(player_speed_y)
            for platform in platforms:
                platform.y += abs(player_speed_y)
                # Recycle platforms
                if platform.y > HEIGHT:
                    platform.x = random.randint(0, WIDTH - 100)
                    platform.y = random.randint(-50, 0)

        # Add moving platforms
        for platform in platforms:
            platform.x += random.choice([-1, 1])
            if platform.x < 0:
                platform.x = 0
            elif platform.x > WIDTH - 100:
                platform.x = WIDTH - 100

        # Game over when player falls
        if player.y > HEIGHT:
            fall_sound.play()
            game_over = True

    # Draw everything
    screen.blit(background, (0, 0))
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)
    screen.blit(player_img, player)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Game Over Message
    if game_over:
        game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)
