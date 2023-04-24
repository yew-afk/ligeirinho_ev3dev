#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from time import sleep

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

corEsquerdo = ColorSensor(Port.S3)
corDireito = ColorSensor(Port.S2)

distanciaEsquerdo = UltrasonicSensor(Port.S1)
distanciaDireito = UltrasonicSensor(Port.S4)

velocidadeEsquerdo = 200
velocidadeDireito = 200

while True:

    distancia1 = int(ultrassonico1.distance())
    distancia2 = int(ultrassonico2.distance())

    right_motor.run(velocidadeDireito)
    left_motor.run(velocidadeEsquerdo)

    valorEsquerdo = (corEsquerdo.reflection())
    valorDireito = (corDireito.reflection())

    velocidadeEsquerdo = valorEsquerdo * 2
    velocidadeDireito = valorDireito * 2

    sleep(0.00001)

while True:

    if distancia1 < 80:
        ev3.light.on(Color.RED)

    else:
        ev3.light.on(Color.GREEN)

    wait(1000)
    print(distancia1)

