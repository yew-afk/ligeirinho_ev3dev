#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from time import sleep

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

while True:

    left_motor.run(1000)
    right_motor.run(1000)