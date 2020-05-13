import pandas as pd

lista = ['andres', 'leti', 'pablo', 'jose']

df = pd.Dataframe(lista)

import PyPDF2

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
    for i range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i]):
            print(len(citas)

get_citas(pags)

cita1 = citas[0].split('[*]')[1]

def get_citas(lista):
    for i range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i].split('[*]')[1])
    print('Listas Tomadas')

autores = []

def get_autores(lista):
    for i in range(len(pags)):
        if '[*]' in pags[1]:
            cita = pags[i].split('[*]')[1]
            autor = cita.split('\n')[0]
            autores.append(autor)
    print('Autores Tomados')

get_autores(pags)

