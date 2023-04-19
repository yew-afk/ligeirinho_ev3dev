#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor
from time import sleep

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

cor = ColorSensor(Port.S3)

while True:

    valor = str(cor.color())

    if valor == "Color.BLACK":
        right_motor.run(-50)
        left_motor.run(200)
    else:
        right_motor.run(200)
        left_motor.run(-50)

    
    sleep(0.00001)


