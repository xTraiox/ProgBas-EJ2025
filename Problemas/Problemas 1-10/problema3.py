num = int(input("Ingresa el numero: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print("El factorial de", num, "es", factorial)