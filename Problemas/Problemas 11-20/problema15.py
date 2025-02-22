def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): # Funcion para Verificar si es bisiesto
        return True
    return False

# Pedir el año al usuario
año = int(input("Ingresa un año: "))


if bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
