# 28BYJ-48 Stepper Motor & HuskyLens Face Detection - GPIO Setup

## Overview
This guide explains how to connect and configure the **28BYJ-48 Stepper Motor** and **HuskyLens** to a **Raspberry Pi Pico** (or other MicroPython-supported boards) for face detection and stepper movement.

## Required Components
- **28BYJ-48 Stepper Motor** with **ULN2003 driver board**
- **HuskyLens AI Camera**
- **Raspberry Pi Pico** or similar microcontroller
- **5V Power Supply** (for stepper motor)
- Jumper Wires

## GPIO Pin Assignments
| Component  | Raspberry Pi Pico GPIO |
|------------|----------------------|
| **Stepper IN1** | GPIO 10 |
| **Stepper IN2** | GPIO 11 |
| **Stepper IN3** | GPIO 12 |
| **Stepper IN4** | GPIO 13 |
| **HuskyLens TX** | GPIO 8 |
| **HuskyLens RX** | GPIO 9 |
| **Servo PWM** | GPIO 15 |

## Wiring Diagram
### **Stepper Motor (28BYJ-48) with ULN2003 Driver**
| ULN2003 IN Pin | Raspberry Pi Pico GPIO |
|--------------|----------------------|
| IN1         | GPIO 10 |
| IN2         | GPIO 11 |
| IN3         | GPIO 12 |
| IN4         | GPIO 13 |
| VCC (5V)    | 5V (External Power) |
| GND         | GND |

### **HuskyLens AI Camera**
| HuskyLens Pin | Raspberry Pi Pico GPIO |
|--------------|----------------------|
| TX          | GPIO 8 |
| RX          | GPIO 9 |
| VCC         | 3.3V or 5V |
| GND         | GND |

### **Continuous Rotation Servo**
| Servo Pin | Raspberry Pi Pico GPIO |
|-----------|----------------------|
| Signal (PWM) | GPIO 15 |
| VCC | 5V |
| GND | GND |

