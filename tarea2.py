# Cree un loop que imprima la sucesión de fibonacci F(n+1) --> 0,1,1,2,3,5,8,13,21,34...
# Tenga cuidado de que no entre en un loop eterno, para ello puede iterar en algun rango, ej. for i in range(20):



n = 0
f = n + 1


def fibonacci(n, f):
    for a in n:
        for b in f:
            print(a + b)



def fibonacci(rango):
    numeros = []
    for i in range(rango):
        if i == 0:
            a = 0
            numeros.append(a)
        elif i <= 1:
            a = numeros[i-1] + i
            numeros.append(a)
        else:
            a = numeros[i-1] + numeros[i-2]
            numeros.append(a)
        print(a)

fibonacci(15)





# Importe la bliblioteca time y use la función time.sleep(2) en su ejercicio anterior para poner una pausa en cada iteración de fibonacci
# Puede cambiar el argumento "2" dentro de time.sleep para variar la duración de la pausa


import time


# Cree una función que haga una nueva lista con todos los menus posibles vistos en la clase anterior



carbohidratos = ["arroz", "papas", "pan"]
vegetales = ["apio", "tomate", "lechuga"]

def menus_disponibles(carbohidratos, vegetales):
    for a in carbohidratos:
        for b in vegetales:
            print(a + "con" + b)

menus_disponibles(carbohidratos, vegetales)

menus = []
menus.append


comidas = [["arroz", "papas", "pan"], ["apio", "tomate", "lechuga"]]

