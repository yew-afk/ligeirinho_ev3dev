#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

erro = 0
Vb = 200

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.C)

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

while True:
    print('Está funcionando')