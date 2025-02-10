def palindromo(cadena):
    return cadena == cadena[::-1]

texto = input("Ingresa una cadena: ")
if palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
