<img width="1561" height="438" alt="image" src="https://github.com/user-attachments/assets/d18918f9-9735-4880-924b-1521dc5cdfb5" />

# Pygame Fundamentals
## Objective
- What is pygame and its history
- What is pygame and its uses
- Setting up our Game
- The Game Loop
- Quitting the Game loop
- Event Objects in Pygame
- Creating a Display Screen
- Pygame Colors
- Frames per second
## Pygame and its history
Pygame is a free and open-source library for making games and multimedia applications in Python. It helps us create 2D games by giving us tools to handle graphics, sounds and user input (like keyboard and mouse events) without needing to dig deep into complex stuff like graphics engines.

- Release date: 28 October 2000
- Programming languages: Python, C, Cython, Assembly language
- Developer: Pete Shinners
- License: GNU Lesser General Public License
- Stable release: 2.5.0 / 24 June 2023; 6 months ago
 ### What we can do with Pygame:
- Draw shapes, images and text on the screen
- Play music and sound effects
- Detect keyboard, mouse or joystick input
- Control the frame rate of your game
- Build simple 2D games like platformers, puzzles or shooter 
## Setting up our Game
We’ll begin this Python tutorial by explaining several core concepts related to the Pygame library and about creating games in general. Also keep in mind, that many of these concepts are transferable skills.  Should you switch to a more advanced game engine later many of these concepts will still hold true.
```python
import pygame
from pygame.locals import *
```
In the above code we begin importing pygame and it’s modules into our python program. The second line allows us to use the functions and variables in the pygame.locals module without having to add the lengthy pygame.locals prefix.
```python
pygame.init()
```
The init() function in pygame initializes the pygame engine. This line must be included before you begin writing any pygame code.
## The Game Loop
The Game Loop is where all the game events occur, update and get drawn to the screen. Once the initial setup and initialization of variables is out of the way, the Game Loop begins where the program keeps looping over and over until an event of type QUIT occurs.
Shown below is what a typical Game loop in Pygame looks like. Despite the fancy, it is just a simple “while” loop that runs infinitely.
```python
 #Game loop begins
while True:
      # Code
      # More Code
      .
      .
      pygame.display.update()
```
Changes in the game are not implemented until the pygame.display.update() function has been called. This function is responsible for updating your game window with any changes that have been made within that specific iteration of the game loop. It’s essential to place this within the game loop, to keep our display screen updated with the latest changes from every iteration.

We place it at the very end so that all possible changes to the Sprites on the screen have already taken place. We could call this more than once (e.g. every time we make a change in the game loop), but that would be more performance intensive and inefficient.
## Quitting the Game loop
Every game loop must have a end point, or some action that triggers the end point (such as clicking the quit button), else your game will run indefinetly.
```python
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```
We call both pygame.quit() and sys.exit() to close the pygame window and the python script respectively. Simply using sys.exit() can cause your IDE to hang due to a common bug. (Remember to import the sys library to use this function).
Note: If you didn’t import everything from pygame.locals as we did you would have to use pygame.locals.QUIT instead of QUIT. As you can see, it is more efficient to use this import statement.
## Event Objects in Pygame
A Pygame “Event” occurs when the user performs a specific action, such as clicking his mouse or pressing a keyboard button. Pygame records each and every event that occurs. However, it won’t really do anything with this information because that part is upto us to do.
We can find out which events have happened by calling the pygame.event.get() function (shown previously), which returns a list of pygame.event.Event objects (which we will just call Event objects for short).
One of the many attributes (or properties) held by event objects is type. The type attribute tells us what kind of event the object represents.
```python
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```
If you take a look at the example above again, you’ll see we used event.type == QUIT to determine whether the game was to be closed or not. We can even create our own custom events to signal certain types of events (such as an enemy spawning or a level up).
## Creating a Display Screen
For every game, we need to create a window of a fixed size by passing a tuple containing the width and height. This tuple is then passed into the display.set_mode() function.
```python	
DISPLAYSURF = pygame.display.set_mode((300,300))
```
In pygame and other game libraries, we regard the (0, 0) coordinate as the top-left most corner. Similarly, the maximum x-point and maximum y-point is the bottom-right corner. Which in this case is (300, 300).
The X-values grow larger as you move left to right, and the Y-values grow larger from top to bottom.

<img width="464" height="356" alt="image" src="https://github.com/user-attachments/assets/cacd6b4a-d4ce-40e6-a167-987504046d25" />

You can also customize this window later by changing it’s title and the default icon.

## Pygame Colors
Colors are going to be a big part of any game development framework or engine, so you should understand it well.
Pygame uses the typical RGB system of colors. To those who aren’t aware, this stand for Red, Green and Blue respectively. These three colors combined (in varying ratios) are used to create all the colors you see on computers, or any device that has a screen.
The values for each color range from 0 – 255, a total of 256 values. You can find the total number of possible color combinations by evaluating 256 x 256 x 256, which results in a value well over 16 million.
In order to use colors on Pygame, we first create Color objects using RGB values. RGB values must be in a tuple format, with three values, each corresponding to a respective color.
```python	
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
```
Shown above are examples of how we can create Colors. We will use these later on in our Pygame tutorial when we begin creating backgrounds or shapes.

## Frames per second
Computer’s are extremely fast and can complete millions of loop cycles in under a second. Now obviously, this is a little fast for us humans. As reference, movies are run at 24 frames per second. Anything less than that will have an obvious stutter to it, whereas values over 100 may cause the things to move too fast for us to see.
By default, if we do not create a limitation the computer will execute the game loop as many times as in can within a second. This is actually a major problem, because without a “limiter” the frame rate will fluctuate greatly throughout the game depending on what’s currently happening (number of objects on screen, player moving or not, etc.)
To limit it we use the tick(fps)method where fps is an integer. The tick() method belongs to the pygame.time.Clock class and must be used with an object of this class.
```python	
FPS = pygame.time.Clock()
FPS.tick(60)
```
This can vary from game to game, depending on how it was designed but you should aim for a value between 30 – 60. Keep in mind, that if you create a rather complex and heavy game the computer might not be able to run it well at higher frames.

## Rects & Collision Detection in Pygame
In every game, each object has fixed boundaries that define the space that it currently occupies. These fixed boundaries are essential when the object interacts or “collides” with other objects.
By defining these boundaries, the game is able to detect when two or more boundaries overlap or touch. This allows it to then handle the interact based on which objects are touching. Such as the Player picking up an item, or attacking another entity.

  <img width="54" height="98" alt="image" src="https://github.com/user-attachments/assets/b02b5458-88d4-498d-a4e1-6f38493662d4" />

Shown in the image above is a typical “rect” object (colored in black) around a Car. It’s not 100% accurate, as it does not full take on the shape of the Car but it is accurate enough for most purposes.
```python	
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
```
We can also check for a collision between a Rect and a pair of coordinates
```python
object1 = pygame.Rect((20, 50), (50, 100))
print(object1.collidepoint(50, 75))
```
There is another trick we can use to automatically create a Rect based off an image’s dimensions. We will explore this later on in this Pygame tutorial, when we create our game.

