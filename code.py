"""
Made by Elliott Roach
Made on 2026 Mar
this turns a servo 0 to 90
"""

import board
import digitalio
import time
from adafruit_motor import servo

# setup
data_wire = pwmio.PWMOut(board.gp2, frequency=50)

my_servo = servo.ContinuousServo(data_wire)
my_servo.angle = 0

while True:
    my_servo.angle = 0
    time.sleep(1)
    my_servo.angle = 90
    time.sleep(1)
    
