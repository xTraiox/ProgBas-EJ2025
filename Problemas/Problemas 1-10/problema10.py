def leer(nombre):
        with open(nombre, 'r') as archivo:
            return archivo.read()

def escribir(nombre, texto):
    with open(nombre, 'w') as archivo:
        archivo.write(texto)

archivo = "archivo.txt"
texto = input("Introduce el texto para escribir en el archivo: ")
escribir(archivo, texto)
print("Contenido actual del archivo:")
print(leer(archivo))
