# Geometry Dash Flying Game in Pygame

This is a simple game where the player flies through a cave, avoiding obstacles like in Geometry Dash. The goal is to try and collect the coins and not crash.

## Today's Goals:

* Edit the colours and the generation of the cave
* Change the speed, size and gravity of the player
* Add in a Coin class to add score to the game
* Add in "Evil Coins"/obstacles that kill the player

## Constants and Imports

We need to start by importing libaries that we need for our game such as Pygame etc.
And we need to add in some **constants** to use later on in the program.

*a constant is any named value that remains unchanged throughout the program, unlike variables which can change*

Copy this code into your python editor!

```python
import random
import pygame
import math

import background

colours = {
    "cave": (0, 0, 0),
    "walls": (30, 30, 30),
    "player": (255, 255, 255),
}

DISPLAY_SIZE = [1000, 700]
PLAYER_SIZE = [50, 50]
PLAYER_RECT = [
    round(DISPLAY_SIZE[0]/2 - PLAYER_SIZE[0]/2),
    round(DISPLAY_SIZE[1]/2 - PLAYER_SIZE[1]/2),
    PLAYER_SIZE[0], PLAYER_SIZE[1]]
PLATFORM_HEIGHT = 20
GRAVITY = -0.01
```


## Player Code

Next we need to define our player with its attributes and methods
A method is a function defined in the class, something that the player can do. Whereas an attribute is an instance variable defined in the class eg the players speed

First you must initalise the class to define its attributes:
Copy this code into your python editor!

```python
class Player:
    def __init__(self, rect, colour):
        self.rect = pygame.Rect(rect)
        self.vector = [0, 0]
        self.angle = .5 
        self.speed = 10  
        self.colour = colour
```

Classes also need an "update" method as everything inside the game loop must update every frame

```python
    def update(self, objects):
        delta_x = self.speed*math.sin(self.angle * math.pi)
        delta_y = self.speed*math.cos(self.angle * math.pi)

        self.move(0, 0, [])

        return [delta_x, delta_y]
```

These methods are for moving the player and implementing gravity in the game:

```python
    def move(self, dx, dy, objects):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, objects)
        if dy != 0:
            self.move_single_axis(0, dy, objects)

        self.apply_gravity()

    def move_single_axis(self, dx, dy, objects):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in objects:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
    
    def apply_gravity(self):
        self.move_clockwise()

    def move_clockwise(self, amount=-0.01):
        self.move_angle(amount)
        self.rollover_angle()

    def rollover_angle(self):
        # This ensures the angle stays between 0 and 2pi (360 degrees).
        if self.angle <= 0:
            self.angle = 2
        elif self.angle >= 2:
            self.angle = 0

    def move_angle(self, amount):
        self.angle += amount
        
    def move_anticlockwise(self,  amount=0.02):
        self.move_angle(amount)
        self.rollover_angle()

```

Finally every class needs a draw method so that we can actually see what each object looks like!

```python
    def draw(self, display):
        pygame.draw.ellipse(display, self.colour, self.rect)
```

## The Game Loop

We must define a function that starts the program's **Game Loop**
The Game loop is a **while** loop that runs until a condition is met. We are going to make the game loop end when the player hits the walls.

At the start of the main function, we must setup the game- creating the background and player, screen size etc
Copy this code into your python editor!

```python
def main():
    pygame.init()
    display = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("SAM IS THE BEST SENSEI")
    clock = pygame.time.Clock()
    FPS = 30

    cave = background.Cave(display.get_rect(), 20, colours["cave"])

    player = Player(PLAYER_RECT, colours["player"])
    distance = 0
    score = 0
```

Now we create the while loop to keep the game running.

```python
    end = False
    while not end:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
```

Put this right at the end of the code, this allows us to run the game from the command prompt.

```python
if __name__ == "__main__":
    main()
```

## Try and run the game and see what happens!

