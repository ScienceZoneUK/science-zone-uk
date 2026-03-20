# Catch the Falling Objects

## Imports
```
import pygame
import random
import sys
```

## Setup & Styling
```
pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# BASKET
basket_x = WIDTH // 2
basket_y = HEIGHT - 50
basket_width = 100
basket_height = 20
basket_speed = 8

# FALLING OBJECTS
falling_objects = []
spawn_timer = 0

# GAME STATS
score = 0
missed = 0
game_over = False
```

## Main Game Loop
```
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Time since last frame
    
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Restart game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                score = 0
                missed = 0
                falling_objects = []
                game_over = False
    
    if not game_over:
        # MOVE BASKET (left and right with arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed
        
        # Keep basket on screen
        if basket_x < 0:
            basket_x = 0
        if basket_x > WIDTH - basket_width:
            basket_x = WIDTH - basket_width
        
        # SPAWN NEW FALLING OBJECTS
        spawn_timer += dt
        if spawn_timer > 1.0:  # Every 1 second
            # Random x position at top of screen
            new_x = random.randint(20, WIDTH - 20)
            new_y = 0
            # Choose random color
            colors = [RED, GREEN, BLUE, YELLOW]
            new_color = random.choice(colors)
            # Add to list: [x, y, color]
            falling_objects.append([new_x, new_y, new_color])
            spawn_timer = 0
        
        # MOVE FALLING OBJECTS DOWN
        for obj in falling_objects[:]:
            obj[1] += 3  # Move down (y gets bigger)
            
            # Check if caught by basket
            obj_x = obj[0]
            obj_y = obj[1]
            if (obj_y + 15 >= basket_y and 
                obj_x >= basket_x and 
                obj_x <= basket_x + basket_width):
                score += 10
                falling_objects.remove(obj)
            
            # Check if missed (fell off bottom)
            elif obj_y > HEIGHT:
                missed += 1
                falling_objects.remove(obj)
                if missed >= 10:
                    game_over = True
    
    # DRAW EVERYTHING
    screen.fill(BLACK)
    
    # Draw basket
    pygame.draw.rect(screen, WHITE, (basket_x, basket_y, basket_width, basket_height))
    
    # Draw falling objects
    for obj in falling_objects:
        pygame.draw.circle(screen, obj[2], (obj[0], obj[1]), 15)
    
    # Draw score and missed
    score_text = small_font.render(f"Score: {score}", True, GREEN)
    missed_text = small_font.render(f"Missed: {missed}/10", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))
    
    # Game over screen
    if game_over:
        game_over_text = font.render("GAME OVER!", True, RED)
        final_score = small_font.render(f"Final Score: {score}", True, WHITE)
        restart_text = small_font.render("Press R to Restart", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(final_score, (WIDTH // 2 - 120, HEIGHT // 2 + 10))
        screen.blit(restart_text, (WIDTH // 2 - 130, HEIGHT // 2 + 60))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
```

## Now run your code
# Challenges
## Challenge 1 - Colour Changer
Try out some new colours, make your game unique to the colours you like!

## Challenge 2 - Basket size?
Try making the basket a different size per level, do you make it harder or easier as the game goes on

## Challenge 3 - Object overload!
Make more objects spawn per level, how chaotic can you make it!
