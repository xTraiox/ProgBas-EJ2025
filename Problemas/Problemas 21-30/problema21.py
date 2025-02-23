# 21. Calcular el area y volumen de distintas figuras geometricas.
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def area_cuadrado(lado):
    return lado ** 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

if __name__ == "__main__":
    print("Area de un círculo de radio 5:", area_circulo(5))
    print("Volumen de una esfera de radio 5:", volumen_esfera(5))
    print("Area de un rectangulo de 4x6:", area_rectangulo(4, 6))
    print("Area de un triangulo de base 4 y altura 8:", area_triangulo(4, 8))
    print("Volumen de una piramide con base 15 y altura 5:", volumen_piramide(15, 5))
    print("Area de un cuadrado de lado 4:", area_cuadrado(4))
    print("Volumen de un cubo de lado 4:", volumen_cubo(4))
    print("Volumen de un cilindro de radio 5 y altura 10:",  "{0:.5f}".format(volumen_cilindro(5, 10)))
