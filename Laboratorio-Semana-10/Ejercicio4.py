import statistics

def calcular_estadisticas(*args):

    if not args:
        return "No se ingresaron números."
    
    promedio = lambda nums: sum(nums) / len(nums)  # Cálculo de promedio con lambda
    mediana = statistics.median(args)  # Uso de la función median de statistics
    desviacion_estandar = statistics.stdev(args) if len(args) > 1 else 0  # Cálculo de desviación estándar
    
    return promedio(args), mediana, desviacion_estandar

try:
    numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
    
    # Calcular estadísticas
    resultado = calcular_estadisticas(*numeros)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Promedio: {resultado[0]:.2f}")
        print(f"Mediana: {resultado[1]:.2f}")
        print(f"Desviación estándar: {resultado[2]:.2f}")
except ValueError:
    print("Error: Asegúrese de ingresar solo números separados por espacios.")
