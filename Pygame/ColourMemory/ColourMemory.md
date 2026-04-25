# Colour Memory

## Imports
```
import pygame
import random
import sys
```

## Constants & Colours
```
pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Memory Match")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 50)
PURPLE = (200, 50, 255)
ORANGE = (255, 150, 50)

# Fonts
big_font = pygame.font.Font(None, 72)
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

```

## Set-up
```
# Game colors to remember
GAME_COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]

# Game state
game_state = "start"  # start, show, memorize, playing, correct, wrong, win
sequence = []
player_sequence = []
level = 1
score = 0

# Create colored squares (4x4 grid)
squares = []
for row in range(4):
    for col in range(4):
        # Only use 6 squares (3 pairs)
        if len(squares) < 6:
            x = 150 + col * 130
            y = 150 + row * 130
            # Add each color twice for matching pairs
            if len(squares) < 3:
                squares.append({"x": x, "y": y, "color": GAME_COLORS[len(squares)], "clicked": False})
            else:
                squares.append({"x": x, "y": y, "color": GAME_COLORS[len(squares) - 3], "clicked": False})

# Shuffle squares
random.shuffle(squares)

# Selected squares for matching
selected = []
show_timer = 0
wait_timer = 0
```

## Main
```
# MAIN GAME LOOP
running = True
while running:
    dt = clock.tick(60) / 1000.0
    
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Start screen
        if event.type == pygame.KEYDOWN and game_state == "start":
            if event.key == pygame.K_SPACE:
                game_state = "playing"
        
        # Playing - click squares
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == "playing":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Check which square was clicked
            for square in squares:
                if not square["clicked"]:
                    # Check if mouse is inside square
                    if (square["x"] <= mouse_x <= square["x"] + 100 and
                        square["y"] <= mouse_y <= square["y"] + 100):
                        
                        # Add to selected if not already selected
                        if square not in selected:
                            selected.append(square)
                            
                            # If 2 squares selected, check if they match
                            if len(selected) == 2:
                                if selected[0]["color"] == selected[1]["color"]:
                                    # Match!
                                    selected[0]["clicked"] = True
                                    selected[1]["clicked"] = True
                                    score += 10
                                    game_state = "correct"
                                    show_timer = 0.5
                                else:
                                    # No match
                                    game_state = "wrong"
                                    show_timer = 1.0
        
        # Restart
        if event.type == pygame.KEYDOWN and game_state == "win":
            if event.key == pygame.K_r:
                # Reset everything
                game_state = "start"
                score = 0
                selected = []
                for square in squares:
                    square["clicked"] = False
                random.shuffle(squares)
    
    # GAME LOGIC
    if game_state == "correct" or game_state == "wrong":
        show_timer -= dt
        if show_timer <= 0:
            selected = []
            game_state = "playing"
            
            # Check if all squares matched
            all_matched = True
            for square in squares:
                if not square["clicked"]:
                    all_matched = False
            
            if all_matched:
                game_state = "win"
    
    # DRAW EVERYTHING
    screen.fill(BLACK)
    
    # Draw title
    title = font.render("Color Memory Match", True, WHITE)
    screen.blit(title, (WIDTH // 2 - 200, 20))
    
    # Draw score
    score_text = small_font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (20, 20))
    
    # Start screen
    if game_state == "start":
        instructions = [
            "Match all the colored pairs!",
            "",
            "Click two squares to flip them",
            "Match all pairs to win!",
            "",
            "Press SPACE to start"
        ]
        
        y = 200
        for line in instructions:
            text = small_font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 2 - 200, y))
            y += 50
    
    # Playing - draw squares
    elif game_state in ["playing", "correct", "wrong"]:
        for square in squares:
            # Show color if clicked or selected
            if square["clicked"] or square in selected:
                pygame.draw.rect(screen, square["color"], 
                               (square["x"], square["y"], 100, 100))
            else:
                # Show gray back
                pygame.draw.rect(screen, GRAY, 
                               (square["x"], square["y"], 100, 100))
            
            # White border
            pygame.draw.rect(screen, WHITE, 
                           (square["x"], square["y"], 100, 100), 3)
        
        # Show feedback
        if game_state == "correct":
            feedback = font.render("MATCH!", True, GREEN)
            screen.blit(feedback, (WIDTH // 2 - 80, HEIGHT - 80))
        elif game_state == "wrong":
            feedback = font.render("Try Again!", True, RED)
            screen.blit(feedback, (WIDTH // 2 - 120, HEIGHT - 80))
    
    # Win screen
    elif game_state == "win":
        win_text = big_font.render("YOU WIN!", True, GREEN)
        final_score = font.render(f"Final Score: {score}", True, WHITE)
        restart = small_font.render("Press R to play again", True, WHITE)
        
        screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(final_score, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
        screen.blit(restart, (WIDTH // 2 - 150, HEIGHT // 2 + 40))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
```

### Now run your code

## Challenges
### Challenge 1
At the start, we set 9 colours.
Change the colours to your favourite palette or just swap some of the colour names in the rest of the code, up to you.

### Challenge 2
Change the number of squares, either make the pairs increase per level or randomise the tile location.

### Challenge 3
Change how many lives you have and change the next level criteria.
