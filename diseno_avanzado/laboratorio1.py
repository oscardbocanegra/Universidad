"""
Módulo para calcular la distancia mínima entre pares de puntos 2D
=================================================================

Este módulo proporciona funciones para:
1. Leer puntos 2D desde un archivo de texto con un formato específico.
2. Calcular la distancia euclidiana entre dos puntos.
3. Encontrar el par de puntos más cercano y calcular su distancia mínima.

Formato del Archivo de Entrada
------------------------------
El archivo de entrada debe seguir el siguiente formato:
1. La primera línea contiene una lista de valores de las coordenadas x, separados por comas.
2. La segunda línea contiene una lista de valores de las coordenadas y, también separados por comas.

Funciones
---------
leer_puntos(archivo: str) -> list[tuple[int, int]]
    Lee un archivo de texto con el formato especificado y devuelve una lista de 
    puntos representados como tuplas (x, y).

calcular_distancia(p1: tuple[int, int], p2: tuple[int, int]) -> float
    Calcula la distancia euclidiana entre dos puntos 2D.

calcular_pares_mas_cercanos(puntos: list[tuple[int, int]]) -> 
tuple[tuple[int, int], tuple[int, int], float]
    Encuentra el par de puntos más cercanos y calcula su distancia mínima.

Ejemplo de Uso
--------------
# Uso con el archivo "datos_10000.txt"
puntos = leer_puntos("datos_10000.txt")
par_mas_cercano, distancia_minima = calcular_pares_mas_cercanos(puntos)
print(f"Par más cercano: {par_mas_cercano}")
print(f"Distancia mínima: {distancia_minima}")
"""

import math

def leer_puntos(archivo):
    """
    Lee un archivo de texto y extrae los puntos representados por las abscisas y ordenadas.

    Parameters
    ----------
    archivo : str
        La ruta del archivo que contiene los datos.

    Returns
    -------
    list of tuple
        Lista de puntos representados como tuplas (x, y).
    """
    with open(archivo, 'r', encoding='utf-8') as file:
        # Leer las dos líneas del archivo
        abscisas = file.readline().strip().split(',')
        ordenadas = file.readline().strip().split(',')
        # Convertir a enteros y emparejar
        punto = [(int(x), int(y)) for x, y in zip(abscisas, ordenadas)]
    return punto

def calcular_distancia(p1, p2):
    """
    Calcula la distancia euclidiana entre dos puntos 2D.

    Parameters
    ----------
    p1, p2 : tuple
        Tuplas que representan dos puntos (x, y).

    Returns
    -------
    float
        La distancia euclidiana entre p1 y p2.
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calcular_pares_mas_cercanos(punto):
    """
    Encuentra el par de puntos más cercanos y calcula su distancia.

    Parameters
    ----------
    puntos : list of tuple
        Lista de puntos representados como tuplas (x, y).

    Returns
    -------
    tuple
        Un par de puntos más cercanos y su distancia.
    """
    min_distancia = float('inf')
    par_cercano = None
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            distancia = calcular_distancia(puntos[i], puntos[j])
            if distancia < min_distancia:
                min_distancia = distancia
                par_cercano = (puntos[i], puntos[j])
    return par_cercano, min_distancia

# Uso con el archivo "datos_100.txt"
puntos = leer_puntos("datos_100.txt")
par_mas_cercano, distancia_minima = calcular_pares_mas_cercanos(puntos)

print(f"Par más cercano: {par_mas_cercano}")
print(f"Distancia mínima: {distancia_minima}")
