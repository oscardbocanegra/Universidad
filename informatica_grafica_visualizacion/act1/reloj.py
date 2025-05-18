import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(radius):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_marks():
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = 0.9 * math.cos(angle)
        y1 = 0.9 * math.sin(angle)
        x2 = math.cos(angle)
        y2 = math.sin(angle)
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

def draw_hand(length, angle_deg, width=2):
    angle = math.radians(angle_deg)
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(length * math.cos(angle), length * math.sin(angle))
    glEnd()

def display():
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
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.2, 1.2, -1.2, 1.2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
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
