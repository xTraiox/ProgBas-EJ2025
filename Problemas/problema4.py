num = int(input("Ingresa la cantidad de términos: "))

fibonacci = [0, 1]

for _ in range(num - 2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci[:num])
