

# pip install bs
Python3
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests

#Page 01

def simple_request(link):
    headers = {'Content-Type': 'text/css'}
    r = requests.get(link, headers=headers)
    return r.content, r

web_content, request_status =  simple_request('https://www.pauta.cl/nacional/el-perfil-de-los-fallecidos-por-covid-19-en-chile-actualizado')

type(web_content)

#test modificación del tipo de objeto de Bytes a Str

def simple_parser(contenido_web):
    page_soup = soup(str(contenido_web), "html.parser")
    print(type(page_soup))
    # print(page_soup)

simple_parser(web_content)

#Modificación del tipo de objeto de Bytes a Str

def simple_parser(contenido_web):
    page_soup = soup(str(contenido_web), "html.parser")
    return page_soup

Pauta = simple_parser(web_content)

#Buscara solo los tags "<a>" ya que Beatufil Soup trabajar sobre HTML, no sera lo mismo si el objeto es diferente.

info = Pauta.findAll("li").get("strong")

info2 = Pauta.findAll("ul", {"li"})

test1 = Pauta.findAll("div", {"class":"infogram-embed"})

tablas_datos1 = Pauta.findAll("div", {"style":"border: 5px solid #00c7b1; padding: 10px;"})
tablas_datos2 = Pauta.findAll("div", {"style":"border: 5px solid #003865; padding: 10px;"})

def object_convert(tablas):
    strings = soup(str(tablas), "html.parser")
    return strings

seleccion = tablas_datos1 + tablas_datos2

detalle = tablas_datos1.findAll("Strong" + "li")

string_tabla1 = object_convert(tablas_datos1)
tabla1 = string_tabla1.findAll("li")

string_tabla2 = object_convert(tablas_datos2)
tabla2 = string_tabla2.findAll("li")

titulos = []

def get_titulos(tabla):
    for i in range(len(tabla1)):
        tabla1[i].text
        print(tabla)


df = pd.DataFrame(tabla1 and tabla2)

def convert_to_list(tabla):
    lista_datos = str(tabla)
    return lista_datos
        

type(string_tabla2)
type(tablas_datos1)
type(Pauta)

#Page 02

def simple_request(link):
    headers = {'Content-Type': 'text/css'}  #codificación charset=utf-8 ?
    r = requests.get(link, headers=headers)
    return r.content, r
    print('Importada')

web_content, request_status =  simple_request('https://www.salazarisraelusados.cl/web/autos-usados')

type(web_content)

def simple_parser(contenido_web):
    page_soup = soup(str(contenido_web), "html.parser")
    return page_soup

Salazar = simple_parser(web_content)
type(Salazar)

#All Cars
Cars = Salazar.findAll("div", {"id":"w0"})

type(Cars)

def object_convert(tablas):
    strings = soup(str(tablas), "html.parser")
    return strings


Cars_String = object_convert(Cars)
type(Cars_String)

#All Cars Detail
car_list = Cars_String.findAll("div", {"class":"card-body"})
type(car_list)
car_list_string = object_convert(car_list)
type(car_list_string)

## Convert To List
car_list_list = []

def str_convert(parse):
    for i in car_list_string:
        car_list_list.append(str(i))
    return car_list_list

str_convert(car_list)

type(car_list_list)

#Get All (2 Elementos + 1 elemento + 3 elementos)

car_all = car_list_string.findAll('strong') + car_list_string.findAll('h4', {'class':'card-title card-price'}) + car_list_string.findAll('li')

#convertir a lista
car_all_list = []
def str_convert(parse):
    for i in car_all:
        car_all_list.append(str(i))
    return car_all_list

str_convert(car_all)
type(car_all_list)

#convertir lista a data frame
df_car = pd.DataFrame(car_all_list)
type(df_car)

#Lista 

brands = []
models = []
def get_brands(df):
    for i in range(len(df_car)):
        if i % 2==0:
            brands.append(df_car.iloc[i])
        else:
            models.append(df_car.iloc[i])

get_brands(df_car)

#convertir data frame a str
df_car_string = str(df_car)
import re
clean = re.sub('<strong>|</strong>|<li>|</li>|<h4 class="card-title card-price">\n','', df_car_string)

clean = re.sub('<strong>|</strong>|<li>|</li>|<h4 class="card-title card-price">\n','', df_car.iloc[1])

#convertir a lista
clean_list = []
def str_convert(parse):
    for i in clean:
        clean_list.append(str(i))
    return clean_list

str_convert(clean)
type(clean_list)
#convertir a data frame
df_clean = pd.DataFrame(clean)

##### Get Brand And Model
brand_n_model = car_list_string.findAll("strong")
type(brand_n_model)

# Conver to List
brand_n_model_list = []
def str_convert(parse):
    for i in brand_n_model:
        brand_n_model_list.append(str(i))
    return brand_n_model_list

str_convert(brand_n_model)

df_brand_n_model = pd.DataFrame(brand_n_model_list)

brands = []
models = []
def get_brands_model(data):
    for i in range(len(df_brand_n_model)):
        if i % 2==0:
            brands.append(df_brand_n_model.iloc[i])
        else:
            models.append(df_brand_n_model.iloc[i])

get_brands_model(df_brand_n_model)




car_diccionario = brands + models

#Get Price 
car_price = car_list_string.findAll("h4", {'class':'card-title card-price'})

#Get Details

car_details = car_list_string.findAll("ul")
# or
car_details_short = car_list_string.findAll("li")

year = []
km = []
transmision = []

def get_details(text):
    count = 0
    for i in range(len(car_details_short)):
        if count == 0:
            year.append(car_details_short[i])
            count +=1
        elif count == 1:
            km.append(car_details_short[i])
            count +=1
        elif count == 2:
            transmision.append(car_details_short[i])
            count -=2
        

#diccionario
cars_diccionario = {'Marcas':[brands], "Modelos":[models], "Precios":[car_list_string.findAll("h4", {'class':'card-title card-price'})], "Year":[year], "KM":[km], "Trasmision":[transmision]}

df_diccionario = pd.DataFrame(cars_diccionario)

#Data Frames
df = pd.DataFrame(brand_n_model_list)

df_string = str(df)

#Limpiar texto

import re
from decorator import append

def limpiar(string):
    clean = re.sub('<strong>|</strong>','', df_string)
    clean_list = [clean]
    clean_list[0].split('\n')

limpiar(df_string)

clean = re.sub('<strong>|</strong>','', df_string)

clean_list = [clean]

lista_final = clean_list[0].split('\n')

df_clean = pd.DataFrame(lista_final)

brands = []
models = []

def separador(dataframe):
    for i in range(len(df_clean)):
        if df_clean.iloc[i] % 2 == 0:
            brands.append(df_clean.iloc[i])
        else:
            models.append(df.clean.iloc[i])

separador(df_clean)

car_detail_brand = car_list_string.findAll("h4", {"class":"card-title"})
type(car_detail_brand)

#exportar excel

from pandas import ExcelWriter as ew

def generar_DF_Excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx' 
    writer = ew(nombre_final)
    df.to_excel(writer,'Cars')
    writer.save()
    print('Ok')


generar_DF_Excel(df_diccionario, 'cars')

#Page 03

