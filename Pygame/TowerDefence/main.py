import pygame
import math
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Fonts
big_font = pygame.font.Font(None, 72)
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (125, 11, 74)
DARK_GREEN = (82, 5, 47)
RED = (220, 20, 60)
BLUE = (30, 144, 255)
YELLOW = (255, 215, 0)
ORANGE = (255, 140, 0)
PURPLE = (138, 43, 226)
GRAY = (100, 100, 100)

# The path enemies follow
path = [(50, 100), (200, 100), (200, 300), (400, 300),
        (400, 150), (600, 150), (600, 400), (800, 400),
        (800, 200), (950, 200)]

# ENEMY CLASS
class Enemy:
    def __init__(self, health):
        self.x = path[0][0]  # Start position
        self.y = path[0][1]
        self.health = health
        self.max_health = health
        self.speed = 2
        self.path_step = 0  # Which part of path we're on
        self.alive = True
        self.escaped = False  # Did it reach the end?
        
    def move(self):
        # Check if at the end
        if self.path_step >= len(path) - 1:
            self.escaped = True
            self.alive = False
            return
        
        # Move toward next point on path
        target_x = path[self.path_step + 1][0]
        target_y = path[self.path_step + 1][1]
        
        # Calculate direction
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Move along path
        if distance < self.speed:
            self.path_step += 1
        else:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
    
    def draw(self):
        # Draw enemy circle
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 15)
        
        # Draw health bar above enemy
        bar_width = 30
        health_percent = self.health / self.max_health
        pygame.draw.rect(screen, RED, (self.x - 15, self.y - 25, bar_width, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 15, self.y - 25, bar_width * health_percent, 5))

# TOWER CLASS
class Tower:
    def __init__(self, x, y, tower_type):
        self.x = x
        self.y = y
        self.type = tower_type
        
        # Set tower stats based on type
        if tower_type == "basic":
            self.damage = 20
            self.range = 120
            self.shoot_speed = 1.0  # Seconds between shots
            self.color = BLUE
            self.cost = 100
        elif tower_type == "fast":
            self.damage = 10
            self.range = 100
            self.shoot_speed = 0.4
            self.color = ORANGE
            self.cost = 150
        elif tower_type == "strong":
            self.damage = 50
            self.range = 150
            self.shoot_speed = 2.0
            self.color = PURPLE
            self.cost = 200
        
        self.time_since_shot = 0
        
    def update(self, enemies, dt):
        self.time_since_shot += dt
        
        # Can we shoot?
        if self.time_since_shot >= self.shoot_speed:
            # Find closest enemy in range
            for enemy in enemies:
                if enemy.alive:
                    distance = math.sqrt((enemy.x - self.x)**2 + (enemy.y - self.y)**2)
                    if distance <= self.range:
                        # Shoot the enemy!
                        enemy.take_damage(self.damage)
                        self.time_since_shot = 0
                        return True
        return False
    
    def draw(self, show_range=False):
        # Draw range circle if selected
        if show_range:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 30), (int(self.x), int(self.y)), self.range)
            screen.blit(s, (0, 0))
        
        # Draw tower
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 20)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 20, 2)

# DRAW THE PATH
def draw_path():
    for i in range(len(path) - 1):
        pygame.draw.line(screen, DARK_GREEN, path[i], path[i + 1], 40)
    
    # Start (green circle)
    pygame.draw.circle(screen, GREEN, path[0], 25)
    # End (red circle)
    pygame.draw.circle(screen, RED, path[-1], 25)

# DRAW GAME INFO AT TOP
def draw_info(money, lives, wave, enemies_left):
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 60))
    
    money_text = font.render(f"Money: ${money}", True, YELLOW)
    lives_text = font.render(f"Lives: {lives}", True, RED)
    wave_text = font.render(f"Wave: {wave}", True, WHITE)
    
    screen.blit(money_text, (10, 15))
    screen.blit(lives_text, (200, 15))
    screen.blit(wave_text, (380, 15))
    
    if enemies_left > 0:
        enemy_text = small_font.render(f"Enemies: {enemies_left}", True, WHITE)
        screen.blit(enemy_text, (550, 20))

# DRAW TOWER SHOP
def draw_shop(money, selected_type):
    x = WIDTH - 180
    y = 80
    
    # Shop background
    pygame.draw.rect(screen, GRAY, (x - 10, y - 10, 170, 280))
    pygame.draw.rect(screen, WHITE, (x - 10, y - 10, 170, 280), 2)
    
    title = font.render("SHOP", True, WHITE)
    screen.blit(title, (x + 35, y))
    
    # Tower buttons
    towers = [
        ("basic", BLUE, 100, "Basic"),
        ("fast", ORANGE, 150, "Fast"),
        ("strong", PURPLE, 200, "Strong")
    ]
    
    for i, (tower_type, color, cost, name) in enumerate(towers):
        button_y = y + 50 + i * 70
        
        # Check if we can afford it
        can_afford = money >= cost
        button_color = color if can_afford else (100, 100, 100)
        
        # Highlight if selected
        if selected_type == tower_type:
            pygame.draw.rect(screen, YELLOW, (x - 5, button_y - 5, 160, 60), 3)
        
        # Draw button
        pygame.draw.rect(screen, button_color, (x, button_y, 150, 50))
        pygame.draw.rect(screen, WHITE, (x, button_y, 150, 50), 2)
        
        # Tower preview circle
        pygame.draw.circle(screen, color, (x + 25, button_y + 25), 15)
        
        # Text
        name_text = small_font.render(name, True, WHITE)
        cost_text = small_font.render(f"${cost}", True, YELLOW if can_afford else RED)
        screen.blit(name_text, (x + 50, button_y + 10))
        screen.blit(cost_text, (x + 50, button_y + 30))
      
