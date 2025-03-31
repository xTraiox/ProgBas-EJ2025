class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        self.productos.append({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' agregado correctamente.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado correctamente.")
                return
        print(f"Producto '{nombre}' no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print("Información del producto:")
                print(producto)
                return
        print(f"Producto '{nombre}' no encontrado.")

    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x["precio"])
        print("Productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

# Programa principal
inventario = Inventario()

while True:
    print("\nMenú de Inventario:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar productos ordenados por precio")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        inventario.agregar_producto(nombre, categoria, precio, cantidad)
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)
    elif opcion == "4":
        inventario.mostrar_productos_ordenados()
    elif opcion == "5":
        print("Saliendo del sistema de inventario.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
