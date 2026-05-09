```python
import tkinter as tk
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 300
GROUND_Y = 250

root = tk.Tk()
root.title("Dino Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


root.mainloop()
```


```python


# Ground
canvas.create_line(0, GROUND_Y, WIDTH, GROUND_Y, width=2)
```
```python
# Load Dino PNG
dino_image = Image.open("dino.png")

# Resize if needed
dino_image = dino_image.resize((50, 50))

dino_photo = ImageTk.PhotoImage(dino_image)

# Create Dino
dino = canvas.create_image(70, 225, image=dino_photo)
```
```python
velocity_y = 0
gravity = 1
jumping = False
```
```
# Obstacle
obstacle = canvas.create_rectangle(
    700, 220, 740, 250,
    fill="red"
)

game_over = False

def jump(event):
    global velocity_y, jumping

    if not jumping:
        velocity_y = -15
        jumping = True

root.bind("<space>", jump)

def get_dino_bbox():
    x, y = canvas.coords(dino)

    return (
        x - 25,
        y - 25,
        x + 25,
        y + 25
    )
```
```python
def game_loop():
    global velocity_y, jumping, game_over

    if game_over:
        return
```
```python
    # Apply gravity
    canvas.move(dino, 0, velocity_y)
    velocity_y += gravity

    # Dino position
    x1, y1, x2, y2 = get_dino_bbox()

    # Ground collision
    if y2 >= GROUND_Y:
        canvas.move(dino, 0, GROUND_Y - y2)
        velocity_y = 0
        jumping = False
```
```python
    # Move obstacle
    canvas.move(obstacle, -10, 0)

    obs = canvas.coords(obstacle)

    # Reset obstacle
    if obs[2] < 0:
        canvas.move(obstacle, WIDTH, 0)
```
```python
    # Collision detection
    overlap = not (
        x2 < obs[0] or
        x1 > obs[2] or
        y2 < obs[1] or
        y1 > obs[3]
    )

    if overlap:
        game_over = True

        canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text="GAME OVER",
            font=("Arial", 30),
            fill="black"
        )

    root.after(30, game_loop)

game_loop()

root.mainloop()
```
