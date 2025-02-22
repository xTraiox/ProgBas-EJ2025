import math
from fractions import Fraction
from decimal import Decimal

def resolver(a, b, c):     # Funcion para Resolver la ecuación cuadrática
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones reales: x1 = {raiz1}, x2 = {raiz2}"
    elif discriminante == 0:
        raiz = -b / (2*a)
        return f"Una solución real: x = {raiz}"
    else:
        real = -b / (2*a)
        imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        return f"Dos soluciones complejas: x1 = {Fraction(Decimal(real))} + {Fraction(Decimal(imaginaria))}i, x2 = {Fraction(Decimal(real))} - {Fraction(Decimal(imaginaria))}i"

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if a == 0:
    print("No es una ecuación cuadrática, 'a' no puede ser 0.")
else:
    resultado = resolver(a, b, c)
    print(resultado)
