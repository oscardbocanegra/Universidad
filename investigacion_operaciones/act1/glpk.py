from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

# Crear el modelo
model = LpProblem("Estrategia_Produccion_BFI", LpMaximize)

# Variables de decisión
x1 = LpVariable("BodyPlus_100", lowBound=0, cat="Integer")
x2 = LpVariable("BodyPlus_200", lowBound=0, cat="Integer")

# Función objetivo
model += 371 * x1 + 361 * x2, "Utilidad_Total"

# Restricciones
model += 8 * x1 + 12 * x2 <= 600, "Mecanizado"
model += 5 * x1 + 10 * x2 <= 450, "Pintura"
model += 2 * x1 + 2 * x2 <= 140, "Ensamblaje"
model += 3 * x2 >= x1, "Restriccion_Estrategica"

# Resolver el modelo
model.solve()

# Resultados
print("=== RESULTADOS ===")
print(f"Estado de la solución: {LpStatus[model.status]}")
print(f"BodyPlus 100 a producir: {x1.varValue}")
print(f"BodyPlus 200 a producir: {x2.varValue}")
print(f"Utilidad total: ${value(model.objective)}")
