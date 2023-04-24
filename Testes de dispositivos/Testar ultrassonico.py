#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()
ultrassom = UltrasonicSensor(Port.S1)

while True:
    valor = int(ultrassom.distance())
    print(f'{valor} mm')
    wait(10)

