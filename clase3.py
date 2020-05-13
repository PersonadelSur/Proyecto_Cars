#Diccionarios

persona1 = {"edad":10, "nombre": "Marcos"}
persona2 = {"edad":12, "nombre": "Jaime"}

personas = [persona1, persona2]

persona3 = persona2.copy()

persona3.update({"nombre": "Andres"})

print(persona3["nombre"] + " y " + persona2["nombre"])

#if ==, !=, >, <

def quien_es_mayor(var1, var2):
    if var1["edad"] > var2["edad"]:
        print(var1["nombre"] + " es mayor")
    else:
        print(var2["nombre"] + " es mayor")

quien_es_mayor(persona1, persona2)


def quien_es_mayor2(var1, var2):
    if var1["edad"] > var2["edad"]:
        print(var1["nombre"] + " es mayor")
    elif var1["edad"] < var2["edad"]:
        print(var2["nombre"] + " es mayor")
    elif var1["edad"] == var2["edad"]:
        print(" Ambas personas tienen la misma edad")
    else: 
        pass

quien_es_mayor2(persona1, persona2)

persona1.update({"edad": persona2["edad"]})

persona1.update({"poder": 5})
persona2.update({"poder": 7})
persona3['poder'] = 8

#loop while

import time
import random

def torneo_de_pelea(var1, var2):
    peleas = 0
    while peleas <= 10:
        if var1["poder"] > var2["poder"]:
            print(var1["nombre"] + " le sacó la cresta a " + var2["nombre"])
            var2["poder"] += random.randint(0,2)
            peleas +=1
        elif var1["poder"] < var2["poder"]:
            print(var2["nombre"] + " le sacó la cresta a " + var1["nombre"])
            var1["poder"] += random.randint(0,3)
            peleas +=1
        else:
            print("Empataron y se fueron a entrenar")
            var1["poder"] += random.randint(0,2)
            var2["poder"] += random.randint(0,3)
            peleas += 1
            time.sleep(3)


Torneo_de_pelea(persona1, persona2)

#time.sleep() datetime()
import time

def Torneo_de_peleav2(var1, var2):
    peleas = 0
    while peleas <= 10:
        if var1["Poder"] > var2["Poder"]:
            print(var1["nombre"] + " le sacó la ctm a " + var2["nombre"])
            var2["Poder"] += random.randint(0,2)
            peleas += 1
            time.sleep(3)
        elif var2["Poder"] > var1["Poder"]:
            print(var2["nombre"] + " le sacó la ctm a " + var1["nombre"])
            var1["Poder"] += random.randint(0,3)
            peleas += 1
            time.sleep(3)
        else:
            print("Empataron y se fueron a entrenar")
            var1["Poder"] += random.randint(0,3)
            var2["Poder"] += random.randint(0,2)
            peleas += 1
            time.sleep(3)

