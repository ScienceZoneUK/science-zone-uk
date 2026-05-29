# Dodge and Collect
Collect coins while avoiding the enemies

## The code
### Imports and constants
```
import pygame
import random
import sys
import math

pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge and Collect")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLUE = (100, 200, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 150, 0)
GRAY = (100, 100, 100)

# Fonts
big_font = pygame.font.Font(None, 72)
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Player
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_size = 30
player_speed = 6

# Coins
coins = []
coin_spawn_timer = 0

# Enemies
enemies = []
enemy_spawn_timer = 0

# Game stats
score = 0
game_over = False
game_state = "start"
time_elapsed = 0

# Difficulty
current_level = 1
```

### Main game loop
```
# MAIN GAME LOOP
running = True
while running:
    dt = clock.tick(60) / 1000.0
    
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Start game
        if event.type == pygame.KEYDOWN and game_state == "start":
            if event.key == pygame.K_SPACE:
                game_state = "playing"
                score = 0
                time_elapsed = 0
                coins = []
                enemies = []
                coin_spawn_timer = 0
                enemy_spawn_timer = 0
                current_level = 1
        
        # Restart after game over
        if event.type == pygame.KEYDOWN and game_state == "game_over":
            if event.key == pygame.K_SPACE:
                game_state = "start"
                player_x = WIDTH // 2
                player_y = HEIGHT // 2
    
    if game_state == "playing":
        time_elapsed += dt
        
        # PLAYER MOVEMENT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += player_speed
        
        # Keep player on screen
        if player_x < 0:
            player_x = 0
        if player_x > WIDTH - player_size:
            player_x = WIDTH - player_size
        if player_y < 0:
            player_y = 0
        if player_y > HEIGHT - player_size:
            player_y = HEIGHT - player_size
        
        # SPAWN COINS
        coin_spawn_timer += dt
        if coin_spawn_timer > 1.0:
            coin_x = random.randint(0, WIDTH - 20)
            coin_y = random.randint(100, HEIGHT - 20)
            coins.append({"x": coin_x, "y": coin_y, "size": 10})
            coin_spawn_timer = 0
        
        # SPAWN ENEMIES (more as level increases)
        enemy_spawn_timer += dt
        spawn_rate = max(0.5, 2.0 - (current_level * 0.2))  # Faster spawning
        if enemy_spawn_timer > spawn_rate:
            enemy_x = random.randint(0, WIDTH - 25)
            enemy_y = random.randint(100, HEIGHT - 25)
            enemy_speed = 1.5 + (current_level * 0.3)  # Faster enemies
            enemies.append({"x": enemy_x, "y": enemy_y, "speed": enemy_speed, "size": 25})
            enemy_spawn_timer = 0
        
        # MOVE ENEMIES (toward player)
        for enemy in enemies:
            dx = player_x - enemy["x"]
            dy = player_y - enemy["y"]
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 0:
                enemy["x"] += (dx / distance) * enemy["speed"]
                enemy["y"] += (dy / distance) * enemy["speed"]
        
        # CHECK COIN COLLECTION
        for coin in coins[:]:
            dist_to_coin = math.sqrt((player_x - coin["x"])**2 + (player_y - coin["y"])**2)
            if dist_to_coin < player_size // 2 + coin["size"]:
                score += 10
                coins.remove(coin)
        
        # CHECK ENEMY COLLISION
        for enemy in enemies:
            dist_to_enemy = math.sqrt((player_x - enemy["x"])**2 + (player_y - enemy["y"])**2)
            if dist_to_enemy < player_size // 2 + enemy["size"] // 2:
                game_state = "game_over"
        
        # INCREASE LEVEL
        if score % 100 == 0 and score > 0:
            current_level = (score // 100) + 1
    
    # DRAW EVERYTHING
    screen.fill(BLACK)
    
    # Title
    title = font.render("DODGE AND COLLECT", True, GOLD)
    screen.blit(title, (WIDTH // 2 - 220, 10))
    
    # Score and level
    score_text = small_font.render(f"Score: {score}", True, GREEN)
    level_text = small_font.render(f"Level: {current_level}", True, ORANGE)
    time_text = small_font.render(f"Time: {int(time_elapsed)}s", True, WHITE)
    
    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 60))
    screen.blit(time_text, (WIDTH - 200, 20))
    
    # Start screen
    if game_state == "start":
        instructions = [
            "Use ARROW KEYS or WASD to move",
            "",
            "Collect GOLD coins for points",
            "Avoid RED enemies!",
            "",
            "The more you collect, the harder it gets",
            "",
            "Press SPACE to start"
        ]
        
        y = 150
        for line in instructions:
            text = small_font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 2 - 200, y))
            y += 45
    
    # Playing
    elif game_state == "playing":
        # Draw coins
        for coin in coins:
            pygame.draw.circle(screen, GOLD, (int(coin["x"]), int(coin["y"])), coin["size"])
            pygame.draw.circle(screen, ORANGE, (int(coin["x"]), int(coin["y"])), coin["size"], 2)
        
        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, RED, (enemy["x"], enemy["y"], enemy["size"], enemy["size"]))
            pygame.draw.circle(screen, WHITE, (int(enemy["x"] + enemy["size"] // 2), 
                                              int(enemy["y"] + enemy["size"] // 2)), 3)
        
        # Draw player
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size), 2)
        
        # Draw lives indicator (number of enemies)
        enemies_text = small_font.render(f"Enemies: {len(enemies)}", True, RED)
        screen.blit(enemies_text, (WIDTH - 200, 60))
    
    # Game over
    elif game_state == "game_over":
        game_over_text = big_font.render("GAME OVER!", True, RED)
        final_score = font.render(f"Final Score: {score}", True, WHITE)
        max_level = font.render(f"Level Reached: {current_level}", True, ORANGE)
        survival = font.render(f"Survived: {int(time_elapsed)}s", True, GREEN)
        restart_text = small_font.render("Press SPACE to play again", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 120))
        screen.blit(final_score, (WIDTH // 2 - 120, HEIGHT // 2 - 30))
        screen.blit(max_level, (WIDTH // 2 - 120, HEIGHT // 2 + 20))
        screen.blit(survival, (WIDTH // 2 - 110, HEIGHT // 2 + 70))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 130))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
```

## Challenges
### 1 - Player colour
Change the player colour from BLUE to another colour of your choice

### 2 - Player size
Change the player size from 30 to be bigger or smaller

### 3 - Player speed
Change the player speed from 6 to be faster or slower

### 4 - Coin value
Change the value of the coins from 10 to be higher

### 5 - Enemy size
Change the enemy size from 25 to be bigher or smaller

### 6 - Coin spawn rate
Change the spawn timer from 1.0 to a lower number (for more coins) or a higher number (for less coins)

### 7 - Enemy speed
Change the enemy speed multiplier to make them move faster or slower

### 8 - Health system
Create lives that decrease when hit by enemies
```
lives = 3
# When hit by enemy:
if dist_to_enemy < ...:
    lives -= 1
    if lives <= 0:
        game_state = "game_over"
    else:
        # Move player to center
        player_x = WIDTH // 2
        player_y = HEIGHT // 2
```
