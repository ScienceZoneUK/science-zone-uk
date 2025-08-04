# IOT project - Sensing water levels



#### Get micro:bit port
unplug microbit and run:
```ls /dev/tty*```

plug microbit and rerun

Read serial from micro:bit
```python
import serial
from time import sleep

# Update this if your port is different
PORT = "/dev/ttyACM0" #!!!!CHANGE THIS!!!!
BAUD = 115200

try:
    s = serial.Serial(PORT, BAUD, timeout=1)
    s.reset_input_buffer()
    print(f"Connected to {PORT} at {BAUD} baud.")
except serial.SerialException:
    print("Could not open serial port. Is the Micro:bit connected?")
    exit()

try:
    while True:
        try:
            line = s.readline().decode('utf-8').strip()
            if line:
                value = int(line)
                print(f"Water Level: {value}")
        except ValueError:
            print("Received non-integer data.")
        except UnicodeDecodeError:
            print("Received undecodable data.")

        sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    s.close()

```
Microbit code
```python
from microbit import *

while True:
    water_level = pin0.read_analog()
    print(water_level)
    sleep(200)

```
