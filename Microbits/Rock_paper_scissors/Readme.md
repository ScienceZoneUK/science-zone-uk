# Rock Paper Scissors

## Objectives
* Use gesture input with the micro:bit by detecting a shake to trigger gameplay.

* Use `randint()` to randomly select between Rock, Paper, and Scissors.
  
* Display images on the LED matrix to represent different hand gestures using `basic.show_leds()`.

* Play different sound effects using the music module to enhance the user experience.

* Use conditional logic `(if, elif, else)` to select and display the appropriate game outcome.

* Understand the use of variables to store and respond to changing game states.

* Build an interactive micro:bit game that responds to both movement and chance.

* Design intuitive visual and audio feedback to communicate outcomes effectively to users.

## 💻 Get Set Up
* Plug in your Micro:bit.
* Go to: python.microbit.org/v/3
* Start a new project.
## Step 1
Write a function that will run whenever the micro:bit is shaken.
```
def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```


## Step 2
Define a variable named `hand` outside the function and update it inside the gesture handler.
```
Python
hand = 0

def on_gesture_shake():
    global hand
    
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```
## Step 3
Inside the shake function, use randint(1, 3) to simulate a random choice:

* 1 for `Paper`
* 2 for `Rock`
* 3 for `Scissors`
  
```
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```
## Step 4
Use an `if` statement to check if `hand` is 1, and display a Paper icon using LEDs.

```
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```
## Step 5
Add a `music.play_sound_effect()` function call after displaying the Paper icon.
````
if hand == 1:
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
    """)
    music.play_sound_effect(music.create_sound_effect(
        WaveShape.NOISE, 4120, 1266, 255, 148, 500,
        SoundExpressionEffect.WARBLE,
        InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)

````
Now  SHAKE  If you try enough times, you should see a picture of paper on the screen.

### 🔍 **What you’ve done so far:**

In **Step 5**, you added an `if` condition to display **Paper** (`hand == 1`) and play a sound.

But your game has **three possible outcomes**:
1 = Paper
2 = Rock
3 = Scissors

Currently, only **Paper** is handled. So now, you’ll prepare your code to handle the **other cases**.

---

## Step 6
Add an ` else:` clause to handle other cases (Rock and Scissors). You can leave it empty for now or add a placeholder LED display.

```
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                4120,
                1266,
                255,
                148,
                500,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```




### 🧠 **What’s the goal of Step 6?**

* Add an `else:` block so your code **doesn’t ignore** values 2 and 3.
* This prepares your code to later show **Rock or Scissors**.

---

### 🧾 **What’s actually changing in the code?**

Before:

```python
if hand == 1:
    # show Paper
    ...
```

After:

```python
if hand == 1:
    # show Paper
    ...
else:
    # placeholder (for Rock or Scissors, to be added in next steps)
    pass
```

The `else:` block is used here as a **catch-all** — it will handle anything not equal to 1 (i.e., 2 or 3). For now, it's empty (using `pass`) so the code still runs, but does nothing for Rock or Scissors yet.

---

### 🧑‍💻 **Why use `else:` instead of more `if` statements right away?**

You're building your logic **step-by-step**. At this point:

* You **haven’t defined** what to do if `hand == 2` (Rock) or `hand == 3` (Scissors).
* So `else:` is a placeholder, keeping the code complete and error-free while you build it out.

---

### 🧪 Example Code from Step 6:

```python
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)

    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
        """)
        music.play_sound_effect(music.create_sound_effect(
            WaveShape.NOISE, 4120, 1266, 255, 148, 500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        pass  # Rock and Scissors logic to come later

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```

---

### 🧠 In Summary:

| Concept  | What You’re Learning                                                               |
| -------- | ---------------------------------------------------------------------------------- |
| `else:`  | Catches all values not handled by `if` (i.e., hand 2 or 3).                        |
| `pass`   | Placeholder so Python doesn’t throw an error for an empty block.                   |
| Planning | You're preparing the code structure before filling in logic for Rock and Scissors. |

---



## Step 7
Replace the placeholder else clause with an `elif` to check if `hand == 2` and display the Rock icon with a sound.
```
elif hand == 2:
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    """)
    music.play_sound_effect(music.create_sound_effect(
        WaveShape.SINE, 4417, 1, 0, 255, 266,
        SoundExpressionEffect.VIBRATO,
        InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)

```
## Step 8
Complete the else block to represent Scissors.
```
else:
    basic.show_leds("""
        # # . . #
        # # . # .
        . . # . .
        # # . # .
        # # . . #
    """)
    music.play_sound_effect(music.create_sound_effect(
        WaveShape.TRIANGLE, 1177, 4967, 0, 206, 266,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)


```
## Final Code
```
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)

    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
        """)
        music.play_sound_effect(music.create_sound_effect(
            WaveShape.NOISE, 4120, 1266, 255, 148, 500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)

    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
        """)
        music.play_sound_effect(music.create_sound_effect(
            WaveShape.SINE, 4417, 1, 0, 255, 266,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)

    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
        """)
        music.play_sound_effect(music.create_sound_effect(
            WaveShape.TRIANGLE, 1177, 4967, 0, 206, 266,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

```
🧪 Try It Out

* Upload the code to your micro:bit or use the simulator.

* Shake the micro:bit to see a random gesture and hear a corresponding sound.

* Play Rock, Paper, Scissors with a friend!

