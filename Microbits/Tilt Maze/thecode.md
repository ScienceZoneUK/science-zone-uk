```python
from microbit import *

class TiltMaze:
    def __init__(self):
        # Player starts at top-left corner
        self.player_x = 0
        self.player_y = 0

        # Define maze layout: 0 = empty, 1 = wall, 2 = goal
        self.maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 2]
        ]

    def draw(self):
        display.clear()
        for y in range(5):
            for x in range(5):
                if self.maze[y][x] == 1:       # wall
                    display.set_pixel(x, y, 3)
                elif self.maze[y][x] == 2:     # goal
                    display.set_pixel(x, y, 7)
        display.set_pixel(self.player_x, self.player_y, 9)  # player

    def move(self):
        x_tilt = accelerometer.get_x()
        y_tilt = accelerometer.get_y()

        # Move left/right
        if x_tilt < -300 and self.player_x > 0:
            if self.maze[self.player_y][self.player_x - 1] != 1:
                self.player_x -= 1
        elif x_tilt > 300 and self.player_x < 4:
            if self.maze[self.player_y][self.player_x + 1] != 1:
                self.player_x += 1

        # Move up/down
        if y_tilt < -300 and self.player_y > 0:
            if self.maze[self.player_y - 1][self.player_x] != 1:
                self.player_y -= 1
        elif y_tilt > 300 and self.player_y < 4:
            if self.maze[self.player_y + 1][self.player_x] != 1:
                self.player_y += 1

    def check_goal(self):
        return self.maze[self.player_y][self.player_x] == 2

    def play(self):
        while True:
            self.move()
            self.draw()
            if self.check_goal():
                display.show(Image.HAPPY)
                break
            sleep(300)


# Start the game
game = TiltMaze()
game.play()

```
