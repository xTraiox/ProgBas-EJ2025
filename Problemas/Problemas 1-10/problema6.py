def interes_compuesto(Capital_Inicial, Tasa, Anual, Tiempo): # Se crea la funcion para el interes compuesto
    A = Capital_Inicial * (1 + Tasa / Anual) ** (Anual * Tiempo) # Formula
    return round(A, 2)


Capital_Inicial = float(input("Ingrese la Capital Inicial:"))       # Capital inicial
Tasa = float(input("Ingrese la Tasa de interés anual:"))            # Tasa de interés anual
Anual = float(input("Ingrese la Capitalización anual:"))            # Capitalización anual
Tiempo = float(input("Ingrese el Tiempo en años:"))                 # Tiempo en años

monto_final = interes_compuesto(Capital_Inicial, Tasa, Anual, Tiempo)
interes = round(monto_final - Capital_Inicial, 2)

print(f"Monto final: {monto_final}")
print(f"Interés generado: {interes}")
