palabras = []

while True:

    palabra = input("Ingrese palabra deseada (Ent para finalizar): ")

    if palabra == "":
        break

    palabras.append(palabra)

for palabra in palabras:

    print()
    cantidad_a = palabra.count("a") + palabra.count("A")
    print(f"La palabra '{palabra}' tiene {cantidad_a} letras 'A' o 'a'.")