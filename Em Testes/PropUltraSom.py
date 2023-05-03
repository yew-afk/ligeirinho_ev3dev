#!/usr/bin/env pybricks-micropython

#Vinicius

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

kp = 4
vb = 157

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S2)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)


while True:

    distF = ultraF.distance()
    distD = ultraD.distance()

    valorE = cor_esq.reflection()
    valorD = cor_dir.reflection()

    dif = valorE - valorD

    if distF <= 150:

        vel_direito = kp*valorD + 500
        vel_esquerdo = kp*valorE + 500

        right_motor.run(vel_direito)
        left_motor.run(vel_esquerdo)
    else:
        vel_direito = kp*valorD + vb
        vel_esquerdo = kp*valorE + vb

        right_motor.run(vel_direito)
        left_motor.run(vel_esquerdo)