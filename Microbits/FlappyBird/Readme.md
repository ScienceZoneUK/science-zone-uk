# Flappy Bird
## Objectives

### 1. **Creating and Controlling Sprites**

* **Objective:** Learn how to create and control sprites (characters or objects in the game) on the Micro\:bit LED display.
* **Skills:**

  * Creating a sprite with `game.create_sprite()`.
  * Changing the sprite’s properties like position (`LedSpriteProperty.X` and `LedSpriteProperty.Y`).
  * Making the sprite blink or change its appearance using `LedSpriteProperty.BLINK`.

---

### 2. **Using Buttons for Input**

* **Objective:** Understand how to use input from buttons (A and B) to interact with the game.
* **Skills:**

  * Setting up event handlers for button presses using `input.on_button_pressed()`.
  * Modifying sprite positions based on user input (e.g., moving the bird up and down when buttons A and B are pressed).

---

### 3. **Randomization in Games**

* **Objective:** Learn how to use randomness to generate obstacles in the game, creating a dynamic and unpredictable experience.
* **Skills:**

  * Using `randint()` to generate random values (e.g., determining the hole's position in the obstacle grid).
  * Dynamically creating new obstacles at random intervals to keep the game challenging.

---

### 4. **Game Logic and Collision Detection**

* **Objective:** Understand how to check for collisions between objects and trigger game events (like game over).
* **Skills:**

  * Checking if the positions of the bird and obstacles overlap to detect a collision.
  * Using `game.game_over()` to end the game when a collision occurs.

---

### 5. **Using Arrays to Manage Game Elements**

* **Objective:** Learn how to manage multiple game elements (like obstacles) using arrays (lists).
* **Skills:**

  * Storing multiple obstacle sprites in a list (`obstacles: List[game.LedSprite]`).
  * Iterating over the array using loops to move and update each obstacle.

---

### 6. **Creating a Scoring System**

* **Objective:** Implement a scoring system to track player progress and display the score on the LED screen.
* **Skills:**

  * Using a variable to store the score (`score`).
  * Incrementing the score when certain conditions are met (e.g., when an obstacle passes the bird).
  * Displaying the score on the LED grid using `display.show()`.

---

### 7. **Game Timing and Speed Control**

* **Objective:** Learn how to control the speed of the game and obstacles using timing and loops.
* **Skills:**

  * Using `sleep()` (or `basic.pause()`) to create a delay between actions, controlling the speed of the game.
  * Making obstacles move faster over time by adjusting the pause time based on the game's progress.

---

### 8. **Using Loops and Conditional Logic**

* **Objective:** Master using loops and conditional logic to control the flow of the game.
* **Skills:**

  * Using `for` loops to iterate over obstacles and perform actions like moving them.
  * Implementing `if` statements to check for specific conditions (e.g., obstacle position, collision detection, game over).
  * Creating infinite loops using `game.forever()` to continuously run the game.

---

### 9. **Basic Game Design and Mechanics**

* **Objective:** Learn how to build a simple game with core mechanics, including sprite movement, collision detection, and scoring.
* **Skills:**

  * Designing a game loop that continually updates the game state.
  * Managing game states (e.g., the game over condition).

---

### 10. **Improving Game Difficulty**

* **Objective:** Understand how to adjust game difficulty dynamically to keep the player engaged.
* **Skills:**

  * Increasing the speed of obstacles over time to make the game more challenging.
  * Adjusting the frequency of obstacle generation to increase game difficulty as the player progresses.

---

### **Bonus Objectives (Advanced):**

* **Implementing Sound Effects**: Learn how to use the Micro\:bit’s sound capabilities to add effects when the bird hits an obstacle or when the game starts/ends.
* **High Score System**: Implement a feature that tracks the highest score achieved in the game, even across different game sessions.

---

### **Summary of Skills to Be Learned:**

* **Game Design Fundamentals:** Creating game mechanics, scoring, and game-over logic.
* **Programming Techniques:** Random number generation, loops, conditional checks, and managing arrays.
* **Micro\:bit Hardware Interaction:** Handling button inputs, controlling sprites, and using the LED display.
* **Problem-Solving:** Implementing collision detection, speed control, and difficulty scaling.

---

By the end of this project, you'll have a solid foundation in game programming, problem-solving, and working with hardware interfaces (like the Micro\:bit's buttons and LED display). You'll also gain valuable experience in making games more engaging through dynamic difficulty and real-time interactions.


