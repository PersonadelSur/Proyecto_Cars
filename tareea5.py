Python3

import PyPDF2
import os
import pandas as pd 

pags = []

def leerpdf(filename):
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
    print ('Leido')


filename = "relatos de poder.pdf"
leerpdf(filename)


#obtener preguntas
lista_preguntas = []

def get_preguntas(lista):
    for i in range(len(pags)):
        if '¿' and '?' in pags[i]:
            preguntas = []
            preguntas.append(pags[i].split('¿')[1])
            for n in range(len(preguntas)):
                lista_preguntas.append(preguntas[n].split('?')[0])
                print(lista_preguntas)

get_preguntas(pags)

df_preguntas = pd.DataFrame(lista_preguntas)

df_preguntas

#Obtener Exlamaciones

lista_exclamaciones = []

def get_exclamaciones(lista):
    for i in range(len(pags)):
        if '¡' and '!' in pags[i]:
            exclamaciones = []
            exclamaciones.append(pags[i].split('¡')[1])
            for n in range(len(exclamaciones)):
                lista_exclamaciones.append(exclamaciones[n].split('!')[0])
                print(lista_exclamaciones)

get_exclamaciones(pags)

df_exclamaciones = pd.DataFrame(lista_exclamaciones)
df_exclamaciones

#N veces menciona Don Juan  // Cómo almacenar la cuenta no el texto.

donjuan_name_count = []

def get_Don_Juan_Name(lista):
    count_Juan = 0
    for i in range(len(pags)):
        if 'Don Juan' in pags[i]:
            count_Juan +=1
            print(count_Juan)

get_Don_Juan_Name(pags)

#N veces menciona Drogas

drogas = []

def get_drogas(lista):
    count = 0
    count2 = 0
    for i in range(len(pags)):
        if 'drogas' in pags[i]:
            count +=1
        else:
            count2 +=1
    print(count2, count)

get_drogas(pags)

#if not error. (como hacer)

#N veces menciona guerrero

guerrero = []

def get_guerrero(lista):
    count = 0
    for i in range(len(pags)):
        if 'guerrero' in pags[i]:
            count +=1

            print(count)

get_guerrero(pags)


