def convertir_temperatura(valor, escala_convertir, escala_final): #Crear la funcion para Realizar la conversión
    if escala_convertir == "Celsius":
        if escala_final == "Fahrenheit":
            return (valor * 9/5) + 32
        elif escala_final == "Kelvin":
            return valor + 273.15
    elif escala_convertir == "Fahrenheit":
        if escala_final == "Celsius":
            return (valor - 32) * 5/9
        elif escala_final == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif escala_convertir == "Kelvin":
        if escala_final == "Celsius":
            return valor - 273.15
        elif escala_final == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
    return None  

# Solicitar la temperatura y las escalas
valor = float(input("Ingresa la temperatura: "))
escala_convertir = input("Ingresa la escala a convertir (Celsius, Fahrenheit, Kelvin): ")
escala_final = input("Ingresa la escala a la que la quieres convertir (Celsius, Fahrenheit, Kelvin): ")

# Realizar la conversión
resultado = convertir_temperatura(valor, escala_convertir, escala_final)
if resultado is not None:
    print(f"{valor} grados {escala_convertir} son {resultado} grados {escala_final}")
else:
    print("Escalas no válidas.")
