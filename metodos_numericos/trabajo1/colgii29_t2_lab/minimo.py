# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
    a = [str() for _ in range(50)]
    print("Ingrese cantidad de datos: ")
    n = float(input())

    for i in range(1, int(n) + 1):
        print("Ingrese el dato ", i, ":")
        a[i-1] = input()

    min = float(a[0])
    for i in range(2, int(n) + 1):
        if float(a[i-1]) < min:
            min = float(a[i-1])

    print("El mínimo de los", n, "números es:", min)

