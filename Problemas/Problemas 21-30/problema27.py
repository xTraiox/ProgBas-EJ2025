def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {
        "metros": 1,
        "kilometros": 1000,
        "centimetros": 0.01,
        "milimetros": 0.001,
        "pulgadas": 0.0254,
        "pies": 0.3048,
        "yardas": 0.9144
    }
    
    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        return "Unidades no válidas"
    
    valor_en_metros = valor * conversiones[unidad_origen]
    valor_convertido = valor_en_metros / conversiones[unidad_destino]
    return valor_convertido

def convertir_peso(valor, unidad_origen, unidad_destino):
    conversiones = {
        "kilogramos": 1,
        "gramos": 0.001,
        "toneladas": 1000,
        "libras": 0.453592,
        "onzas": 0.0283495
    }

    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        return "Unidades no válidas"
    
    valor_kg = valor * conversiones[unidad_origen]
    valor_convertido = valor_kg / conversiones[unidad_destino]
    
    return valor_convertido

menu = True

def menu():
    while menu:
        print("\n--- Conversor de Unidades ---")
        print("1. Convertir Longitud")
        print("2. Convertir Peso")
        print("3. Convertir Temperatura")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = float(input("Introduce el valor a convertir: "))
            unidad_origen = input("Introduce la unidad de origen (metros, kilometros, centimetros, milimetros, pulgadas, pies, yardas): ").lower()
            unidad_destino = input("Introduce la unidad de destino (metros, kilometros, centimetros, milimetros, pulgadas, pies, yardas): ").lower()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}")
        
        elif opcion == "2":
            valor = float(input("Introduce el valor a convertir: "))
            unidad_origen = input("Introduce la unidad de origen (kilogramos, gramos, toneladas, libras, onzas): ").lower()
            unidad_destino = input("Introduce la unidad de destino (kilogramos, gramos, toneladas, libras, onzas): ").lower()
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}")
        
        elif opcion == "3":
            print("Saliendo....")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
