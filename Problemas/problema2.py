num1= float(input("Ingresa el numero 1:"))
num2= float(input("Ingresa el numero 2:"))
operador= input("Ingrese el operador (+, -, *, /):")

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: División por cero")
else:
    print("El operador no es valido")





