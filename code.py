"""
Made by Elliott Roach
Made on 2026 Mar
this turns a servo 0 to 90
"""

import board
import digitalio
import time
from servo import Servo
from adafruit_motor import servo

# setup
my_servo = Servo(pin_id=2)

my_servo.write = 0

while True:
    my_servo.write = 0
    time.sleep(1)
    my_servo.write = 90
    time.sleep(1)
