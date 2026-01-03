import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
ORANGE = (255, 140, 0)
YELLOW = (255, 215, 0)
GREEN = (50, 205, 50)
BLUE = (30, 144, 255)
PURPLE = (138, 43, 226)
CYAN = (0, 255, 255)

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

class Paddle:
    def __init__(self):
        self.width = 120
        self.height = 15
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 40
        self.speed = 8
        self.color = WHITE
        
    def move(self, mouse_x):
        self.x = mouse_x - self.width // 2
        self.x = max(0, min(self.x, WIDTH - self.width))
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=5)
        pygame.draw.rect(screen, CYAN, (self.x, self.y, self.width, self.height), 2, border_radius=5)

class Ball:
    def __init__(self):
        self.radius = 8
        self.reset()
        
    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        angle = random.uniform(-45, 45)
        speed = 6
        self.dx = speed * (1 if random.random() > 0.5 else -1)
        self.dy = -speed
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Wall collision
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1
            
    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius - 2)

class Brick:
    def __init__(self, x, y, color, points):
        self.x = x
        self.y = y
        self.width = 75
        self.height = 25
        self.color = color
        self.points = points
        self.alive = True
        
    def draw(self):
        if self.alive:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=3)
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2, border_radius=3)

def create_bricks(level):
    bricks = []
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    rows = min(6 + level, 10)
    
    for row in range(rows):
        for col in range(10):
            x = col * 80 + 5
            y = row * 30 + 60
            color = colors[row % len(colors)]
            points = (6 - row % 6) * 10
            bricks.append(Brick(x, y, color, points))
    
    return bricks

def check_collision(ball, paddle, bricks):
    # Paddle collision
    if (ball.y + ball.radius >= paddle.y and 
        ball.x >= paddle.x and ball.x <= paddle.x + paddle.width):
        if ball.dy > 0:
            ball.dy *= -1
            # Add spin based on where ball hits paddle
            hit_pos = (ball.x - paddle.x) / paddle.width
            ball.dx = (hit_pos - 0.5) * 10
    
    # Brick collision
    for brick in bricks:
        if brick.alive:
            if (ball.x + ball.radius >= brick.x and 
                ball.x - ball.radius <= brick.x + brick.width and
                ball.y + ball.radius >= brick.y and 
                ball.y - ball.radius <= brick.y + brick.height):
                
                brick.alive = False
                ball.dy *= -1
                return brick.points
    return 0

def main():
    paddle = Paddle()
    ball = Ball()
    level = 1
    bricks = create_bricks(level)
    score = 0
    lives = 3
    game_over = False
    win = False
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (game_over or win):
                    # Restart
                    paddle = Paddle()
                    ball = Ball()
                    level = 1
                    bricks = create_bricks(level)
                    score = 0
                    lives = 3
                    game_over = False
                    win = False
        
        if not game_over and not win:
            # Move paddle with mouse
            mouse_x, _ = pygame.mouse.get_pos()
            paddle.move(mouse_x)
            
            # Move ball
            ball.move()
            
            # Check collisions
            points = check_collision(ball, paddle, bricks)
            score += points
            
            # Check if ball fell
            if ball.y - ball.radius > HEIGHT:
                lives -= 1
                if lives <= 0:
                    game_over = True
                else:
                    ball.reset()
            
            # Check if level complete
            if all(not brick.alive for brick in bricks):
                level += 1
                if level > 5:
                    win = True
                else:
                    bricks = create_bricks(level)
                    ball.reset()
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw bricks
        for brick in bricks:
            brick.draw()
        
        # Draw paddle and ball
        paddle.draw()
        ball.draw()
        
        # Draw UI
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 150, 10))
        screen.blit(level_text, (WIDTH // 2 - 50, 10))
        
        # Game over or win screen
        if game_over:
            game_over_text = font.render("GAME OVER!", True, RED)
            restart_text = small_font.render("Press SPACE to restart", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
            screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 20))
        
        if win:
            win_text = font.render("YOU WIN!", True, GREEN)
            final_score = font.render(f"Final Score: {score}", True, YELLOW)
            restart_text = small_font.render("Press SPACE to restart", True, WHITE)
            screen.blit(win_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
            screen.blit(final_score, (WIDTH // 2 - 120, HEIGHT // 2))
            screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 40))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
