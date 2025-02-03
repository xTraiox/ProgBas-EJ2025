import math

def calcular(r):
    area = math.pi * r**2
    circunferencia = 2 * math.pi * r
    return area, circunferencia

r = float(input("Introduce el radio del círculo: "))

area, circunferencia = calcular(r)

# Mostrar resultados con 2 decimales
print(f"Área del círculo: {area:.2f}")
print(f"Circunferencia del círculo: {circunferencia:.2f}")
