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

    valorEsquerdo = (corEsquerdo.reflection())
    valorDireito = (corDireito.reflection())

    velocidadeEsquerdo = valorEsquerdo * 2
    velocidadeDireito = valorDireito * 2

    sleep(0.00001)


