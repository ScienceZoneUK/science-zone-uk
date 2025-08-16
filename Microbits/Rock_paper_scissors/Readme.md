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
## Step 7

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
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                4417,
                1,
                0,
                255,
                266,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)


hand = 0
```
## Step 8

```
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
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                4417,
                1,
                0,
                255,
                266,
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
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                1177,
                4967,
                0,
                206,
                266,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

```



