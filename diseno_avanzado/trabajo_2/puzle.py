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

# Clase para representar el estado del puzzle y sus movimientos
class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.zero_index = board.index(0)
        self.priority = self.moves + self.manhattan_distance()  # f(n) = g(n) + h(n)

    # Calcula la distancia Manhattan como heurística
    def manhattan_distance(self):
        distance = 0
        for i, value in enumerate(self.board):
            if value != 0:
                target_x, target_y = divmod(value - 1, 4)
                current_x, current_y = divmod(i, 4)
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    # Genera los estados vecinos aplicando movimientos válidos
    def neighbors(self):
        neighbors = []
        for move, position_change in MOVES.items():
            new_zero_index = self.zero_index + position_change
            if self.is_valid_move(move, new_zero_index):
                new_board = self.board[:]
                # Intercambiamos el valor de la casilla vacía
                new_board[self.zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[self.zero_index]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    # Valida si un movimiento es posible
    def is_valid_move(self, move, new_zero_index):
        if new_zero_index < 0 or new_zero_index >= 16:
            return False
        if move == 'left' and self.zero_index % 4 == 0:
            return False
        if move == 'right' and self.zero_index % 4 == 3:
            return False
        return True

    # Verifica si el estado actual es el estado objetivo
    def is_goal(self):
        return self.board == GOAL_STATE

    # Define comparación de estados para la cola de prioridad
    def __lt__(self, other):
        return self.priority < other.priority

# Función para contar inversiones
def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions

# Función para verificar si el puzzle es resoluble
def is_solvable(board):
    inversions = count_inversions(board)
    zero_row = board.index(0) // 4  # Fila en la que se encuentra el espacio vacío
    # El puzzle es resoluble si el número de inversiones y la posición del espacio vacío cumplen ciertas condiciones
    if (inversions % 2 == 0 and zero_row % 2 != 0) or (inversions % 2 != 0 and zero_row % 2 == 0):
        return True
    return False

# Función de resolución usando A* con ramificación y poda
def solve_puzzle(initial_state):
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

# Reconstruye el camino de solución desde el estado objetivo
def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    path.reverse()
    return path

# Función para imprimir el estado del puzzle de forma visual
def print_board(board, step):
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