## Software Setup
### **1. Install MicroPython on Pico**
1. Download MicroPython firmware from [Raspberry Pi Official Site](https://micropython.org/download/)
2. Flash it to the Pico using **Thonny IDE**

### **2. Install Required Libraries**
Upload the following Python libraries to your Pico:
- `huskylensPythonLibrary.py` (HuskyLens communication)
- `stepperMotor.py` (Stepper motor control)

### **3. Run the Code**
```python
import time
from machine import Pin, PWM
from huskylensPythonLibrary import HuskyLensLibrary
from stepperMotor import StepperMotor

# HuskyLens Initialization
husky = HuskyLensLibrary("I2C")
husky.face_recognition_mode()

# Stepper Motor
stepper = StepperMotor(10, 11, 12, 13)

# Servo Motor
servo = PWM(Pin(15))
servo.freq(50)

def move_servo(speed):
    duty = int((speed + 1) * (1024 / 2))
    servo.duty_u16(duty)

while True:
    results = husky.command_request_blocks()
    if results:
        print("Face detected - Moving stepper and servo")
        stepper.move_revolution()
        move_servo(1)
    else:
        print("No face detected.")
        stepper.stop()
        move_servo(0)
    time.sleep(0.5)
```

# StepperMotor Class - 28BYJ-48 Stepper Motor Control

## Overview
This class provides an easy-to-use interface for controlling a **28BYJ-48 stepper motor** with a **ULN2003 driver board** using **MicroPython** on a **Raspberry Pi Pico** or similar microcontroller.

## Features
- Simple initialization with GPIO pin assignments
- Move a **specific number of steps**
- Perform **one full revolution** (4096 steps for 28BYJ-48)
- Stop the stepper motor safely
- Configurable **step delay** for speed adjustments

## GPIO Wiring
| ULN2003 IN Pin | Microcontroller GPIO |
|---------------|----------------------|
| IN1           | GPIO 10 |
| IN2           | GPIO 11 |
| IN3           | GPIO 12 |
| IN4           | GPIO 13 |
| VCC (5V)      | 5V External Power |
| GND           | GND |

## Class Usage

### **1. Import the Class**
```python
from stepperMotor import StepperMotor
```

### **2. Initialize the Stepper Motor**
```python
stepper = StepperMotor(in1=10, in2=11, in3=12, in4=13)
```

### **3. Move the Stepper**
- **Move a specific number of steps (positive for forward, negative for reverse)**
```python
stepper.move_steps(1024)  # Moves forward 1024 steps
stepper.move_steps(-512)  # Moves backward 512 steps
```
- **Move one full revolution**
```python
stepper.move_revolution()
```
- **Stop the stepper**
```python
stepper.stop()
```

## Class Reference
```python
class StepperMotor:
    def __init__(self, in1, in2, in3, in4, steps_per_rev=4096, delay=0.001):
        """
        Initialize the stepper motor.
        
        Parameters:
        - in1, in2, in3, in4: GPIO pins connected to the ULN2003 driver
        - steps_per_rev: Total steps per revolution (default: 4096 for 28BYJ-48)
        - delay: Step delay in seconds (affects speed)
        """
```

```python
def move_steps(self, steps):
    """
    Move the stepper motor a given number of steps.
    
    Parameters:
    - steps: Number of steps to move (positive for forward, negative for reverse)
    """
```

```python
def move_revolution(self):
    """
    Move the stepper motor one full revolution (4096 steps).
    """
```

```python
def stop(self):
    """
    Stop the stepper motor by setting all control pins LOW.
    """
```

## Example Program
```python
import time
from stepperMotor import StepperMotor

# Initialize the stepper motor
stepper = StepperMotor(10, 11, 12, 13)

# Move one full revolution
print("Moving one full revolution...")
stepper.move_revolution()

# Move 1024 steps forward
print("Moving 1024 steps forward...")
stepper.move_steps(1024)

# Move 512 steps backward
print("Moving 512 steps backward...")
stepper.move_steps(-512)

# Stop the motor
print("Stopping stepper motor.")
stepper.stop()
```

## Notes
- The **ULN2003 driver board** is required to drive the **28BYJ-48 stepper motor**.
- Adjust the `delay` parameter to **control speed** (lower values = faster movement).
- Ensure you have a **5V power source** for the motor.

## License
This project is open-source under the MIT License.


### Stepper Motor Class
```python
import time
from machine import Pin

class StepperMotor:
    def __init__(self, in1, in2, in3, in4, steps_per_rev=4096, delay=0.001):
        self.pins = [Pin(in1, Pin.OUT), Pin(in2, Pin.OUT), Pin(in3, Pin.OUT), Pin(in4, Pin.OUT)]
        self.steps_per_rev = steps_per_rev
        self.delay = delay
        self.step_sequence = [
            [self.pins[0]],
            [self.pins[0], self.pins[1]],
            [self.pins[1]],
            [self.pins[1], self.pins[2]],
            [self.pins[2]],
            [self.pins[2], self.pins[3]],
            [self.pins[3]],
            [self.pins[3], self.pins[0]],
        ]
        self.current_step = 0

    def set_pins_low(self):
        for pin in self.pins:
            pin.low()

    def set_pins_high(self, active_pins):
        for pin in active_pins:
            pin.high()

    def move_steps(self, steps):
        direction = 1 if steps > 0 else -1
        for _ in range(abs(steps)):
            self.set_pins_low()
            self.set_pins_high(self.step_sequence[self.current_step])
            self.current_step = (self.current_step + direction) % len(self.step_sequence)
            time.sleep(self.delay)

    def move_revolution(self):
        self.move_steps(self.steps_per_rev)

    def stop(self):
        self.set_pins_low()

# Example Usage
if __name__ == "__main__":
    stepper = StepperMotor(10, 11, 12, 13)
    print("Moving one full revolution...")
    stepper.move_revolution()
    print("Stopping stepper motor.")
    stepper.stop()

```

## Notes
- The **ULN2003 driver board** is required to power the **28BYJ-48 stepper motor** properly.
- Ensure the **HuskyLens** is in **Face Recognition Mode**.
- The **Pico** operates at **3.3V logic**; the HuskyLens can handle both **3.3V and 5V logic**.
- If using a different microcontroller, update the **GPIO pin numbers** accordingly.

## License
This project is open-source under the MIT License.
