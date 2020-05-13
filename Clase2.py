#funciones predefinidas: int, str, float, lst, dict
dos = "dos"
tres = 3
type(tres)
tres = str(tres)
type(tres)

def division(valor1, valor2):
    return valor1 / valor2


division(6, 4)

division(6.25, 7)

division(valor1, valor2)

def division2(valor1, valor2):
    try:
        resultado = valor1 / valor2
    except:
        resultado = "No se pueden dividir"
    return resultado

division2(6, dos)

division2(6, tres)

division2(6, int(tres))

#atributos: .split()

vladimir = "Vladimir Painequeo"

valentin = vladimir.replace("Vladimir", "Valentín")

lista_valentin = valentin.split(" ")

apellido_valentin = valentin.split(" ")[1]

nombre_valentin = valentin.split(" ")[0]


#listas

vegetales = ["apio", "lechuga", "palta"]

apio = vegetales[0]

vegetales.append("tomate")
vegetales.remove("apio")

print(vegetales)


carbohidratos = ["arroz", "pan", "papas"]

#librerías
import random

print(random.choice(vegetales))


help(random)

def Sugerencia_comida(carbohidratos, vegetales):
    print(random.choice(carbohidratos) + " con " + random.choice(vegetales))

#loop for
def todos_los_carbohidratos(carbohidratos):
    for element in carbohidratos:
        print(element)

def menus_posibles(carbohidratos, vegetales):
    for element in carbohidratos:
        for elemento in vegetales:
            print(element + " con " + elemento)   



#Diccionarios
persona1 = {"edad":10, "nombre": "Marcos", "poder": 5}
persona2 = {"edad":12 ,"nombre": "Jaime", "poder": 7}

#If


#Loop while


#time.sleep() datetime()