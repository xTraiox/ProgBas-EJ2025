import conversor

def main():
    while True:
        print("\nMenú de Conversión:")
        print("1. Kilómetros a Millas")
        print("2. Celsius a Fahrenheit")
        print("3. Litros a Galones")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            km = float(input("Ingrese la cantidad de kilómetros: "))
            print(f"{km} km equivale a {conversor.km_a_millas(km):.2f} millas.")
        elif opcion == "2":
            c = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{c}°C equivale a {conversor.celsius_a_fahrenheit(c):.2f}°F.")
        elif opcion == "3":
            litros = float(input("Ingrese la cantidad de litros: "))
            print(f"{litros} L equivale a {conversor.litros_a_galones(litros):.2f} galones.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
