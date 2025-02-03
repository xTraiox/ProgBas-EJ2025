# Definir listas para números pares e impares
par = []
impar = []

# Solicitar al usuario un límite
limite = int(input("Ingrese el límite: "))

# Clasificar los números en pares e impares
for num in range(1, limite + 1):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

# Determinar el tamaño máximo entre ambas listas
tamanio = max(len(par), len(impar))

# Imprimir los números en formato tabla
for item in range(tamanio):
    try:
        print(par[item], impar[item], sep=' | ')
    except IndexError:
        if item >= len(par):
            print("-", impar[item], sep=' | ')
        else:
            print(par[item], "-", sep=' | ')
