def Burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def selection_sort(lista):
    for i in range(len(lista)):
        mini = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[mini]:
                mini = j
        lista[i], lista[mini] = lista[mini], lista[i]
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menor = [x for x in lista[1:] if x < pivote]
    mayor = [x for x in lista[1:] if x >= pivote]
    return quick_sort(menor) + [pivote] + quick_sort(mayor)

def menu():
    lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))
    print("\nMétodos de ordenamiento disponibles:")
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. Merge Sort")
    print("5. Quick Sort")

    opcion = int(input("Elige un método (1-5): "))

    if opcion == 1:
        print("Lista ordenada (Bubble Sort):", Burbuja(lista))
    elif opcion == 2:
        print("Lista ordenada (Insertion Sort):", insertion_sort(lista))
    elif opcion == 3:
        print("Lista ordenada (Selection Sort):", selection_sort(lista))
    elif opcion == 4:
        print("Lista ordenada (Merge Sort):", merge_sort(lista))
    elif opcion == 5:
        print("Lista ordenada (Quick Sort):", quick_sort(lista))
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
