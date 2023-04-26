#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

A = 4.11
B = -12.33

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)

while True:

    valorEsquerdo = (cor_esq.reflection())
    valorDireito = (cor_dir.reflection())

    vel_direito = A*valorDireito + B
    vel_esquerdo = A*valorEsquerdo + B

    right_motor.run(vel_direito)
    left_motor.run(vel_esquerdo)