import random

def quicksort(arr):
    """Ordena una lista usando el algoritmo Quicksort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def busqueda_binaria(arr, objetivo):
    """Realiza búsqueda binaria en una lista ordenada."""
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Generar lista aleatoria
tamano = int(input("Ingrese el tamaño de la lista: "))
lista = [random.randint(1, 100) for _ in range(tamano)]
print("Lista original:", lista)

# Ordenar lista
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)

# Búsqueda en la lista
num_buscar = int(input("Ingrese un número a buscar: "))
resultado = busqueda_binaria(lista_ordenada, num_buscar)
if resultado != -1:
    print(f"El número {num_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {num_buscar} no está en la lista.")
