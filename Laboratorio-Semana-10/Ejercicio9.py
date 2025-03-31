def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        return "No se puede dividir por cero."
    return a / b


class Calculadora:
    def __init__(self):
        self.resultado = 0

    def operar(self, operacion, a, b):
        if operacion == "sumar":
            self.resultado = sumar(a, b)
        elif operacion == "restar":
            self.resultado = restar(a, b)
        elif operacion == "multiplicar":
            self.resultado = multiplicar(a, b)
        elif operacion == "dividir":
            self.resultado = dividir(a, b)
        return self.resultado


def ejemplo_imperativo():
    print("Ejemplo de código imperativo:")
    # Solicitar al usuario dos números
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{b} es mayor que {a}")
    else:
        print("Los números son iguales.")

    for i in range(a, b + 1):
        print(i, end=" ")
    print()


def ejemplo_estructurado():
    print("\nEjemplo de código estructurado:")
    a = 10
    b = 5
    print(f"Resultado de sumar {a} y {b}: {sumar(a, b)}")
    print(f"Resultado de restar {a} y {b}: {restar(a, b)}")


def main():
    print("Bienvenido al programa que implementa múltiples paradigmas de programación")

    ejemplo_imperativo()

    ejemplo_estructurado()

    a = 12
    b = 4
    print(f"\nSumar usando el módulo: {sumar(a, b)}")
    print(f"Restar usando el módulo: {restar(a, b)}")

    calculadora = Calculadora()
    print(f"\nUsando la calculadora (objeto):")
    print(f"Resultado de sumar 15 y 7: {calculadora.operar('sumar', 15, 7)}")
    print(f"Resultado de dividir 20 entre 4: {calculadora.operar('dividir', 20, 4)}")


if __name__ == "__main__":
    main()
