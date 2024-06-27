deudores = {}
cont = 0

print("Ingrese los 5 RUT de los deudores.")
while True:
    print()
    rut = input("Ingrese RUT del deudor: ")
    valor = int(input("Ingrese deuda en pesos: "))
    deudores[rut] = valor
    cont = cont + 1

    if cont >= 5:
        break

print()
print("Ingrese RUT de los deudores y abonos correspondientes.")
while True:
    print()
    rut = input("Ingrese RUT del deudor: ")

    if rut == "":
        break

    abono = int(input("Ingrese abono: "))

    if rut in deudores:
        deudores[rut] -= abono
        if deudores[rut] <= 0:  
            del(deudores[rut])
    else:
        print("RUT no encontrado. Intente nuevamente.")

print(deudores)
