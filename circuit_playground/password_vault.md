# 🛠️ Secret Tap Password Vault — CircuitPython Lesson

**Audience**: 9-year-olds  
**Time**: 60 minutes  
**Device**: Adafruit Circuit Playground Express  
**Language**: CircuitPython  
**Libraries**: `adafruit_circuitplayground`, `adafruit_hid`, plus a `PasswordTyper.py` file

---

## 🧠 Learning Goals

By the end of the lesson, students will:
1. Use capacitive touch inputs.
2. Give feedback with lights and sounds.
3. Use a tap pattern to unlock a secret.
4. Automatically type a password into the computer.

---

## 🧩 Supplies Needed

- Circuit Playground Express
- USB cable
- Mu Editor or other CircuitPython editor
- Pre-loaded `PasswordTyper.py` file
- Library folder with:
  - `adafruit_hid/`
  - `adafruit_circuitplayground.mpy`

---

## ⏱️ Class Breakdown

### 🟢 Part 1: Hello, Touch! (10 min)

**Concept**: Touch sensors detect your finger!

```python
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched A1!")
```

Try other pads like `A2`, `A3`, `A4`.

---

### 🔵 Part 2: Add Lights and Sounds (10 min)

**Concept**: Feedback helps us see and hear when something happens.

```python
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        cp.pixels.fill((255, 0, 0))  # Red
        cp.play_tone(440, 0.2)
    else:
        cp.pixels.fill((0, 0, 0))
```

Try using different pads with different colors/sounds.

---

### 🟣 Part 3: Collect the Tap Pattern (10 min)

**Concept**: Store a secret sequence of taps in a list!

```python
from adafruit_circuitplayground import cp
import time

combo = ['1', '2', '3', '4']
entered = []

def get_touch():
    if cp.touch_A1:
        return '1'
    if cp.touch_A2:
        return '2'
    if cp.touch_A3:
        return '3'
    if cp.touch_A4:
        return '4'
    return None

while True:
    touch = get_touch()
    if touch:
        entered.append(touch)
        print("Tapped:", entered)
        cp.pixels.fill((0, 0, 255))
        cp.play_tone(660, 0.1)
        time.sleep(0.3)
        cp.pixels.fill((0, 0, 0))
        while get_touch():
            pass

    if len(entered) == 4:
        if entered == combo:
            print("Correct!")
        else:
            print("Try again.")
        entered = []
```

---

### 🟡 Part 4: Auto-Type the Password! (15 min)

**Concept**: The board can act like a USB keyboard.

Create a file called `PasswordTyper.py` with this code:

```python
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class PasswordTyper:
    def __init__(self, password):
        self.password = password
        self.keyboard = Keyboard(usb_hid.devices)

    def type(self):
        for char in self.password:
            self._type_char(char)
            time.sleep(0.1)
        self.keyboard.press(Keycode.ENTER)
        self.keyboard.release_all()

    def _type_char(self, char):
        char_map = {
            '0': Keycode.ZERO,
            '1': Keycode.ONE,
            '2': Keycode.TWO,
            '3': Keycode.THREE,
            '4': Keycode.FOUR,
            '5': Keycode.FIVE,
            '6': Keycode.SIX,
            '7': Keycode.SEVEN,
            '8': Keycode.EIGHT,
            '9': Keycode.NINE,
            '!': (Keycode.ONE, True),
        }

        if char.isalpha():
            if char.isupper():
                self.keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper()))
            else:
                self.keyboard.press(getattr(Keycode, char.upper()))
        elif char in char_map:
            value = char_map[char]
            if isinstance(value, tuple):
                self.keyboard.press(Keycode.SHIFT, value[0])
            else:
                self.keyboard.press(value)
        self.keyboard.release_all()
```

Test with this:

```python
from PasswordTyper import PasswordTyper

typer = PasswordTyper("SecreT123!")
typer.type()
```

---

### 🔴 Part 5: Final Project (15 min)

Combine it all!

```python
import time
import usb_hid
from adafruit_circuitplayground import cp
from PasswordTyper import PasswordTyper

combo = ['1', '2', '3', '4']
entered = []
typer = PasswordTyper("SecreT123!")

def get_touch():
    if cp.touch_A1:
        return '1'
    if cp.touch_A2:
        return '2'
    if cp.touch_A3:
        return '3'
    if cp.touch_A4:
        return '4'
    return None

def check_combo():
    if entered == combo:
        cp.pixels.fill((0, 255, 0))  # Green
        cp.play_tone(880, 0.2)
        typer.type()
    else:
        cp.pixels.fill((255, 0, 0))  # Red
        cp.play_tone(220, 0.3)
    time.sleep(1)
    cp.pixels.fill((0, 0, 0))

while True:
    touch = get_touch()
    if touch:
        entered.append(touch)
        cp.pixels.fill((0, 0, 255))  # Blue
        cp.play_tone(660, 0.1)
        time.sleep(0.3)
        cp.pixels.fill((0, 0, 0))
        while get_touch():
            pass

    if len(entered) == 4:
        check_combo()
        entered = []
```

---

## ✅ Wrap-up & Extensions

- Celebrate success!
- Change the password or color/sound
- Add a way to reset the combo
