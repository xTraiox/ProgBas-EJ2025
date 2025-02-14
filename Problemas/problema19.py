import random
import numpy as np

def generador():
    print("\nElige una distribución:")
    print("1. Uniforme")
    print("2. Normal")
    print("3. Binomial")

    opcion = input("Opción: ")

    if opcion == "1":
        a = float(input("Ingrese el valor mínimo: "))
        b = float(input("Ingrese el valor máximo: "))
        cantidad = int(input("Cantidad de números a generar: "))
        numeros = [random.uniform(a, b) for _ in range(cantidad)]

    elif opcion == "2":
        mu = float(input("Ingrese la media:"))
        sigma = float(input("Ingrese la desviación estándar: "))
        cantidad = int(input("Cantidad de números a generar: "))
        numeros = [random.gauss(mu, sigma) for _ in range(cantidad)]

    elif opcion == "3":
        n = int(input("Ingrese el número de intentos: "))
        p = float(input("Ingrese la probabilidad de éxito: "))
        cantidad = int(input("Cantidad de números a generar: "))
        numeros = np.random.binomial(n, p, cantidad)

    else:
        print("Opción no válida.")
        return

    print("\nNúmeros generados:")
    print(numeros)

if __name__ == "__main__":
    while True:
        generador()
