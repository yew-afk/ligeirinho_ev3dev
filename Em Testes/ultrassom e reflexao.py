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

def reflexao():
    right_motor.run(velocidadeDireito)
    left_motor.run(velocidadeEsquerdo)

    valorEsquerdo = (corEsquerdo.reflection())
    valorDireito = (corDireito.reflection())

    velocidadeEsquerdo = valorEsquerdo * 2
    velocidadeDireito = valorDireito * 2

while True:

    distancia1 = int(ultraFrente.distance())
    #distancia2 = int(ultraLado.distance())
   
    while distancia1 > 50:
        reflexao()
        distancia1 = int(ultraFrente.distance())

    if distancia1 <= 50:
        right_motor.stop()
        left_motor.stop()

        wait(10)

        distancia2 = int(ultraLado.distance())
        right_motor.reset_angle(0)

        while distancia2 < 60:
            right_motor.run(100)
            left_motor.run(-100)
        
        angulo_volta = int(right_motor.angle())
        detectando_passagem = False
        
        while detectando_passagem == False:
            right_motor.run(100)
            left_motor.run(100)
            distancia2 = int(ultraLado.distance())
            
            if distancia2 > 100:
                detectando_passagem = True
        
        right_motor.run_angle(100, -(angulo_volta))
        left_motor.run_angle(100, angulo_volta, wait=True)