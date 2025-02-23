contactos = {}

def agregar(nombre, telefono):
    if nombre in contactos:
        print(f"El contacto {nombre} ya existe.")
    else:
        contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado exitosamente.")

def eliminar(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"No se encontró el contacto {nombre}.")

def mostrar():
    if not contactos:
        print("La agenda está vacía.")
    else:
        print("Contactos en la agenda:")
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")

menu = True

def menu():
    while menu:
        print("\n--- Menú de la Agenda ---")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Mostrar contactos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            agregar(nombre, telefono)
        elif opcion == "2":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            eliminar(nombre)
        elif opcion == "3":
            mostrar()
        elif opcion == "4":
            print("Saliendo....")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
