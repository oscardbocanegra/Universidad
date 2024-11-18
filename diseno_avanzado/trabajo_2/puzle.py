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
    board : list of int
        Una lista de enteros que representa el estado actual del puzzle.
    moves : int, optional
        Número de movimientos realizados para alcanzar este estado (por defecto es 0).
    previous : PuzzleState, optional
        El estado anterior del puzzle, usado para reconstruir el camino (por defecto es None).

    Attributes
    ----------
    board : list of int
        Estado actual del puzzle.
    moves : int
        Número de movimientos realizados hasta el momento.
    previous : PuzzleState
        Estado anterior en el camino hacia la solución.
    zero_index : int
        Índice de la posición del espacio vacío en `board`.
    priority : int
        Valor de prioridad calculado como la suma de los movimientos y la heurística de Manhattan.

    Examples
    --------
    >>> state = PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15])
    >>> state.manhattan_distance()
    1
    """

    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.zero_index = board.index(0)
        self.priority = self.moves + self.manhattan_distance()  # f(n) = g(n) + h(n)

    def manhattan_distance(self):
        """
        Calcula la heurística de distancia Manhattan.

        Returns
        -------
        int
            La suma de las distancias Manhattan de cada pieza a su posición objetivo.

        Notes
        -----
        La distancia Manhattan es utilizada como heurística para estimar el costo
        restante para resolver el puzzle desde el estado actual.
        """
        distance = 0
        for i, value in enumerate(self.board):
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
                new_board = self.board[:]
                new_board[self.zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[self.zero_index]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
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
        return self.board == GOAL_STATE

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


def count_inversions(board):
    """
    Cuenta el número de inversiones en el estado actual del puzzle.

    Parameters
    ----------
    board : list of int
        Lista de enteros representando el estado actual del puzzle.

    Returns
    -------
    int
        El número total de inversiones en el estado del puzzle.

    Notes
    -----
    Una inversión ocurre cuando un número mayor precede a un número menor.
    """
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions


def is_solvable(board):
    """
    Verifica si el puzzle es resoluble.

    Parameters
    ----------
    board : list of int
        Lista de enteros representando el estado actual del puzzle.

    Returns
    -------
    bool
        True si el puzzle es resoluble, False de lo contrario.

    Notes
    -----
    La resolubilidad depende del número de inversiones y la posición
    del espacio vacío.
    """
    inversions = count_inversions(board)
    zero_row = board.index(0) // 4
    if (inversions % 2 == 0 and zero_row % 2 != 0) or (inversions % 2 != 0 and zero_row % 2 == 0):
        return True
    return False


def solve_puzzle(initial_state):
    """
    Resuelve el puzzle de 15 piezas usando el algoritmo A* con ramificación y poda.

    Parameters
    ----------
    initial_state : list of int
        Lista de enteros representando el estado inicial del puzzle.

    Returns
    -------
    list of list of int or None
        El camino de solución desde el estado inicial hasta el objetivo, o None
        si no es alcanzable.

    Examples
    --------
    >>> solve_puzzle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12])
    """
    if not is_solvable(initial_state):
        print("La configuración inicial no es alcanzable.")
        return None
    
    open_set = []
    heapq.heappush(open_set, PuzzleState(initial_state))
    closed_set = set()
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.is_goal():
            return reconstruct_path(current_state)
        closed_set.add(tuple(current_state.board))
        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) not in closed_set:
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
        path.append(state.board)
        state = state.previous
    path.reverse()
    return path


def print_board(board, step):
    """
    Imprime el estado del puzzle de forma visual.

    Parameters
    ----------
    board : list of int
        El estado actual del puzzle a imprimir.
    step : int
        El número de paso en la secuencia de solución.
    """
    print(f"Paso {step}:")
    for i in range(0, 16, 4):
        print(board[i:i+4])
    print("-" * 10)


# Ejemplo de uso con un estado inicial
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12] # Cambiar a otras configuraciones si se desea

# Calcula el tiempo de ejecución
start_time = time.time()
solution_path = solve_puzzle(initial_state)
end_time = time.time()

# Muestra el resultado
if solution_path:
    print("Solución encontrada. Mostrando cada paso:")
    for step, board in enumerate(solution_path):
        print_board(board, step)
    print(f"Solución encontrada en {len(solution_path) - 1} movimientos.")
else:
    print("No se encontró solución.")

# Muestra el tiempo total de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.4f} segundos.")
