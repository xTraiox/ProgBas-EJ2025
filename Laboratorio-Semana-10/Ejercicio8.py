def mergesort(arr):
    """Ordena una lista usando el algoritmo Mergesort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Función auxiliar para combinar dos listas ordenadas."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Solicitar al usuario que ingrese los números
datos = input("Ingrese una lista de números separados por espacio: ")
lista = list(map(int, datos.split()))

# Mostrar lista antes del ordenamiento
print("Lista original:", lista)

# Ordenar lista con Mergesort
lista_ordenada = mergesort(lista)

# Mostrar lista después del ordenamiento
print("Lista ordenada con Mergesort:", lista_ordenada)
