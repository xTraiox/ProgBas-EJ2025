def lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  
    return -1  

def binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  

# Menú 
def main():
    lista = list(map(int, input("Ingrese una lista de números ordenados (separados por espacios): ").split()))
    objetivo = int(input("Ingrese el número a buscar: "))

    print("\nElige el método de búsqueda:")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")
    opcion = input("Opción: ")

    if opcion == "1":
        resultado = lineal(lista, objetivo)
    elif opcion == "2":
        resultado = binaria(lista, objetivo)
    else:
        print("Opción no válida")
        return

    if resultado != -1:
        print(f"Elemento encontrado en la posición {resultado}")
    else:
        print("Elemento no encontrado")

if __name__ == "__main__":
    main()
