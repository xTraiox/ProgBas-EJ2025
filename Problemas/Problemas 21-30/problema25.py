import numpy as np
import matplotlib.pyplot as plt

def generar_datos(cantidad, rango=(0, 100)):
    """ Genera una lista de números aleatorios dentro de un rango especificado. """
    return np.random.randint(rango[0], rango[1], cantidad)

def graficar_histograma(datos, bins=10):
    """ Genera y muestra un histograma a partir de una lista de datos. """
    plt.hist(datos, bins=bins, edgecolor='#000', color='#87CEEB')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

if __name__ == "__main__":
    datos = generar_datos(1000, (0, 100))
    graficar_histograma(datos, bins=20)