Open the file where your code is stored inside of the command prompt.
Run "py main.py" in the command prompt to test your game! 


## Continuing the Game Loop

Next we need to add controls to our game, using pygame key events to detect whether keys are pressed to move the player.

Copy this code into your python editor!

```python
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.move_anticlockwise()
        if keys[pygame.K_s]:
            print("%s - %s" % (distance, score))
```

Update the player and calculate its speed and moment to move the background along with the player

```python
        # Logic
        movement = player.update([])
        distance += round(movement[0] / 10)

        # Covert to move landscape
        movement[0] = -movement[0]
        movement[1] = -movement[1]

```

Add in a check for collision to end the game if the player touches a wall

```python
        hit = cave.update(movement, player)
        if hit:
            end = True
```

Draw everything into our game window!

```python
        # Drawing
        display.fill(colours["walls"])

        cave.draw(display)
        player.draw(display)

        pygame.display.update()
        clock.tick(FPS)
```

## Try and run the game and see what happens!

Run "py main.py" in the command prompt to test your game! 



## Adding a Coin Class

Add a new class, a coin collectable that increases the score when the player collides with the class

Copy this code into your python editor!

```python
class Coin:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.colour = (200, 200, 0)

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def check_collide(self, player):
        if self.rect.colliderect(player.rect):
            return True
        return False

    def draw(self, display):
        pygame.draw.circle(display, self.colour, self.rect.center, round(self.rect.width/2))
```

## Spawn and update the coins

We need to create another new class to update and keep track of all the coins in the game
It does this by having a "spawn" method to create mulitple coins and an update method to move the coins.

Copy this code into your python editor!

```python
class CoinManager:
    def __init__(self, boundary):
        self.boundary = pygame.Rect(boundary)
        self.coins = []
        self.spawn_chance = 0.02

    def spawn(self, cave):
        current_piece = cave.pieces[len(cave.pieces) - 1]
        x = current_piece.rect.x
        y = random.randint(current_piece.rect.y, current_piece.rect.bottom)

        coin = Coin([x, y, cave.size, cave.size])
        self.coins.append(coin)

    def update(self, movement, player, cave):
        score = 0

        for coin in self.coins:
            coin.move(movement)

            if coin.check_collide(player):
                score += 1
                self.delete(coin)

            elif self.check_delete(coin):
                self.delete(coin)

        if self.check_spawn():
            self.spawn(cave)

        return score
```

We need some additional methods to check and delete coins

```python
  def check_spawn(self):
        if random.random() <= self.spawn_chance:
            return True
        return False

    def check_delete(self, coin):
        if not self.boundary.colliderect(coin.rect):
            return True

    def delete(self, coin):
        self.coins.remove(coin)
```

Finally we need to have a draw method to draw every coin in the game

```python
    def draw(self, display):
        for coin in self.coins:
            coin.draw(display)
```


## Update the Game Loop
We need to add the coin manager to our game loop to add coins into our game.
Add in these new lines of code next to the commented lines of code!

Start with creating the coin manager to spawn and update the coins

```python
    #cave = background.Cave(display.get_rect(), 20, colours["cave"])
    
    coin_manager = CoinManager(display.get_rect())

    #player = Player(PLAYER_RECT, colours["player"])
```

Keep track of the score by using the coin managers update function!

```python
        #movement[1] = -movement[1]

        score += coin_manager.update(movement, player, cave)
        
        #hit = cave.update(movement, player)
```

Make sure to use the draw method so that we can see all of the coins in our game

```python
        #cave.draw(display)
        coin_manager.draw(display)
        #player.draw(display)
```

## Display the Score

Make sure to display the score so right at the end of the game loop, add this code to draw the score varaible onto the screen
Copy this code into your python editor!

```python
        #Drawing
        #display.fill(colours["walls"])

        #cave.draw(display)
        #coin_manager.draw(display)
        #player.draw(display)

        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render("Score: " + str(score), True, (255, 0 ,0))
        display.blit(txtsurf,(100 - txtsurf.get_width() // 2, 50 - txtsurf.get_height() // 2))
```

