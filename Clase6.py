Python3

# pip install bs

from bs4 import BeautifulSoup as soup
import pandas as pd
import requests

def simple_request(link):
    headers = {'Content-Type': 'application/json'}
    r = requests.get(link, headers=headers)
    return r.content, r

web_content, request_status =  simple_request('https://soundcloud.com/uiceheidd/bandit-ft-nba-youngboy')

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

sopita = simple_parser(web_content)

#Buscara solo los tags "<a>" ya que Beatufil Soup trabajar sobre HTML, no sera lo mismo si el objeto es diferente.

links = sopita.findAll("a")
links

links = sopita.findAll("a").get("href")
links

links = [link.get("href") for link in links]

#Busqueda especifica/ Dentro del Tag <a> busco un titulo. 

links2 = sopita.findAll("a", {"title":"Popular searches"})
len(links2)

links2 = sopita.find("ul", {"class":"ListSdbr"})
links2
links2[0]


s = requests.Session()


#Busca un elemento dentro del código web de la página idetificando el tag del elemento, y se especifica una segunda indicacion tipo-elemento_a_buscar para seleccionar el elemento correcto. El campo texto corresponde a si lo buscado está como str
def sopear_elemento(url, tag, tipo, elemento_a_buscar, texto):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    if texto == True:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)}).text.strip()
    else:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elemento

data = sopear_elemento(links, "div", "class" , "downloadLinks", 1)

data = sopear_elemento(links, "meta", "genre" , "content", 1)

data = (link, "")

genero = sopita.find("dd").text

def sopear_varios_elementos(url, tag, tipo, elemento_a_buscar):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    elementos = data.findAll(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elementos


