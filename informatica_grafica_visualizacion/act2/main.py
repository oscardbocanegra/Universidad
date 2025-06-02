"""
main.py

Este script crea una ventana OpenGL con cuatro vistas simultáneas de un cubo, cada una utilizando un tipo diferente de proyección:

1. Proyección ortogonal
2. Proyección gabinete
3. Proyección perspectiva simétrica
4. Proyección perspectiva oblicua

El cubo se dibuja con colores distintos en cada cara y se rota para resaltar la tridimensionalidad y las diferencias entre las proyecciones. No se utiliza gluLookAt ni se mueve la posición del ojo, cumpliendo con la restricción del enunciado.

Requisitos:
- Python
- PyOpenGL
- numpy

Autor: [Tu Nombre]
Fecha: 2025-06-01
"""
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

# Tamaño de la ventana
width, height = 800, 800

# Dibuja un cubo centrado en el origen con colores en cada cara
def draw_cube_colored():
    """Dibuja un cubo con colores diferentes en cada cara."""
    glBegin(GL_QUADS)
    # Cara frontal (roja)
    glColor3f(1, 0, 0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    # Cara trasera (verde)
    glColor3f(0, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    # Cara izquierda (azul)
    glColor3f(0, 0, 1)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    # Cara derecha (cian)
    glColor3f(0, 1, 1)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5,  0.5, -0.5)
    glVertex3f(0.5,  0.5,  0.5)
    glVertex3f(0.5, -0.5,  0.5)
    # Cara superior (magenta)
    glColor3f(1, 0, 1)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5, -0.5)
    # Cara inferior (amarillo)
    glColor3f(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glEnd()

# Proyección ortogonal
def set_ortho():
    """Configura una proyección ortogonal."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

# Proyección gabinete
def set_cabinet():
    """Configura una proyección gabinete (oblicua con ángulo de 45° y escala 0.5)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    angle = np.deg2rad(45)
    d = 0.5  # Escala típica para gabinete
    m = np.array([
        [1, 0, d*np.cos(angle), 0],
        [0, 1, d*np.sin(angle), 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    glMultMatrixf(m.T)
    glOrtho(-2, 2, -2, 2, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

# Proyección perspectiva simétrica
def set_perspective():
    """Configura una proyección perspectiva simétrica usando gluPerspective."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

# Proyección perspectiva oblicua
def set_oblique():
    """Configura una proyección perspectiva oblicua (oblicua con ángulo de 30° y escala 1.0)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    angle = np.deg2rad(30)
    d = 1.0
    m = np.array([
        [1, 0, d*np.cos(angle), 0],
        [0, 1, d*np.sin(angle), 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    glMultMatrixf(m.T)
    glOrtho(-2, 2, -2, 2, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

def display():
    """Función principal de dibujo: divide la ventana en cuatro viewports y dibuja el cubo en cada proyección."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    # Viewport 1: ortogonal
    glViewport(0, height//2, width//2, height//2)
    set_ortho()
    glPushMatrix()
    glRotatef(30, 1, 1, 0)
    draw_cube_colored()
    glPopMatrix()

    # Viewport 2: gabinete
    glViewport(width//2, height//2, width//2, height//2)
    set_cabinet()
    glPushMatrix()
    glRotatef(30, 1, 1, 0)
    draw_cube_colored()
    glPopMatrix()

    # Viewport 3: perspectiva simétrica
    glViewport(0, 0, width//2, height//2)
    set_perspective()
    glPushMatrix()
    glRotatef(30, 1, 1, 0)
    draw_cube_colored()
    glPopMatrix()

    # Viewport 4: perspectiva oblicua
    glViewport(width//2, 0, width//2, height//2)
    set_oblique()
    glPushMatrix()
    glRotatef(30, 1, 1, 0)
    draw_cube_colored()
    glPopMatrix()

    glutSwapBuffers()

def main():
    """Inicializa GLUT y ejecuta el bucle principal de la ventana."""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Cuatro vistas de un cubo")
    glutDisplayFunc(display)
    glClearColor(0.9, 0.9, 0.9, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()
