
# Understanding Conditional Staements/ Selection in Python
```python

number = 0

def on_gesture_shake():
    global number
    basic.clear_screen()
    number = randint(1, 3)
    if number == 3:
        basic.show_icon(IconNames.YES)
    elif number == 2:
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.MEH)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

```
# Task one 
Given that the code below displays something on the screen 
'''python
 basic.showString("Hello!")

'''
Create a dice using this code

Make a list of random tasks and make the computer decide what task to show depending on the number selected

