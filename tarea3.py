#Ejercicio1
#Escriba funcion que meta los valores del 1 al 100 en una lista.

#Ejercicio2
#Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].

#Ejercicio3
#Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
#Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.

#Ejercicio4
#Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo orden.

#Ejercicio5
# Cree un contador dentro de su función que estime la cantidad de número pares que hay dentro de su sucesion de fibonacci,
# para esto puede usar una comparación entre el número // 2 y el número / 2, solo en caso de los pares, esto debería ser verdad
# además se recomienda definir la variable count = 0 antes del loop


#EX1

centenar = []

def tarea1(numero):
    for i in range(100):
        centenar.append(i+1)
    else:
        pass

Solve = tarea1(100)
print(centenar)

#variante 1

centenar = []

def tarea1(numero):
    for i in range(numero):
        centenar.append(i+1)
        print(centenar)


#EX2

lista_1 = [1 , 4, 5]
resultados = []

def suma_lista(var1):
    for a in (lista_1):
        if a <= 0:
            resultados.append(a)
        else:
            resultados.append(lista_1[a]+lista_1[a-1])
        print(resultados)


#Ex3
#Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
#Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.

indicadores = [0 , 1, 2, 3]

def ordenada(var1, var2):
    for a in indicadores:
        if indicadores[0] < indicadores[1] and indicadores[1] < indicadores[2]:
            True
        else:
            False
        
    


#Ejercicio4
#Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo orden.


duplicada = [3, 3, 4, 5, 6, 7, 7, 9]
unica = []

def elimina_duplicados(var):
    for i in duplicada:
        if duplicada[] =! i:
        unica.append(i)
        else:
            print(unica)



#Ejercicio5
# Cree un contador dentro de su función que estime la cantidad de número pares que hay dentro de su sucesion de fibonacci,
# para esto puede usar una comparación entre el número // 2 y el número / 2, solo en caso de los pares, esto debería ser verdad
# además se recomienda definir la variable count = 0 antes del loop


def contador(pares):
    count = 0
    for 
    if
    
    count += 1

    else