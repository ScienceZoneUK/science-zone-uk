# Catch the Dot ⚫️
## Objectives


| Bloom’s Level        | Learning Objective                                                                                                                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 🔵 **Remembering**   | Pupils will be able to **define** what a Micro\:bit is and recall its main input/output features (buttons, LED display, accelerometer). |
| 🟢 **Understanding** | Pupils will be able to **describe** how a simple game loop works (input → update → output → repeat).                                    |
| 🟡 **Applying**      | Pupils will be able to **use** Micro\:bit buttons to control a paddle in the “Catch the Dot” game.                                      |
| 🟠 **Analysing**     | Pupils will be able to **compare** different strategies for catching the dot (e.g., moving early vs. waiting).                          |
| 🔴 **Evaluating**    | Pupils will be able to **justify** how scoring makes a game more engaging and how feedback (points up/down) motivates players.          |
| 🟣 **Creating**      | Pupils will be able to **design** their own variation of the game (e.g., faster dots, smaller paddle, or extra features like sounds).   |

---

## 🎮 Game Concept

* A **dot (ball)** falls from the top of the LED grid.
* The **paddle** is on the bottom row (y=4).
* Player moves the paddle left and right using **buttons A and B**.
* If the paddle catches the dot, score goes up.
* If it misses, score goes down.

## 🕹️ How to play

1. Paddle starts in the middle, dot spawns at a random x position on top row.
2. Press **A** = move paddle left, **B** = move paddle right.
3. Every 500 ms, the dot moves down one row.
4. If it lands on paddle → score +1. If missed → score -1.
5. Dot respawns at top, game continues endlessly.


✅ **Step 1: Connect your Micro\:bit**
Plug your Micro\:bit into your computer with the USB cable.
Open Google Chrome and go to: `python.microbit.org/v/3`
At the top, click the ⚡ **Connect** button, choose your Micro\:bit, and click **Connect**.

---

✅ **Step 2: Create the file & imports**
Create a new Python file in the editor and add the imports:

```python
from microbit import *
import random
```

Flash this tiny program (or keep it in the editor) so the editor is connected and ready.

---

✅ **Step 3: Set up the class and initial state**
Add the class and the `__init__` which sets paddle, dot and score:

```python
class CatchTheDot:
    def __init__(self):
        self.paddle_x = 2               # paddle left column (paddle occupies x and x+1)
        self.dot_x = random.randint(0, 4)
        self.dot_y = 0
        self.score = 0
```

Flash this to confirm no syntax errors.

---

✅ **Step 4: Draw the game to the LED grid**
Add the `draw()` method — clears screen, draws paddle and dot:

```python
    def draw(self):
        display.clear()
        display.set_pixel(self.paddle_x, 4, 9)
        if self.paddle_x < 4:
            display.set_pixel(self.paddle_x + 1, 4, 9)
        display.set_pixel(self.dot_x, self.dot_y, 5)
```

Flash and you should see a blank grid (or whatever positions are current).

---

✅ **Step 5: Move the paddle with buttons**
Add `move_paddle()` to read buttons A and B (non-blocking):

```python
    def move_paddle(self):
        if button_a.was_pressed() and self.paddle_x > 0:
            self.paddle_x -= 1
        if button_b.was_pressed() and self.paddle_x < 3:
            self.paddle_x += 1
```

Press A/B while flashing to check the method (it’s polled inside the loop later).

---

✅ **Step 6: Make the dot fall and handle catch/miss**
Add `update_dot()` — moves the dot down, checks landing, updates score and respawns:

```python
    def update_dot(self):
        self.dot_y += 1
        if self.dot_y > 4:                        # dot landed (passed bottom)
            if self.paddle_x <= self.dot_x <= self.paddle_x + 1:
                self.score += 1                   # caught
            else:
                self.score -= 1                   # missed
            self.dot_x = random.randint(0, 4)     # respawn at top
            self.dot_y = 0
```

Flash & test by letting the dot fall (you’ll need the full loop for visible animation).

---

✅ **Step 7: The main game loop**
Add `play()` which runs the per-frame sequence: input → update → draw → pause.

```python
    def play(self):
        while True:
            self.move_paddle()    # 1) handle button input
            self.update_dot()     # 2) move dot and check catch/miss
            self.draw()           # 3) update LEDs
            sleep(500)            # 4) pause (controls fall speed)
```

Flash — the dot will now fall, you can press A/B to move the paddle.

---

✅ **Step 8: Create and start the game**
At the bottom of the file, create the object and start playing:

```python
game = CatchTheDot()
game.play()
```

Flash the whole file to your Micro\:bit and play: press A/B to move and try to catch the falling dot.

---

✅ **Step 9: Quick tweaks & tips**

* If the dot appears to jump immediately (you want it shown at the top first), swap the order in `play()` to call `draw()` before `update_dot()`.
* To make it harder, reduce `sleep(500)` to `sleep(350)` or lower.
* To show the score when it changes, add `display.scroll(str(self.score))` after updating `self.score` in `update_dot()` (note: scrolling pauses the game).
* To make the paddle single-pixel and use tilt controls instead of buttons, replace `move_paddle()` with accelerometer logic.

---

