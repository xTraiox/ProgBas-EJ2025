import random
import statistics
import matplotlib.pyplot as plt

def generar_datos(cantidad, minimo, maximo):
    """Genera una lista de datos aleatorios dentro de un rango"""
    datos = [random.randint(minimo, maximo) for _ in range(cantidad)]
    return datos

def analizar_datos(datos):
    """Calcula estadísticas básicas de los datos"""
    if len(datos) == 0:
        print("No hay datos para analizar.")
        return
    
    print(f"Datos: {datos}")
    print(f"Cantidad de datos: {len(datos)}")
    
    media = statistics.mean(datos)
    print(f"Media (Promedio): {media}")
    
    mediana = statistics.median(datos)
    print(f"Mediana: {mediana}")
    
    varianza = statistics.variance(datos) if len(datos) > 1 else 0
    print(f"Varianza: {varianza}")
    
    desviacion_estandar = statistics.stdev(datos) if len(datos) > 1 else 0
    print(f"Desviación estándar: {desviacion_estandar}")
    
def graficar_datos(datos):
    """Genera un histograma para los datos"""
    plt.hist(datos, bins=10, edgecolor='#000', color='#87CEEB')
    plt.title("Histograma de los Datos")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")

    plt.show()

menu = True

def menu():
    while menu:
        print("\n--- Generar y Analizar Datos Estadísticos ---")
        print("1. Generar datos aleatorios")
        print("2. Analizar datos")
        print("3. Graficar datos")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = int(input("Introduce la cantidad de datos a generar: "))
            minimo = int(input("Introduce el valor mínimo de los datos: "))
            maximo = int(input("Introduce el valor máximo de los datos: "))
            datos = generar_datos(cantidad, minimo, maximo)
            print(f"Datos generados: {datos}")

        elif opcion == "2":
            if 'datos' in locals() or 'datos' in globals():
                analizar_datos(datos)
            else:
                print("Primero debes generar los datos.")
        
        elif opcion == "3":
            if 'datos' in locals() or 'datos' in globals():
                graficar_datos(datos)
            else:
                print("Primero debes generar los datos.")
        
        elif opcion == "4":
            print("Saliendo....")
            break
        
        else:
            print("Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    menu()