# MAIN GAME
def main():
    # Game variables
    money = 500
    lives = 20
    wave = 1
    
    towers = []
    enemies = []
    
    selected_tower_type = None
    show_tutorial = True  # Set to False to skip tutorial
    game_over = False
    
    # Wave control
    wave_active = False
    enemies_to_spawn = 10
    enemies_spawned = 0
    spawn_timer = 0
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Tutorial screen click (OPTIONAL - can be removed)
            if event.type == pygame.MOUSEBUTTONDOWN and show_tutorial:
                button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 100, 300, 60)
                if button.collidepoint(mouse_x, mouse_y):
                    show_tutorial = False
            
            # Game clicks
            if event.type == pygame.MOUSEBUTTONDOWN and not show_tutorial and not game_over:
                # Check shop
                shop_x = WIDTH - 180
                shop_y = 80
                
                tower_info = [("basic", 100), ("fast", 150), ("strong", 200)]
                
                for i, (tower_type, cost) in enumerate(tower_info):
                    button_y = shop_y + 50 + i * 70
                    if shop_x <= mouse_x <= shop_x + 150 and button_y <= mouse_y <= button_y + 50:
                        if money >= cost:
                            selected_tower_type = tower_type
                
                # Place tower on map
                if selected_tower_type and mouse_x < WIDTH - 200 and mouse_y > 60:
                    # Check if spot is valid (not too close to other towers)
                    can_place = True
                    for tower in towers:
                        distance = math.sqrt((tower.x - mouse_x)**2 + (tower.y - mouse_y)**2)
                        if distance < 50:
                            can_place = False
                    
                    if can_place:
                        new_tower = Tower(mouse_x, mouse_y, selected_tower_type)
                        if money >= new_tower.cost:
                            towers.append(new_tower)
                            money -= new_tower.cost
                            selected_tower_type = None
            
            # Keyboard
            if event.type == pygame.KEYDOWN:
                # Start wave
                if event.key == pygame.K_SPACE and not wave_active and not show_tutorial and not game_over:
                    wave_active = True
                    enemies_spawned = 0
                    spawn_timer = 0
                
                # Restart game
                if event.key == pygame.K_r and game_over:
                    money = 500
                    lives = 20
                    wave = 1
                    towers = []
                    enemies = []
                    wave_active = False
                    game_over = False
                    #
                    enemies_to_spawn = 10
                    enemies_spawned = 0
        
        # Show tutorial (OPTIONAL - can be removed)
        
        # Game logic
        if not game_over:
            # Spawn enemies during wave
            if wave_active:
                spawn_timer += dt
                if spawn_timer >= 1.5 and enemies_spawned < enemies_to_spawn:
                    enemy_health = 50 + wave * 10
                    enemies.append(Enemy(enemy_health))
                    enemies_spawned += 1
                    spawn_timer = 0
            
            # Move enemies
            for enemy in enemies[:]:
                enemy.move()
                if enemy.escaped:
                    lives -= 1
                    enemies.remove(enemy)
                    if lives <= 0:
                        game_over = True
                elif not enemy.alive:
                    money += 25
                    enemies.remove(enemy)
            
            # Towers shoot
            for tower in towers:
                tower.update(enemies, dt)
            
            # Check if wave complete
            if wave_active and enemies_spawned >= enemies_to_spawn and len(enemies) == 0:
                wave_active = False
                wave += 1
                enemies_to_spawn += 2
                money += 100
        
        # Draw everything
        screen.fill((51, 6, 31))
        draw_path()
        
        # Draw towers
        for tower in towers:
            tower.draw()
        
        # Draw enemies
        for enemy in enemies:
            enemy.draw()
        
        # Draw UI
        draw_info(money, lives, wave, len(enemies))
        draw_shop(money, selected_tower_type)
        
        # Instructions
        if not wave_active and not game_over:
            text = font.render("Press SPACE to start wave!", True, YELLOW)
            screen.blit(text, (WIDTH // 2 - 180, HEIGHT - 40))
        
        # Game over screen
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            game_over_text = big_font.render("GAME OVER!", True, RED)
            wave_text = font.render(f"You survived {wave - 1} waves!", True, WHITE)
            restart_text = small_font.render("Press R to restart", True, WHITE)
            
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 60))
            screen.blit(wave_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))
            screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 60))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
