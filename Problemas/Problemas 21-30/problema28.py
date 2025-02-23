titular = ""
saldo = 0

def iniciar_cuenta():
    global titular, saldo
    titular = input("Introduce el nombre del titular de la cuenta: ")
    saldo = 0
    print(f"Cuenta de {titular} iniciada con saldo inicial de {saldo}.")

def deposito(cantidad):
    global saldo
    if cantidad > 0:
        saldo += cantidad
        print(f"Has depositado {cantidad}. El nuevo saldo es: {saldo}")
    else:
        print("La cantidad a depositar debe ser mayor que cero.")

def retiro(cantidad):
    global saldo
    if cantidad > 0:
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Has retirado {cantidad}. El nuevo saldo es: {saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    else:
        print("La cantidad a retirar debe ser mayor que cero.")

def consultar_saldo():
    print(f"El saldo actual de la cuenta de {titular} es: {saldo}")

menu = True

def menu():
    iniciar_cuenta()
    while menu:
        print("\n--- Menú de la Cuenta Bancaria ---")
        print("1. Realizar depósito")
        print("2. Realizar retiro")
        print("3. Consultar saldo")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = float(input("Introduce la cantidad a depositar: "))
            deposito(cantidad)
        
        elif opcion == "2":
            cantidad = float(input("Introduce la cantidad a retirar: "))
            retiro(cantidad)
        
        elif opcion == "3":
            consultar_saldo()
        
        elif opcion == "4":
            print("Saliendo....")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
