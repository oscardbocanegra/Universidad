# reloj.py
# Programa para dibujar un reloj analógico estático usando OpenGL y GLUT en Python
#
# Este programa crea una ventana donde se dibuja un reloj analógico con las marcas de las horas y manecillas estáticas.

import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as GLUT

# Definir la fuente para los números
FONT = GLUT.GLUT_BITMAP_HELVETICA_18

def draw_circle(radius):
    """
    Dibuja un círculo usando líneas para representar el borde del reloj.
    :param radius: Radio del círculo
    """
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_marks():
    """
    Dibuja las 12 marcas de las horas alrededor del reloj y los números de las horas.
    El 12 debe estar arriba, 3 a la derecha, 6 abajo, 9 a la izquierda.
    """
    for i in range(12):
        # Mueve el 12 dos posiciones a la izquierda
        angle = math.radians((i + 1) * -30 + 90)
        x1 = 0.9 * math.cos(angle)
        y1 = 0.9 * math.sin(angle)
        x2 = math.cos(angle)
        y2 = math.sin(angle)
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        # Dibujar el número de la hora, centrado
        glColor3f(0, 0, 0)
        num_radius = 0.78
        num_x = num_radius * math.cos(angle)
        num_y = num_radius * math.sin(angle)
        offset_x = -0.03 * len(str(i+1))
        offset_y = -0.04
        glRasterPos2f(num_x + offset_x, num_y + offset_y)
        hour = str(i+1)
        for ch in hour:
            glutBitmapCharacter(FONT, ord(ch))

def draw_hand(length, angle_deg, width=2):
    """
    Dibuja una manecilla del reloj.
    :param length: Longitud de la manecilla (relativa al radio)
    :param angle_deg: Ángulo en grados desde las 12 en sentido horario
    :param width: Grosor de la línea
    """
    angle = math.radians(angle_deg)
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(length * math.cos(angle), length * math.sin(angle))
    glEnd()

def display():
    """
    Función de dibujo principal. Limpia la pantalla y dibuja el reloj con sus manecillas.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    draw_circle(1.0)
    draw_marks()
    # Manecillas (estáticas, ejemplo: 10:10:30)
    glColor3f(0.2, 0.2, 0.8)  # Hora
    draw_hand(0.5, 120, 6)
    glColor3f(0.2, 0.8, 0.2)  # Minuto
    draw_hand(0.8, 60, 4)
    glColor3f(0.8, 0.2, 0.2)  # Segundo
    draw_hand(0.9, 180, 2)
    glutSwapBuffers()

def reshape(w, h):
    """
    Ajusta la vista cuando la ventana cambia de tamaño.
    """
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.2, 1.2, -1.2, 1.2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    """
    Función principal: inicializa GLUT y ejecuta el bucle principal.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'Reloj Analogico OpenGL')
    glClearColor(1, 1, 1, 1)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__':
    main()
