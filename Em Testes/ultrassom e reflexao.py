#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

corEsquerdo = ColorSensor(Port.S3)
corDireito = ColorSensor(Port.S2)

ultraFrente = UltrasonicSensor(Port.S1)
ultraLado = UltrasonicSensor(Port.S4)
 
podecontinuar = True

while True:

    distancia1 = int(ultraFrente.distance())
    distancia2 = int(ultraLado.distance())

    if distancia1 > 50 and podecontinuar == True:

        right_motor.run(velocidadeDireito)
        left_motor.run(velocidadeEsquerdo)

        valorEsquerdo = (corEsquerdo.reflection())
        valorDireito = (corDireito.reflection())

        velocidadeEsquerdo = valorEsquerdo * 2
        velocidadeDireito = valorDireito * 2

    elif distancia1 <= 50 and podecontinuar == True:
        
        podecontinuar = False
        right_motor.stop()
        left_motor.stop()

    elif podecontinuar == False:
        right_motor.reset_angle(0)
        left_motor.reset_angle(0)

        while distancia2 > 50:
            right_motor.run(100)
            left_motor.run(-100)

            angulodireito = right_motor.angle()
            anguloesquerdo = left_motor.angle()

        right_motor.reset_angle(0)
        left_motor.reset_angle(0)

        while distancia2 < 100:
            right_motor.run(100)
            left_motor.run(100)

            percursodireito = right_motor.angle()
            percursoesquerdo = left_motor.angle()
        

    wait(10)