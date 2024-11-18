"""
Este módulo resuelve el puzzle de 15 piezas utilizando el algoritmo A* con heurística de
distancia Manhattan y técnicas de ramificación y poda. Incluye funciones para verificar
la resolubilidad del puzzle, imprimir los pasos de la solución, y medir el tiempo de ejecución.
"""

import heapq
import time

# Representamos el objetivo del puzzle en una lista
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

# Definimos las posibles direcciones de movimiento
MOVES = {
    'up': -4,
    'down': 4,
    'left': -1,
    'right': 1
}

class PuzzleState:
    """
    Representa el estado del puzzle de 15 piezas.

    Esta clase encapsula la lógica para representar y manipular
    los diferentes estados en el proceso de resolver el puzzle.

    Parameters
    ----------
    state_board : list of int
        Una lista de enteros que representa el estado actual del puzzle.
    moves : int, optional
        Número de movimientos realizados para alcanzar este estado (por defecto es 0).
    previous : PuzzleState, optional
        El estado anterior del puzzle, usado para reconstruir el camino (por defecto es None).
    """
    def __init__(self, state_board, moves=0, previous=None):
        self.state_board = state_board
        self.moves = moves
        self.previous = previous
        self.zero_index = state_board.index(0)
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        """
        Calcula la heurística de distancia Manhattan.

        Returns
        -------
        int
            La suma de las distancias Manhattan de cada pieza a su posición objetivo.
        """
        distance = 0
        for i, value in enumerate(self.state_board):
            if value != 0:
                target_x, target_y = divmod(value - 1, 4)
                current_x, current_y = divmod(i, 4)
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def neighbors(self):
        """
        Genera los estados vecinos aplicando movimientos válidos.

        Returns
        -------
        list of PuzzleState
            Lista de objetos `PuzzleState` que representan los posibles
            movimientos desde el estado actual.
        """
        neighbors = []
        for move, position_change in MOVES.items():
            new_zero_index = self.zero_index + position_change
            if self.is_valid_move(move, new_zero_index):
                new_state_board = self.state_board[:]
                new_state_board[self.zero_index], new_state_board[new_zero_index] = (
                    new_state_board[new_zero_index],
                    new_state_board[self.zero_index]
                )
                neighbors.append(PuzzleState(new_state_board, self.moves + 1, self))
        return neighbors

    def is_valid_move(self, move, new_zero_index):
        """
        Valida si un movimiento es posible.

        Parameters
        ----------
        move : str
            El movimiento que se desea realizar ('up', 'down', 'left', 'right').
        new_zero_index : int
            El índice resultante si el movimiento es válido.

        Returns
        -------
        bool
            True si el movimiento es válido, False de lo contrario.
        """
        if new_zero_index < 0 or new_zero_index >= 16:
            return False
        if move == 'left' and self.zero_index % 4 == 0:
            return False
        if move == 'right' and self.zero_index % 4 == 3:
            return False
        return True

    def is_goal(self):
        """
        Verifica si el estado actual es el estado objetivo.

        Returns
        -------
        bool
            True si el estado actual es el objetivo, False de lo contrario.
        """
        return self.state_board == GOAL_STATE

    def __lt__(self, other):
        """
        Define la comparación de estados para la cola de prioridad.

        Parameters
        ----------
        other : PuzzleState
            Otro estado del puzzle con el cual comparar.

        Returns
        -------
        bool
            True si este estado tiene una prioridad menor que `other`.
        """
        return self.priority < other.priority


def count_inversions(state_board):
    """
    Cuenta el número de inversiones en el estado actual del puzzle.

    Parameters
    ----------
    state_board : list of int
        Lista de enteros representando el estado actual del puzzle.

    Returns
    -------
    int
        El número total de inversiones en el estado del puzzle.
    """
    inversions = 0
    for i in range(len(state_board)):
        for j in range(i + 1, len(state_board)):
            if state_board[i] > state_board[j] != 0:
                inversions += 1
    return inversions


def is_solvable(state_board):
    """
    Verifica si el puzzle es resoluble.

    Parameters
    ----------
    state_board : list of int
        Lista de enteros representando el estado actual del puzzle.

    Returns
    -------
    bool
        True si el puzzle es resoluble, False de lo contrario.
    """
    inversions = count_inversions(state_board)
    zero_row = state_board.index(0) // 4
    if (inversions % 2 == 0 and zero_row % 2 != 0) or (inversions % 2 != 0 and zero_row % 2 == 0):
        return True
    return False


def solve_puzzle(start_state):
    """
    Resuelve el puzzle de 15 piezas usando el algoritmo A* con ramificación y poda.

    Parameters
    ----------
    start_state : list of int
        Lista de enteros representando el estado inicial del puzzle.

    Returns
    -------
    list of list of int or None
        El camino de solución desde el estado inicial hasta el objetivo, o None
        si no es alcanzable.
    """
    if not is_solvable(start_state):
        print("La configuración inicial no es alcanzable.")
        return None
    
    open_set = []
    heapq.heappush(open_set, PuzzleState(start_state))
    closed_set = set()
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.is_goal():
            return reconstruct_path(current_state)
        closed_set.add(tuple(current_state.state_board))
        for neighbor in current_state.neighbors():
            if tuple(neighbor.state_board) not in closed_set:
                heapq.heappush(open_set, neighbor)
    return None


def reconstruct_path(state):
    """
    Reconstruye el camino de solución desde el estado objetivo.

    Parameters
    ----------
    state : PuzzleState
        El estado final del puzzle desde el cual reconstruir el camino.

    Returns
    -------
    list of list of int
        La lista de estados que forman el camino de solución.
    """
    path = []
    while state:
        path.append(state.state_board)
        state = state.previous
    path.reverse()
    return path


def print_board(state_board, solution_step):
    """
    Imprime el estado del puzzle de forma visual.

    Parameters
    ----------
    state_board : list of int
        El estado actual del puzzle a imprimir.
    solution_step : int
        El número de paso en la secuencia de solución.
    """
    print(f"Paso {solution_step}:")
    for i in range(0, 16, 4):
        print(state_board[i:i+4])
    print("-" * 10)


# Ejemplo de uso con un estado inicial
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12]

# (DIFICIL ) initial_state = [12, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 13, 6, 3]


# Calcula el tiempo de ejecución
start_time = time.time()
solution_path = solve_puzzle(initial_state)
end_time = time.time()

# Muestra el resultado
if solution_path:
    print("Solución encontrada. Mostrando cada paso:")
    for solution_step, state_board in enumerate(solution_path):
        print_board(state_board, solution_step)
    print(f"Solución encontrada en {len(solution_path) - 1} movimientos.")
else:
    print("No se encontró solución.")

# Muestra el tiempo total de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.4f} segundos.")
