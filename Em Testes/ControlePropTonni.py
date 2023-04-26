#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSendor(Port.S3)

while True:

    valorEsquerdo = (corEsquerdo.reflection())
    valorDireito = (corDireito.reflection())

    vel_direito = 2.74*valorDireito - 8.22
    vel_esquerdo = 2.74*valorEsquerdo - 8.22

    right_motor.run(vel_direito)
    left_motor.run(vel_esquerdo)