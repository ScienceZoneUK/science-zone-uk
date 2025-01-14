import gc
import time
from motor import Motor, motor2040
from pimoroni import REVERSED_DIR

class Rover:
    def __init__(self, speed_scale=10.0):
        self.speed_scale = speed_scale
        
        # Initialize motors
        self.motor_a = Motor(motor2040.MOTOR_A, speed_scale=self.speed_scale)  # Front right
        self.motor_b = Motor(motor2040.MOTOR_B, speed_scale=self.speed_scale)  # Rear right
        self.motor_c = Motor(motor2040.MOTOR_C, speed_scale=self.speed_scale)  # Rear left
        self.motor_d = Motor(motor2040.MOTOR_D, speed_scale=self.speed_scale)  # Front left

        # Reverse directions for left motors
        self.motor_c.direction(REVERSED_DIR)
        self.motor_d.direction(REVERSED_DIR)

        # Enable all motors
        self.enable_motors()

    def enable_motors(self):
        self.motor_a.enable()
        self.motor_b.enable()
        self.motor_c.enable()
        self.motor_d.enable()

    def disable_motors(self):
        self.motor_a.disable()
        self.motor_b.disable()
        self.motor_c.disable()
        self.motor_d.disable()

    def stop_all(self):
        self.motor_a.stop()
        self.motor_b.stop()
        self.motor_c.stop()
        self.motor_d.stop()

    def move(self, speeds, duration):
        self.motor_a.speed(speeds[0])
        self.motor_b.speed(speeds[1])
        self.motor_c.speed(speeds[2])
        self.motor_d.speed(speeds[3])
        time.sleep(duration)
        self.stop_all()

    def move_forward(self, speed, duration):
        self.move([speed, speed, speed, speed], duration)

    def move_backward(self, speed, duration):
        self.move([-speed, -speed, -speed, -speed], duration)

    def strafe_left(self, speed, duration):
        self.move([-speed, speed, -speed, speed], duration)

    def strafe_right(self, speed, duration):
        self.move([speed, -speed, speed, -speed], duration)

    def spin_clockwise(self, speed, duration):
        self.move([speed, speed, -speed, -speed], duration)

    def spin_counterclockwise(self, speed, duration):
        self.move([-speed, -speed, speed, speed], duration)

    def diagonal_left_forward(self, speed, duration):
        self.move([speed, 0, 0, speed], duration)

    def diagonal_right_forward(self, speed, duration):
        self.move([0, speed, speed, 0], duration)

    def dance_sequence(self, speed=3.0, duration=3):
        print("Starting dance sequence with sideways moves!")

        # Forward and backward motion
        self.move_forward(speed, duration)
        self.move_backward(speed, duration)

        # Strafing left and right
        self.strafe_left(speed, duration)
        self.strafe_right(speed, duration)

        # Spins
        self.spin_clockwise(speed, duration)
        self.spin_counterclockwise(speed, duration)

        # Diagonal motions
        self.diagonal_left_forward(speed, duration)
        self.diagonal_right_forward(speed, duration)

        # Sideways moves again for emphasis
        self.strafe_left(speed, duration)
        self.strafe_right(speed, duration)

        print("Dance sequence complete!")

# Usage Example
if __name__ == "__main__":
    # Free up hardware resources
    gc.collect()

    rover = MecanumRover(speed_scale=10.0)
    rover.dance_sequence(speed=3.0, duration=3)

    rover.stop_all()
    rover.disable_motors()

    print("Motors disabled. Rover at rest.")