## Step 1: Add the Bird to the Game
First, we are going to add a sprite for the bird from the Game menu and make it blink.
```
bird: game.LedSprite = None
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)
```
## Step 2: Make the Bird fly
Before creating the code for the game actions, let’s first add some controls so that we can move around. We’ll control the bird by pressing the A button to go up or the B button to go down.
```
bird: game.LedSprite = None

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)
```
## Step 3: Generating obstacles
This is where things will start to get interesting. We’re going to randomly generate obstacles. We’ll keep all obstacles inside the array. All obstacles will have a single hole for the bird to fly through.

First, create an array of obstacles which will hold all of the obstacle sprites.
```
obstacles: List[game.LedSprite] = []
```
Now generate vertical obstacles consisting of 4 sprites and 1 random hole. Create new variable called emptyObstacleY. Using pick random, generate a random number from 0 to 4 and store it inside emptyObstacleY.

Using for loop, iterate from 0 to 4. For every coordinate not equal to emptyObstacleY create and add obstacle sprites to the end of the obstacles array.

```
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []
emptyObstacleY = randint(0, 4)
for index in range(5):
    if index != emptyObstacleY:
        obstacles.append(game.create_sprite(4, index))
```
Now with every micro:bit restart you should see different autogenerated vertical obstacles.

Before continuing, make sure that obstacles are generated randomly and that the bird is moving up and down.

```
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []
bird: game.LedSprite = None
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)
emptyObstacleY = randint(0, 4)
for index in range(5):
    if index != emptyObstacleY:
        obstacles.append(game.create_sprite(4, index))

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)
```

## Step 4: Make obstacles move
Access each obstacle using a for element loop (iterate over the obstacles array) and decrease the obstacle X coordinate by 1. Right click on the value block and rename it to obstacle ; then drag that obstacle block on top of sprite in the change x block.
```
obstacles: List[game.LedSprite] = []

def on_forever():
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)
    basic.pause(1000)
basic.forever(on_forever)
```
## Step 5: Make obstacles disappear
Make obstacles disappear after reaching leftmost corner. Iterate over all obstacles, delete the obstacle sprites where the X coordinate equals 0, and remove them from the obstacles array.
```
obstacles: List[game.LedSprite] = []

def on_forever():
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)
    basic.pause(1000)
basic.forever(on_forever)
```
## Step 6: Generate more obstacles
At the moment, our code generates just one vertical obstacle. We need to put obstacle generation code into the forever loop so that it keeps generating more and more obstacles.

```
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []

def on_forever():
    global emptyObstacleY
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)
    emptyObstacleY = randint(0, 4)
    for index in range(5):
        if index != emptyObstacleY:
            obstacles.append(game.create_sprite(4, index))
    basic.pause(1000)
basic.forever(on_forever)
```
Now our screen is full of moving obstacles. Create some spaces between generated obstacles. Let’s introduce a ticks variable to count how many iterations the forever loop has done and execute obstacle creation only if ticks is divisible by 3.
```
ticks = 0
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index in range(5):
            if index != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index))
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)
```
## Step 7: Game Over
Right now nothing happens when the bird is hit by obstacle. Fix this by iterating over the obstacles array and checking if any obstacle sprite coordinate equals the bird coordinate.
```
bird: game.LedSprite = None
ticks = 0
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index in range(5):
            if index != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index))
    for obstacle2 in obstacles:
        if obstacle2.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle2.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)
```
## Final Code
```
ticks = 0
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []
index = 0
bird: game.LedSprite = None

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

index = 0
obstacles = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index2 in range(5):
            if index2 != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index2))
    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)
```
## Challenge
Here are some additional features you can add to the game:

* Count and show the Crashy Bird game score.
* Make the obstacles move faster every time an obstacle is passed.
