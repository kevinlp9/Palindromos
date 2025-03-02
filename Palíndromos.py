import random
from random import randint

def generar_palindromo():
    print("\n<<< GENERADOR DE PALÍNDROMOS BINARIOS >>>\n")
    mod = input("1) MODO MANUAL  2) MODO AUTÓMATICO \n")

    if mod == "1":
        tam = int(input("INGRESE LA LONGITUD: "))
    else:
        tam = randint(0, 10000)

    gram = open("Gramática.txt", "w")
    gram.write("TAMAÑO DE CADENA: " + str(tam) + "\n")
    l = int(tam / 2)
    if (tam % 2 != 0):
        print("\n --- PALÍNDROMO IMPAR --- \n")
        imp = 1
    else:
        print("\n --- PALÍNDROMO PAR --- \n")
        imp = 0

    pal = "P"

    for i in range(0, l + 1):
        if i == l:
            final = pal.split()

            if imp == 0:
                print("REGLA 1 APLICADA (P -> e)")
                gram.write("REGLA 1 APLICADA (P -> e)")
                final.remove("P")
                print(final)
                gram.write(str(final) + "\n")

            if imp == 1:
                reglas1 = randint(2, 3)
                if reglas1 == 2:
                    print("REGLA 2 APLICADA (P -> 0)")
                    gram.write("REGLA 2 APLICADA (P -> 0) ")
                    final[l] = "0"
                    print(final)
                    gram.write(str(final) + "\n")
                if reglas1 == 3:
                    print("REGLA 3 APLICADA (P -> 1)")
                    gram.write("REGLA 3 APLICADA (P -> 1) ")
                    final[l] = "1"
                    print(final)
                    gram.write(str(final) + "\n")

        else:
            reglas2 = randint(4, 5)
            if reglas2 == 4:
                print("REGLA 4 APLICADA (P -> 0P0)")
                gram.write("REGLA 4 APLICADA (P -> 0P0) ")
                pal = "0 " + pal + " 0"
                print(pal)
                gram.write(str(pal) + "\n")

            if reglas2 == 5:
                print("REGLA 5 APLICADA (P -> 1P1)")
                gram.write("REGLA 5 APLICADA (P -> 1P1) ")
                pal = "1 " + pal + " 1"
                print(pal)
                gram.write(str(pal) + "\n")

        print("\n")


while True:
    generar_palindromo()

    opcion = input("¿DESEA GENERAR OTRO PALÍNDROMOS? (s/n): ").lower()
    if opcion != 's':
        break
