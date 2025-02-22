def crear_pila():
    return []

def apilar(pila, item):
    pila.append(item)

def desapilar(pila):
    return pila.pop() if pila else "Pila vacía"

def cima(pila):
    return pila[-1] if pila else "Pila vacía"

def mostrar_pila(pila):
    return pila[::-1]  

def crear_cola():
    return []

def encolar(cola, item):
    cola.append(item)

def desencolar(cola):
    return cola.pop(0) if cola else "Cola vacía"

def frente(cola):
    return cola[0] if cola else "Cola vacía"

def mostrar_cola(cola):
    return cola


def crear_lista():
    return None  
def insertar_lista(lista, dato):
    if lista is None:
        return (dato, None)
    else:
        nodo = lista
        while nodo[1] is not None:
            nodo = nodo[1]
        nodo = (nodo[0], (dato, None))  
        return lista

def eliminar_lista(lista, dato):
    if lista is None:
        return None
    if lista[0] == dato:
        return lista[1]  

    nodo_actual = lista
    nodo_anterior = None
    while nodo_actual and nodo_actual[0] != dato:
        nodo_anterior = nodo_actual
        nodo_actual = nodo_actual[1]

    if nodo_actual is None:
        return lista  

    nodo_anterior = (nodo_anterior[0], nodo_actual[1])  
    return lista

def mostrar_lista(lista):
    elementos = []
    nodo = lista
    while nodo:
        elementos.append(nodo[0])
        nodo = nodo[1]
    return elementos


print(" Pila")
pila = crear_pila()
apilar(pila, 10)
apilar(pila, 20)
apilar(pila, 30)
print("Pila después de apilar:", mostrar_pila(pila))
print("Desapilar:", desapilar(pila))
print("Cima de la pila:", cima(pila))

print("\n Cola")
cola = crear_cola()
encolar(cola, 1)
encolar(cola, 2)
encolar(cola, 3)
print("Cola después de encolar:", mostrar_cola(cola))
print("Desencolar:", desencolar(cola))
print("Frente de la cola:", frente(cola))

print("\n Lista Enlazada")
lista = crear_lista()
lista = insertar_lista(lista, 100)
lista = insertar_lista(lista, 200)
lista = insertar_lista(lista, 300)
print("Lista enlazada:", mostrar_lista(lista))
lista = eliminar_lista(lista, 200)
print("Lista enlazada después de eliminar 200:", mostrar_lista(lista))
