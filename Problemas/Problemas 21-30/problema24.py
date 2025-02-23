
def suma_serie(n):
    """
    Calcula la suma de la serie 1 + 2 + 3 + ... + n
    """
    return sum(range(1, n + 1))

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    print(f"La suma de la serie hasta {num} es: {suma_serie(num)}")
