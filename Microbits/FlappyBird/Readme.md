Step 1: Add the Bird to the Game
First, we are going to add a sprite for the bird from the Game menu and make it blink.

bird: game.LedSprite = None
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

Step 2: Make the Bird fly
Before creating the code for the game actions, let’s first add some controls so that we can move around. We’ll control the bird by pressing the A button to go up or the B button to go down.

bird: game.LedSprite = None

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)
Step 3: Generating obstacles
This is where things will start to get interesting. We’re going to randomly generate obstacles. We’ll keep all obstacles inside the array. All obstacles will have a single hole for the bird to fly through.

First, create an array of obstacles which will hold all of the obstacle sprites.
```
obstacles: List[game.LedSprite] = []
```
Now generate vertical obstacles consisting of 4 sprites and 1 random hole. Create new variable called emptyObstacleY. Using pick random, generate a random number from 0 to 4 and store it inside emptyObstacleY.

Using for loop, iterate from 0 to 4. For every coordinate not equal to emptyObstacleY create and add obstacle sprites to the end of the obstacles array.
