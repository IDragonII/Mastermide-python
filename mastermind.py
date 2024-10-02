from z3 import *

rojo = Bool("rojo")
azul = Bool("azul")
verde = Bool("verde")
amarillo = Bool("amarillo")

colores = ["rojo", "amarillo", "azul", "verde"]

posicion_1 = [rojo, azul, verde, amarillo]
posicion_2 = [rojo, azul, verde, amarillo]
posicion_3 = [rojo, azul, verde, amarillo]
posicion_4 = [rojo, azul, verde, amarillo]

combinacion_secreta = ['rojo', 'azul', 'verde', 'amarillo']

conocimiento = And(
    Or(posicion_1),
    Or(posicion_2),
    Or(posicion_3),
    Or(posicion_4),
    Not(And(posicion_1[0], posicion_2[0])),
    Not(And(posicion_1[1], posicion_2[1])),
    Not(And(posicion_1[2], posicion_3[2])),
    Not(And(posicion_1[3], posicion_4[3])),
)

def cantidad_correctos(secreta, intento):
    return sum([1 for s, g in zip(secreta, intento) if s == g])

def verificar_suponer(secreta, intento):
    return secreta == intento

def juego_mastermind():
    intentos = 0
    print("¡Bienvenido a Mastermind!")
    print("Colores disponibles: rojo, azul, verde, amarillo")

    while True:
        suposicion_usuario = input("Ingresa tu combinación de 4 colores separados por comas (por ejemplo: rojo,azul,verde,amarillo): ").split(',')
        suposicion_usuario = [g.strip().lower() for g in suposicion_usuario]

        if len(set(suposicion_usuario)) < 4:
            print("No puedes repetir colores. Intenta de nuevo.")
            continue

        if verificar_suponer(combinacion_secreta, suposicion_usuario):
            print(f"¡Felicidades! Adivinaste la combinación secreta en {intentos+1} intentos.")
            break
        else:
            correctos_pos = cantidad_correctos(combinacion_secreta, suposicion_usuario)
            print(f"Colores correctos en posición correcta: {correctos_pos}")
            print("Intenta de nuevo.\n")
            intentos += 1

juego_mastermind()
