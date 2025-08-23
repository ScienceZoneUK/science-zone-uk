## Step 1 Imports/ Initializing pygame

pygame → library for making games in Python (handles graphics, input, timing, etc.).

random → used for generating random numbers (block positions & speeds here).
```
import pygame
import random

# Initialize Pygame
pygame.init()
```
## Screen Setup and colours
```
# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Blocks")

# Colours
WHITE = (255, 255, 255)
RED = (200, 0, 0)

```
## Clock /Block Class
```

# Clock
clock = pygame.time.Clock()


class Block:
    def __init__(self):
        self.size = 30
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = random.randint(2, 6)

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))



```
## Main Game Loop
```
def main():
    run = True
    blocks = []
```
## Game Loop Body
```
    while run:
        clock.tick(60)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
```
## Spawn Blocks Randomly
```
        # Spawn new blocks randomly
        if random.randint(1, 30) == 1:
            blocks.append(Block())
```
## Update & Draw Blocks
```
        # Update and draw blocks
        for block in blocks[:]:
            block.update()
            block.draw(screen)
            if block.y > HEIGHT:
                blocks.remove(block)  # remove once it goes off-screen
```
## Update Display
```
        pygame.display.flip()

    pygame.quit()
```
## Entry Point
```
if __name__ == "__main__":
    main()
```
