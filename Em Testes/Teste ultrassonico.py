#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()
ultrassonico1 = UltrasonicSensor(Port.S1)
# ultrassonico2 = UltrasonicSensor(Port.S4)

while True:
    distancia1 = ultrassonico1.distance()

    if distancia1 < 40:
        ev3.light.on(Color.RED)

    else:
        ev3.light.off
