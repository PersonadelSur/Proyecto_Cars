import pandas as pd
from pandas import ExcelWriter

import random

lista = pd.ExcelFile("random_muestra.xlsx")
lista.sheet_names
lista = lista.parse("Hoja2")

print(lista)
print(lista.head())
print(lista.columns)

lista.loc[1, "List Id"]
lista.loc[5, "List Id"]

autos = []
def nueva_lista(lista):
    for i in range(len(lista)):
        if lista.loc[i, 'List Id'] not in autos:
            autos.append(lista.loc[i, 'List Id'])
        else:
            pass
    return autos

autos = nueva_lista(lista)

def eleccion(autos):
    random_autos = []
    for i in range(40):
        random_autos.append(random.choice(autos))
    return random_autos

random_autos = eleccion(autos)

df = pd.DataFrame(random_autos)


def generar_df_excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx'
    writer = ExcelWriter(nombre_final)
    df.to_excel(writer, 'Muestras')
    writer.save()
    print('OK')

def generar_excel(dfautos, nombre):
    nombre_final = nombre + '.xlsx'
    writer = ExcelWriter(nombre_final)
    dfautos.to_excel(writer, 'muestras')
    writer.save()
    print('ok')


generar_df_excel(df, 'muestras')