def verificar_numero(n, m):
    if n % 2 == 0:     # Verifica si es un numero par
        print(f"{n} es un número par.")
    else:
        print(f"{n} es un número impar.")
    
    if n % m == 0:     # Verifica si es multiplo
        print(f"{n} es múltiplo de {m}.")
    else:
        print(f"{n} no es múltiplo de {m}.")

# Mostrar resultados
n = int(input("Introduce el número a verificar: "))
m = int(input("Introduce el número para verificar si es múltiplo: "))

verificar_numero(n, m)
