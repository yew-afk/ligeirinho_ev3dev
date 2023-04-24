#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port


ev3 = EV3Brick()

motor_esq = Motor(Port.B)
motor_dir = Motor(Port.C)

cor_esq = ColorSensor(Port.S3)
cor_dir = ColorSensor(Port.S2)

while True:

    valor_esq = int(cor_esq(reflection()))
    valor_dir = int(cor_dir(reflectiob()))

    if valor_esq >= 50 and valor_dir >= 50:
        motor_esq.run(2.5*valor_esq)
        motor_dir.run(2.5*valor_dir)
    
    elif valor_esq < 50 and valor_esq > valor_dir:
        motor_esq.run(0.2*valor_esq)
        motor_dir.run(2.5*valor_dir)
    
    elif valor_dir < 50 and valor_dir > valor_esq:
        motor_esq.run(2.5*valor_esq)
        motor_dir.run(0.2*valor_dir)
    
    else:
        motor_esq.run(2.5*valor_esq)
        motor_dir.run(2.5*valor_dir)