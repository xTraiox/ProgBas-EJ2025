# Se crea la funcion para determinar si el numero es primo
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1): # Itera desde 2 hasta la raíz cuadrada del número
        if numero % i == 0: # Verificar si el número es divisible por i
            return False
    return True

numero = int(input("Introduce un número: "))
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
