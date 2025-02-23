import numpy as np

def sumar_matrices(matriz1, matriz2):
    if matriz1.shape == matriz2.shape:
        return matriz1 + matriz2

def multiplicar_matrices(matriz1, matriz2):
    if matriz1.shape[1] == matriz2.shape[0]:
        return np.dot(matriz1, matriz2)

def transponer_matriz(matriz):
    return np.transpose(matriz)

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.array([[2, 0], [1, 2]])
    
    print("Matriz A:")
    print(A)
    print("Matriz B:")
    print(B)
    print("Suma de A y B:")
    print(sumar_matrices(A, B))
    print("Multiplicación de A y C:")
    print(multiplicar_matrices(A, C))
    print("Transposición de A:")
    print(transponer_matriz(A))
