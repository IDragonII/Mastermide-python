import pygame
import sys
from z3 import *

pygame.init()

ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mastermind")

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fuente = pygame.font.SysFont(None, 36)

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (200, 200, 200)

rojo = Bool("rojo")
azul = Bool("azul")
verde = Bool("verde")
amarillo = Bool("amarillo")

combinacion_secreta = ['rojo', 'azul', 'verde', 'amarillo']

casillas = [None] * 4
resultado_texto = "Arrastra los colores para ingresar tu combinación."

def cantidad_correctos(secreta, intento):
    return sum([1 for s, g in zip(secreta, intento) if s == g])

def verificar_suponer(secreta, intento):
    return secreta == intento

def mostrar_texto(texto, x, y, max_width):
    words = texto.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if fuente.size(current_line + word)[0] > max_width:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line += word + " "
    lines.append(current_line)
    for i, line in enumerate(lines):
        texto_render = fuente.render(line, True, NEGRO)
        ventana.blit(texto_render, (x, y + i * fuente.get_height()))

class ColorCirculo:
    def __init__(self, color, x, y, nombre):
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)
        self.nombre = nombre

    def draw(self):
        pygame.draw.circle(ventana, self.color, (self.rect.centerx, self.rect.centery), 25)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

def dibujar_tablero():
    for i in range(4):
        pygame.draw.rect(ventana, GRIS_CLARO, (50 + i * 125, 75, 100, 100), 2)

def dibujar_boton_verificar():
    pygame.draw.rect(ventana, GRIS_CLARO, (400, 250, 150, 50))
    mostrar_texto("Verificar", 420, 260, 150)

def juego_mastermind():
    global resultado_texto
    circulos = [
        ColorCirculo(ROJO, 70, 195, "rojo"),
        ColorCirculo(AZUL, 200, 195, "azul"),
        ColorCirculo(VERDE, 325, 195, "verde"),
        ColorCirculo(AMARILLO, 450, 195, "amarillo"),
    ]
    color_seleccionado = None
    verificado = False

    while True:
        ventana.blit(fondo, (0, 0))
        dibujar_tablero()
        dibujar_boton_verificar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for circulo in circulos:
                    if circulo.is_over(event.pos):
                        color_seleccionado = circulo
                        break

                if 400 <= event.pos[0] <= 550 and 250 <= event.pos[1] <= 300:
                    if None not in casillas:
                        if verificar_suponer(combinacion_secreta, casillas):
                            resultado_texto = "¡Felicidades! Has adivinado la combinación secreta."
                        else:
                            correctos_pos = cantidad_correctos(combinacion_secreta, casillas)
                            resultado_texto = f"{correctos_pos} colores correctos"
                        verificado = True

            if event.type == pygame.MOUSEBUTTONUP:
                if color_seleccionado:
                    for i in range(4):
                        if 50 + i * 125 <= event.pos[0] <= 150 + i * 125 and 75 <= event.pos[1] <= 175:
                            casillas[i] = color_seleccionado.nombre
                            break
                    color_seleccionado = None

            if event.type == pygame.MOUSEMOTION:
                if color_seleccionado:
                    color_seleccionado.rect.center = event.pos

        for circulo in circulos:
            circulo.draw()

        if verificado:
            mostrar_texto(resultado_texto, 50, 260, ANCHO - 300)

        pygame.display.flip()

juego_mastermind()
