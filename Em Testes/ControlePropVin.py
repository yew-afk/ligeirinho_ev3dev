#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

b = 100
kp = 1

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSendor(Port.S3)

while True:

    valor_esq = cor_esq.reflection()
    valor_dir = cor_dir.reflection()
    dif = valor_esq - valor_dir

    if dif >= 0:
        vE = b + kp*dif
        vD = b - kp*dif
        left_motor.run(vE)
        right_motor.run(vD)
    else:
        vE = b - kp*dif
        vD = b + kp*dif
        left_motor.run(vE)
        right_motor.run(vD)
    

