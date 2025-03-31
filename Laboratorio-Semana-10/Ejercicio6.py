class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_informacion(self):
        """Muestra la información del vehículo."""
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio:,.2f}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, numero_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.numero_puertas = numero_puertas
    
    def mostrar_informacion(self):
        """Muestra la información del automóvil."""
        return super().mostrar_informacion() + f", Número de puertas: {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_informacion(self):
        """Muestra la información de la motocicleta."""
        return super().mostrar_informacion() + f", Cilindrada: {self.cilindrada} cc"

# Ejemplo de uso
auto = Automovil("Toyota", "Corolla", 2022, 20000, 4)
moto = Motocicleta("Yamaha", "YZF-R3", 2021, 5500, 321)

print(auto.mostrar_informacion())
print(moto.mostrar_informacion())
