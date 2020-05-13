Python3
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests

'https://www.salazarisraelusados.cl/web/autos-usados?page=2'

def simple_request(link):
    headers = {'Content-Type': 'text/css'}  #codificación charset=utf-8 ?
    r = requests.get(link, headers=headers)
    return r.content, r

web_content, request_status =  simple_request('https://www.salazarisraelusados.cl/web/autos-usados')

pages = [20]

def get_all_pages(links):
    for range(len(pages):
        url = 'https://www.salazarisraelusados.cl/web/autos-usados?page='.(pages)
   

PAGES = ['brad-brach','oliver-drake',...]
for i in range(len(PLAYER_NAME)):
    url = 'http://espn.go.com/mlb/player/_/id/{}/{}'.format(PLAYER_ID[i], PLAYER_NAME[i])


#como hacer un loop de varias urls.simple_request
Ejemplos:

url = 'http://www.hkjc.com/chinese/racing/selecthorsebychar.asp?ordertype=2'
url1 = 'http://www.hkjc.com/chinese/racing/selecthorsebychar.asp?ordertype=3'
url2 = 'http://www.hkjc.com/chinese/racing/selecthorsebychar.asp?ordertype=4'

r  = requests.get(url)
r1  = requests.get(url1)
r2  = requests.get(url2)


