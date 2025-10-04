# 🏓 Pong Game with AI Opponent + Score (Pygame)

Welcome to the **Pong Game**!  
You’ll control one paddle while the **computer AI** controls the other.  
Each time the ball passes a paddle, the other player **scores a point**.  
First to 5 points wins! 🏆

---

## 🎯 Objective
- Learn how to use **Pygame**
- Understand how the **game loop** works
- Add a **score system**
- Make a simple **AI opponent**
- Handle **collision and ball bouncing**

---

## 🚀 Step 1: Setting Up the Game

```python
import pygame
import sys
import random

# Start pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏓 Pong Game with AI and Score")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame speed
clock = pygame.time.Clock()
```
## 🧱 Step 2: Create the Paddles and Ball
```python
# Paddle and Ball sizes
paddle_width, paddle_height = 10, 70

# Player paddle (left side)
player = pygame.Rect(50, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)

# Opponent paddle (right side - AI)
opponent = pygame.Rect(WIDTH - 60, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)

# Ball setup
ball = pygame.Rect(WIDTH//2 - 7, HEIGHT//2 - 7, 14, 14)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Speeds
player_speed = 0
opponent_speed = 6
```
- 🏗️ These are the main moving parts of our game — the player, the AI opponent, and the ball.
## 🕹️ Step 3: Score Setup and Fonts
```python
# Scores
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)
```
- 🎯 We start both scores at zero (0) and use a font to display them on screen.
pygame.font.Font(None, 74) means a built-in font with size 74.
## 🎮 Step 4: The Game Loop
```python
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_speed = 0
```
- 🎮 The Game Loop runs the game forever until you quit.
It listens for keyboard input to move the paddle.

## ⚙️ Step 5: Move the Player, AI, and Ball
```python
    # Move player
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

    # Move opponent AI
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
```
- 🤖 AI Movement:
The computer paddle automatically follows the ball.
The ball also moves and bounces off the top and bottom walls.
```python
    # Bounce off paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Score system
    if ball.left <= 0:
        opponent_score += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if ball.right >= WIDTH:
        player_score += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
```
- 🎯 When the ball goes off the left or right side, the opposite player scores 1 point!
Then the ball resets to the middle.

## 🖼️ Step 7: Draw Everything (Including the Score)
```python
    # Draw background
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display scores
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH//2 + 40, 10))
    screen.blit(opponent_text, (WIDTH//2 - 80, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
- 🎨 This part draws everything on screen and updates it each frame.
The score appears at the top, with the player’s on the right and the opponent’s on the left.

## 🧠 What You Learned

- ✅ How to move paddles and the ball  
- ✅ How to add AI movement  
- ✅ How to keep and display scores  
- ✅ How to reset the ball after scoring  
- ✅ How to control frame rate (speed)  

---

## 🪄 Fun Challenges for Kids

- 🎵 Add background music  
- 🌈 Change paddle colors  
- 💨 Make the ball go faster each time someone scores  
- 🏁 Add a “You Win!” message when someone reaches 5 points  

# Full Code
```python
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game with AI")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game objects
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

# Player and AI paddles
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle speed
player_speed = 0
opponent_speed = 7

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -7
            if event.key == pygame.K_DOWN:
                player_speed = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Move paddles
    player.y += player_speed

    # Keep player on screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision (top/bottom)
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision (paddles)
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # AI movement (follow ball)
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Keep AI on screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

    # Scoring system
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Drawing everything
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, BLUE, player)
    pygame.draw.rect(SCREEN, RED, opponent)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display score
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    SCREEN.blit(player_text, (420, 10))
    SCREEN.blit(opponent_text, (350, 10))

    # Update screen
    pygame.display.flip()
    clock.tick(60)
```
# 🏓 Final Pong Game (with Challenges Solved)
```python
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game with AI - Kids Edition")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)  # Blue
AI_COLOR = (255, 100, 100)     # Light Red

# Game objects
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

# Player and AI paddles
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle speed
player_speed = 0
opponent_speed = 7

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Background music 🎵
pygame.mixer.music.load(pygame.mixer.music.get_init() or "background.mp3") if False else None
# (Note: Replace with your own .mp3 file path if you have one)
# pygame.mixer.music.play(-1)

# Clock
clock = pygame.time.Clock()

# Function to reset the ball
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

# Function to display text
def draw_text(text, size, color, x, y):
    font_obj = pygame.font.Font(None, size)
    text_surface = font_obj.render(text, True, color)
    SCREEN.blit(text_surface, (x, y))

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -7
            if event.key == pygame.K_DOWN:
                player_speed = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Move player
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        # 💨 Make the ball go faster each time it hits
        ball_speed_x *= 1.05
        ball_speed_y *= 1.05

    # AI movement
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

    # Scoring system
    if ball.left <= 0:
        player_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        opponent_score += 1
        reset_ball()

    # 🌈 Change paddle colors each score
    PLAYER_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    AI_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 🏁 Winning condition
    if player_score == 5 or opponent_score == 5:
        SCREEN.fill(BLACK)
        if player_score == 5:
            draw_text("🎉 You Win! 🎉", 100, WHITE, 220, 250)
        else:
            draw_text("😢 AI Wins!", 100, WHITE, 250, 250)
        pygame.display.flip()
        pygame.time.delay(3000)
        player_score, opponent_score = 0, 0
        reset_ball()

    # Draw everything
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, PLAYER_COLOR, player)
    pygame.draw.rect(SCREEN, AI_COLOR, opponent)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    SCREEN.blit(player_text, (420, 10))
    SCREEN.blit(opponent_text, (350, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

```
