#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

erro = 0
Vb = 150
Kp = 5
comp = 40       

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.C)

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

while True:
    valor_esq = int(corE.reflection())
    valor_dir = int(corD.reflection())

    erro =  (valor_esq - valor_dir) + 10

    mE = Vb + Kp*erro
    mD = Vb - Kp*erro

    motorD.run(mD+comp)
    motorE.run(mE)

    # print(valor_esq, valor_dir)
    #print(erro)
    #print(mE)
    #print(mD)
    #print()
    #wait(5000)

    
    