## Try and run the game and see what happens!

Run "py main.py" in the command prompt to test your game! 


## Challenge 1: Player Tail
Time to make the player sprite more interesting!
We are going to add a tail to our player by using a list and an update method

Copy this code into your python editor!

```python
        #self.colour = colour
        self.tail = []
        self.tail_decay = 1
```

Using a list to store all the parts to the tail, this update method goes through the tail list and moves every part of the tail
And it also copies the player and adds itself to the tail, keeping it going

```python
    def update_tail(self, dx, dy):
        for rect in self.tail:

            rect.move_ip(dx, dy)
            rect.inflate_ip(-self.tail_decay, -self.tail_decay)
            if rect.width <= self.tail_decay or rect.height <= self.tail_decay:
                self.tail.remove(rect)

        self.tail.append(self.rect.copy())
```

Inside Player's update method, add in the tail update method so the tail is created within the game loop

```python
        #self.move(0, 0, [])
        self.update_tail(-delta_x, -delta_y)
        #return [delta_x, delta_y]
```

Inside the Player's draw method, add a for loop to cycle through every part of the tail and draw it onto the screen

```python
        #pygame.draw.ellipse(display, self.colour, self.rect)

        for rect in self.tail:
            pygame.draw.ellipse(display, self.colour, rect)
```

## Challenge 2: Edit and change the colours

To add new colours, at the start of the program add in this list of colours.

Copy this code into your python editor!


```python
tail_colours = [(200, 200, 0), (255, 0, 0), (255, 165, 0)]
```

Update and change how the tail is drawn, pick a random colour from the list and add it to the tail colour

```python
        for rect in self.tail:
            tailcolour = random.choice(tail_colours)
            pygame.draw.ellipse(display, tailcolour, rect)
```

## Challenge 3: Add evil coins

An easy way to add a new version of a coin is to copy the old one and make slight changes.
Copy this code into your python editor!

```python
class evilCoin:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.colour = (255, 0, 0)

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def check_collide(self, player):
        if self.rect.colliderect(player.rect):
            return True
        return False

    def draw(self, display):
        pygame.draw.circle(display, self.colour, self.rect.center, round(self.rect.width/2))
```

Inside the coin manager class, add a list for the evil coins

```python
    #def __init__(self, boundary):
        #self.boundary = pygame.Rect(boundary)
        #self.coins = []
        #self.spawn_chance = 0.02

        self.evilCoins = []
```

Again insde the coin manager class, we need to create a new method for spawning the evil coins

```python
    def evil(self, cave):
        current_piece = cave.pieces[len(cave.pieces) - 1]
        x = current_piece.rect.x
        y = random.randint(current_piece.rect.y, current_piece.rect.bottom)

        evilCoin = evilCoin([x, y, cave.size, cave.size])
        self.evilCoins.append(evilCoin)
```

In the coin manager update method, we have to loop through the evil coins and make sure to spawn them along with the normal coins

```python
    #def update(self, movement, player, cave):
        #score = 0
        #for coin in self.coins:
            #coin.move(movement)

            #if coin.check_collide(player):
                #score += 1
                #self.delete(coin)

            #elif self.check_delete(coin):
                #self.delete(coin)

        for evilCoin in self.evilCoins:
            evilCoin.move(movement)

            if evilCoin.check_collide(player):
                score -= 1
                self.evilCoins.remove(evilCoin)

            elif self.check_delete(evilCoin):
                self.evilCoins.remove(evilCoin)

        #if self.check_spawn():
            #self.spawn(cave)
            self.evil(cave)

        #return score
```

Make sure to update the draw method to draw in all of the evil coins aswell!

```python
    #def draw(self, display):
        #for coin in self.coins:
            #coin.draw(display)

        for coin in self.evilCoins:
            coin.draw(display)
```


