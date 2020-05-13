import pandas as pd

lista = ['pablo', 'andres', 'leti', 'jose']

df = pd.DataFrame(lista)

df2 = df.transpose() #transpone la base de datos

frame_data = {'name': ['James', 'Jason', 'Rogers'], 'age': [18, 20, 22], 'job': ['Assistant', 'Manager', 'Clerk']}
df = pd.DataFrame(frame_data, index = ['James', 'Jason', 'Rogers'])

df2 = df.drop(['Rogers']) #elimina la fila en que se encuentre 'Rogers' dentro de la columna indice, en esta base de datos se establecio que el index es la cokumna con los nombres, si no agregamos un index, pandas elaborará uno numerico y lo agregará como columna index
df2 = df.drop(df.index[[0, 1]]) #elimina un rango de filas

df2 = df.drop_duplicates(['name']) #bota los duplicados de la columna name
df2 = df.drop(['job'], axis=1) #elimina la columna 'job' Si el valor del eje es 1 significa que queremos eliminar columnas, si el valor del eje es 0 o se deja en blanco significa que la fila se eliminará


suma= df['age'].sum() # esto nos permite sumar los datos de la columna 'A'
valores_unicos =  df['age'].nunique() #cuenta los valores unicos
cantidad de datos = df['age'].count() # cuenta todos los valores de la columna 'A'
df[0:3] #selecciona las 3 primeras columnas




#from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
#pip install PyPDF2
import os

pags = []


def process_file(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
        pags.append(pageObj.extractText())
    print('Leido')

filename = "Sopa de Wuhan ASPO.pdf"

process_file(filename)

indice = pags[9].split('\n')

cap1 = pags[16]

citas = []

def get_citas(lista):
    for i in range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i])
            print(citas)

get_citas(pags)

citas = []


def get_citas(lista):
    for i in range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i].split('[*]')[1])
            print(citas)

get_citas(pags)


autores = []

def get_autores_citas(lista):
    for i in range(len(citas)):
        if ')' in citas[i]:
            autores.append(citas[i].split(')')[0])
            print(autores)

get_autores_citas(citas)


#Limpiar campos y realizar base de datos.

import pandas as pd

df = pd.DataFrame(autores)

#no incluye los duplicados.

autores = []

def get_autores_citas(lista):
    for i in range(len(citas)):
        if ')' in citas[i]:
            autores.append(citas[i].split(')')[0])
            print(autores)

get_autores_citas(citas)





#Obtener nombres
autores_name = []
def clean_autor(var1):
    for i in range(len(autores)):
        autores_name.append(autores[i].split('\n')[0])
        print(autores_name)
        
clean_autor(autores)

#Obtener Ciudades
autores_city = []
def clean_city(var1):
    for i in range(len(autores)):
        city = []
        city.append(autores[i].split(',')[0])
        for n in range(len(city)):
            autores_city.append(city[n].split('(')[1])
            print(autores_city)

clean_city(autores)

#Obtener Años
autores_year = []

def clean_year(var1):
    for i in range(len(autores)):
        year = []
        year.append(autores[i].split(',')[1])
        print(year)
        for n in range(len(year)):
            autores_year.append(year[n].split(',')[0])
            print(autores_year)

clean_year(autores)


dic_autores = {'name': [autores_name], 'city': [autores_city], 'year': [autores_year]}
df_autores = pd.DataFrame(dic_autores)


df2 = df_autores.transpose() #transpone la base de datos
