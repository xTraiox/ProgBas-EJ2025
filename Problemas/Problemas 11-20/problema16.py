def contar_vocales(cadena):
    # Definir las Vocales
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0

    # Recorrer la cadena caracter por caracter
    for caracter in cadena:
            if caracter in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
    return num_vocales, num_consonantes

cadena = input("Ingresa una cadena de texto: ")

# Llamar a la función
vocales, consonantes = contar_vocales(cadena)

print(f"Número de Vocales: {vocales}")
print(f"Número de Consonantes: {consonantes}")
