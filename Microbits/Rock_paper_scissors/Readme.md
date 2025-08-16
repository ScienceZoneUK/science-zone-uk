# Rock Paper Scissors

## Objectives
* Use gesture input with the micro:bit by detecting a shake to trigger gameplay.

* Generate random numbers in MicroPython to simulate random choices (rock, paper, or scissors).

* Display images on the LED matrix to represent different hand gestures.

* Play different sound effects using the music module to enhance the user experience.

* Use conditional logic (if, elif, else) to select and display the appropriate game outcome.

* Understand the use of variables to store and respond to changing game states.

* Build an interactive micro:bit game that responds to both movement and chance.

* Design intuitive visual and audio feedback to communicate outcomes effectively to users.

## 💻 Get Set Up
* Plug in your Micro:bit.
* Go to: python.microbit.org/v/3
* Start a new project.
## Step 1
Use the on shake block in the Workspace to run code when you shake the micro:bit.

```
def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```


## Step 2
Make a new global variable called hand and place the set hand to block in the shake event.
```
Python
hand = 0

def on_gesture_shake():
    global hand
    
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```
## Step 3
to pick a random number from 1 to 3 and store it in the variable named hand.
```
hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```
## Step 4
Place an if block under the pick random and check whether hand is equal to 1. Add a show leds block that shows a picture of a piece of paper. The number 1 is the value for paper.
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
Place a play sound block under show leds and edit it to make it sound like paper.

````
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
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
````
Now click on the SHAKE button in the simulator. If you try enough times, you should see a picture of paper on the screen.

## Step 6
Add an else section
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



