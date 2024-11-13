import time
import heapq

def es_resoluble(tablero):
    """
    Verifica si el tablero es resoluble.
    
    Parameters
    ----------
    tablero : list
        La configuración del tablero de 15-puzzle en formato de lista de 16 elementos.
        
    Returns
    -------
    bool
        True si es resoluble, False en caso contrario.
    """
    # Implementa la verificación de la paridad

def resolver_puzzle(tablero_inicial, tablero_objetivo):
    """
    Resuelve el puzzle utilizando ramificación y poda.
    
    Parameters
    ----------
    tablero_inicial : list
        Configuración inicial del tablero.
    tablero_objetivo : list
        Configuración objetivo del tablero.
        
    Returns
    -------
    list
        La secuencia de pasos para resolver el puzzle.
    """
    # Implementación del algoritmo de búsqueda con ramificación y poda

def main():
    tablero_inicial = [4, 10, 1, 3, 16, 11, 7, 15, 6, 5, 14, 9, 13, 2, 8, 12]  # Ejemplo de tablero
    tablero_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    
    if es_resoluble(tablero_inicial):
        inicio = time.time()
        pasos = resolver_puzzle(tablero_inicial, tablero_objetivo)
        fin = time.time()
        for paso in pasos:
            print(paso)
        print(f"Solución encontrada en {fin - inicio} segundos.")
    else:
        print("La configuración objetivo no es alcanzable desde la configuración inicial.")

if __name__ == "__main__":
    main()
