#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

erro = 0
Vb = 150
Kp = 2
comp = 50

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.C)

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

while True:
    valor_esq = int(corE.reflection())
    valor_dir = int(corD.reflection())

    erro =  valor_esq - valor_dir
    mE = Vb + Kp*erro
    mD = Vb - Kp*erro

    motorE.run(mE+comp)
    motorD.run(mD)