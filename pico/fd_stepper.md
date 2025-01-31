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

## Notes
- The **ULN2003 driver board** is required to power the **28BYJ-48 stepper motor** properly.
- Ensure the **HuskyLens** is in **Face Recognition Mode**.
- The **Pico** operates at **3.3V logic**; the HuskyLens can handle both **3.3V and 5V logic**.
- If using a different microcontroller, update the **GPIO pin numbers** accordingly.

## License
This project is open-source under the MIT License.
