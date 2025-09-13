# Whack-a-Mole — step-by-step breakdown

Nice choice — here’s a clear, line-by-line explanation of how the class you have works, what each method does, why certain values were chosen, and a few practical tweaks you can make.

---

## Quick summary

The program creates a `WhackAMole` class that:

1. Keeps track of a *cursor* (player) and a *mole* (target) on the 5×5 LED grid,
2. Moves the cursor by reading the accelerometer,
3. Lets the player press **A** to whack; score changes if cursor overlaps the mole, and
4. Runs a simple loop that updates the game every 200 ms.

---

## Step-by-step

### 1) Imports

```python
from microbit import *
import random
```

* `microbit` gives you `display`, `accelerometer`, `button_a`, `sleep()`, etc.
* `random` is used to place the mole randomly with `random.randint()`.

---

### 2) Class definition & constructor

```python
class WhackAMole:
    def __init__(self):
        self.cursor_x = 2
        self.cursor_y = 2
        self.mole_x = random.randint(0, 4)
        self.mole_y = random.randint(0, 4)
        self.score = 0
```

* `cursor_x/cursor_y` start at `(2,2)` — the centre of the 5×5 grid (indices 0..4).
* `mole_x/mole_y` are chosen randomly (0–4 inclusive). `random.randint(0,4)` includes both ends.
* `score` starts at 0.

---

### 3) `new_mole()` — pick a new mole location

```python
def new_mole(self):
    self.mole_x = random.randint(0, 4)
    self.mole_y = random.randint(0, 4)
```

* Picks a new random (x,y). It *may* choose the same spot as before; if you want to avoid repeats you can loop until it’s different (see tweaks below).

---

### 4) `draw()` — update the LED grid

```python
def draw(self):
    display.clear()
    display.set_pixel(self.mole_x, self.mole_y, 9)
    display.set_pixel(self.cursor_x, self.cursor_y, 5)
```

* `display.clear()` wipes the 5×5 display.
* `display.set_pixel(x,y,brightness)` sets a single LED (brightness 0–9). Brightness 9 = brightest for the mole; 5 = dimmer for cursor so the mole stands out.
* Coordinate system: `x` is horizontal (0 = left, 4 = right); `y` is vertical (0 = top, 4 = bottom).

---

### 5) `update_cursor()` — move the cursor by tilting

```python
def update_cursor(self):
    if accelerometer.get_x() < -300 and self.cursor_x > 0:
        self.cursor_x -= 1
    elif accelerometer.get_x() > 300 and self.cursor_x < 4:
        self.cursor_x += 1
    if accelerometer.get_y() < -300 and self.cursor_y > 0:
        self.cursor_y -= 1
    elif accelerometer.get_y() > 300 and self.cursor_y < 4:
        self.cursor_y += 1
```

* `accelerometer.get_x()` and `get_y()` return integers indicating tilt/acceleration.
* Thresholds `-300` / `300` decide how far you must tilt to move. If the reading crosses the threshold it moves the cursor one step in that direction.
* Bounds checks (`> 0`, `< 4`) keep the cursor inside the 5×5 grid.
* Note: repeated calls will move the cursor repeatedly if you hold a tilt — that’s how you “slide” the cursor.

---

### 6) `whack()` — register button press and score

```python
def whack(self):
    if button_a.was_pressed():
        if self.cursor_x == self.mole_x and self.cursor_y == self.mole_y:
            self.score += 1
            self.new_mole()
        else:
            self.score -= 1
```

* `button_a.was_pressed()` returns `True` if the A button was pressed *since the last check* and then clears that “pressed” flag. That lets you poll without blocking.
* If the cursor is exactly on the mole, score increments and a new mole spawns. Otherwise a penalty (`score -= 1`) is applied. (You can remove the penalty if you prefer.)

---

### 7) `play()` — main game loop

```python
def play(self):
    while True:
        self.update_cursor()
        self.whack()
        self.draw()
        sleep(200)
```

* Infinite loop: update movement, handle whack, redraw display, then `sleep(200)` ms.
* `sleep(200)` sets the game tick to 200 ms — which controls responsiveness. Larger values → slower reaction; smaller → more CPU and more sensitivity.

---

### 8) Running the game

```python
game = WhackAMole()
game.play()
```

* Creates the object and starts the game loop. The program will run until you reset/power off the micro\:bit.

---

## micro\:bit API notes (short)

* `display.set_pixel(x,y,brightness)` — `brightness` 0..9.
* `display.clear()` — clears LEDs.
* `accelerometer.get_x()` / `get_y()` — integer tilt/accel values; orientation depends how you hold the device. Test to confirm which direction corresponds to which sign.
* `button_a.was_pressed()` — non-blocking; returns True if pressed since last call.
* `sleep(ms)` — pause for `ms` milliseconds.
* `random.randint(a,b)` — inclusive of `a` and `b`.

---

## Common issues & simple fixes

* **Jitter / too many moves from one tilt:** add a short cooldown after moving or require a bigger threshold. Or move only when tilt crosses a threshold and previously was neutral (hysteresis).
* **Mole repeating same spot:** make `new_mole()` loop until the position changes.
* **Score not visible:** call `display.scroll(str(self.score))` whenever you want to show it (e.g., on hit or on game over).
* **Game duration:** add a time limit (use `running_time()` — returns milliseconds) and stop when the time expires, then show final score.

---

## Useful tweak examples

**Avoid repeating the same mole**

```python
def new_mole(self):
    while True:
        x = random.randint(0,4)
        y = random.randint(0,4)
        if x != self.mole_x or y != self.mole_y:
            self.mole_x, self.mole_y = x, y
            break
```

**Add a 30-second time limit and show final score**

```python
def play(self, time_limit_ms=30000):
    start = running_time()
    while running_time() - start < time_limit_ms:
        self.update_cursor()
        self.whack()
        self.draw()
        sleep(200)
    display.clear()
    display.scroll("Score:{}".format(self.score))
```

**Give visual feedback on a hit**

```python
if self.cursor_x == self.mole_x and self.cursor_y == self.mole_y:
    self.score += 1
    for _ in range(2):
        display.set_pixel(self.mole_x, self.mole_y, 9)
        sleep(80)
        display.set_pixel(self.mole_x, self.mole_y, 0)
        sleep(80)
    self.new_mole()
```

---

If you want, I can:

* modify the class to include a timer and end-screen (full code),
* add sound effects, or
* change cursor control to buttons instead of tilt.


