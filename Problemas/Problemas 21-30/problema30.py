# 1. Factorial de un numero
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 

# 2. Secuencia de Fibonacci
def fibonacci(n):
    if n <= 1: 
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

# 3. Busqueda recursiva de un elemento en una lista
def buscar_elemento(lista, valor, indice=0):
    if indice >= len(lista):
        return -1
    if lista[indice] == valor:  
        return indice
    else:
        return buscar_elemento(lista, valor, indice + 1) 

menu = True

def menu():
    while menu:
        print("\n--- Funciones Recursivas ---")
        print("1. Calcular Factorial")
        print("2. Secuencia de Fibonacci")
        print("3. Buscar un elemento en una lista")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            n = int(input("Introduce el numero para calcular su factorial: "))
            print(f"El factorial de {n} es: {factorial(n)}")
        
        elif opcion == "2":
            n = int(input("Introduce el número para calcular su valor en la secuencia de Fibonacci: "))
            print(f"El valor de Fibonacci para {n} es: {fibonacci(n)}")
        
        elif opcion == "3":
            lista = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]
            valor = int(input("Introduce el valor a buscar: "))
            resultado = buscar_elemento(lista, valor)
            if resultado != -1:
                print(f"El valor {valor} se encuentra en el índice {resultado}.")
            else:
                print(f"El valor {valor} no fue encontrado en la lista.")
        
        elif opcion == "4":
            print("Saliendo....")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
