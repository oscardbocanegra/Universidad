def cuadratica(a, b, c, x):
    return a * x**2 + b * x + c

def derivada_cuadratica(a, b, x):
    return 2 * a * x + b

def newton_raphson(a, b, c, x0, iteraciones):
    for i in range(iteraciones):
        f = cuadratica(a, b, c, x0)
        df = derivada_cuadratica(a, b, x0)
        
        x0 = x0 - f / df

        print(f"Iteración {i + 1}: x = {x0}")

    return x0

# Solicitar datos al usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
x0 = float(input("Ingrese la estimación inicial x0: "))
iteraciones = int(input("Ingrese el número de iteraciones: "))

# Llamar a la función Newton-Raphson
raiz = newton_raphson(a, b, c, x0, iteraciones)

print(f"La raíz aproximada es: {raiz}")
