#!/usr/bin/env pybricks-micropython

#Vinicius

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

valor1 = 250 #velocidade maxima
valor2 = 50 #velocidade minimia

a = (valor1 - valor2)/73 #coeficientes da função afim da velocidade
b = valor1 - (76 * a)

ev3 = EV3Brick()

kp = 4
vb = 157

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)

#PC = True

while True:

    distF = int(ultraF.distance())
    distD = int(ultraD.distance())

    valorE = cor_esq.reflection()
    valorD = cor_dir.reflection()

    while distF > 20:

        vel_direito = a*valorDireito + b
        vel_esquerdo = a*valorEsquerdo + b

        right_motor.run(vel_direito)
        left_motor.run(vel_esquerdo)
    
    while distF < 20:
        
        vel_esquerdo = (a*valorEsquerdo + b) + ((a*valorEsquerdo + b)/10)*distF - 1.5*distF
        vel_esquerdo = (a*valorEsquerdo + b) + ((a*valorEsquerdo + b)/10)*distF - 1.5*distF

        right_motor.run(vel_direito)
        left_motor.run(vel_esquerdo)

    wait(10)

    '''elif distF < 80:

        left_motor.run(-100)
        right_motor.run(100)
        wait(100)

    if distD < 100:

           left_motor.run(150)
            right_motor.run(150)
        
        else:

            left_motor.run(100)
            right_motor.run(-100)
            wait(100)'''
