import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

if __name__ == "__main__":
    print("Lanzamiento de un dado:", lanzar_dado())
    print("Lanzamiento de una moneda:", lanzar_moneda())
