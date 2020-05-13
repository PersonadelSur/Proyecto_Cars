
def cual_es_mi_nombre(nombre):
    print(nombre)


cual_es_mi_nombre("Andres")


def suma_de_numeros(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    if isinstance(numero1, int) and isinstance(numero2, int):
        print(int(numero1) + int(numero2))
    else:
        print("no son los datos numericos viejo")

dos = "dos"

suma_de_numeros(6, 100)


def suma_de_numeros(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print(int(numero1) + int(numero2))
    else:
        print("no son los datos numericos viejo")

dos = "dos"

suma_de_numeros(6, 100)
