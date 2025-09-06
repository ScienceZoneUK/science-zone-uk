# Salute!
Salute! is a simple math game where players select a number card from a deck (without looking at it) and hold it to their forehead as in a “salute”. Another player decides whether to make a sum or product of the two cards and then announces the result. Based on the card held by the opposing player and the result announced, each player tries to figure out what card they are holding.
#Goals for this activity
* This a group activity for either a classroom or just friends gathered together.
* Decompose the steps needed to code and play the Salute! math game using micro:bits.
* Create a program to display a random number, in an appropriate range, on the LED Matrix of a micro:bit and correctly install the program on a micro:bit.
* Optionally, create a program to keep score in the game using a micro:bit and correctly install the program on a micro:bit. Optionally, make a headband to hold the micro:bit and battery on the forehead during game play.
* Play the micro:bit Salute! math game, using micro:bits, in groups of 3.

##Materials
* 2 or 3 micro:bits with battery packs and USB cables
* Paper and pencil
* Optional, materials to create headbands to hold the micro:bit
##Coding the game
##Two players
1. Two of the micro:bits are programmed to display a random number within a specified range based on a “salute”. A salute is an agreed upon event/input that the student can make happen without needing to seeing their LED Matrix.
2. Include a loop to verify that the number is larger than 0 and/or 1 if those numbers are not to be included in the game.
3. If upper number in the range is greater than 9, include a loop to display the number multiple times or provide another way to redisplay the number.
#Three players
If using 3 micro:bits, the third micro:bit is programmed to keep score in the game using the A and B buttons and to display the score based on a different event, such as, the A+B button. There should also be a way to reset the scores for the next round of play.
Make the number cards
Choose a random number between 0 and 9.

##Step 1
```
randomNbr = 0

def on_gesture_screen_up():
    global randomNbr
    randomNbr = randint(0, 10)
    basic.show_number(randomNbr)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

```

##Step 2

```
randomNbr = 0

def on_gesture_screen_up():
    global randomNbr
    randomNbr = 0
    while randomNbr < 1:
        randomNbr = randint(0, 10)
    basic.show_number(randomNbr)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

```
##Step 3
```
player1Score = 0
player2Score = 0

def on_button_pressed_a():
    global player1Score
    player1Score += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global player2Score
    player2Score += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    if player1Score == player2Score:
        basic.show_string("TIE")
    elif player1Score > player2Score:
        basic.show_string("Player 1")
    else:
        basic.show_string("Player 2")
    basic.show_number(max(player1Score, player2Score))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_logo_down():
    global player2Score, player1Score
    player2Score = 0
    player1Score = 0
    basic.show_string("Reset")
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

```
