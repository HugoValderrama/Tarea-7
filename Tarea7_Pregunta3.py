supermercado = {}

while True:

    producto = input("Ingrese el nombre del producto (Ent para Salir): ")

    if producto == "":
        break

    cantidad = int(input("Ingrese la cantidad del producto: "))

    supermercado[producto] = cantidad

print()
num = int(input("Ingrese multiplicador para la cantidad: "))

for producto, cantidad in supermercado.items():

    cant_multiplicada = cantidad * num

    print()
    print("Producto: ", producto, " - Cantidad original: ", cantidad, " - Cantidad multiplicada: ", cant_multiplicada)
