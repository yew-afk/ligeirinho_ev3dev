#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from time import sleep

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

corEsquerdo = ColorSensor(Port.S3)
corDireito = ColorSensor(Port.S2)

velocidadeEsquerdo = 200
velocidadeDireito = 200

while True:

    right_motor.run(velocidadeDireito)
    left_motor.run(velocidadeEsquerdo)

    valorEsquerdo = str(corEsquerdo.color())
    valorDireito = str(corDireito.color())

    if valorEsquerdo == "Color.BLACK":
        velocidadeEsquerdo = -100

    else:
        velocidadeEsquerdo = 200
    
    if valorDireito == "Color.BLACK":
        velocidadeDireito = -100
    
    else: 
        velocidadeDireito = 200

    sleep(0.00001)


# testeteste