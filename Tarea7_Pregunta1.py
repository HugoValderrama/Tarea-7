numeros = []
cont = 0

while True:

    num = int(input("Ingrese número deseado: "))
    numeros.append(num)
    cont = cont + 1

    if cont >= 10:
        break

numeros_reversa = numeros.copy()
numeros_reversa.reverse()
print()
print(numeros_reversa)
