#! /usr/bin/env python

import urllib
from bs4 import BeautifulSoup as Soup  #importa BeautifulSoup
import re    #importa regex
from HTMLParser import HTMLParser

                         
arq = open("C:/Users/Raphaela/Desktop/teste.txt")
texto = arq.readlines()
for linha in texto :

    webpage = urllib.urlopen(linha).read()

    # Acha lugar onde está a marca comercial no código html
    marca = re.compile('<font size="1"><b>Marca Comercial: <font size="2">(.*)</font>')


    # Guarda todas as marcas achadas em uma lista
    findMarca = re.findall(marca,webpage)
    
    soup3 = Soup(webpage)

    #Extrai informações da tabela que possui as culturas liberadas para uso do produto formulado, único identificador desta tabela, que a diferencia das demais no código, é scrollleft 
    tableCulturas = soup3.find("table", {"scrollleft" : "0"})

    for j in findMarca:
        j = str(j)
        j = re.sub('<[^<]+?>', '', j)
        i = 0
        cultura = ""
        for col in tableCulturas.findAll('td'):
            if i == 0:
                prvy = col.string.strip()
                if prvy != cultura: 
                    print j+";",
                    print prvy+";",
                i = i + 1
            elif i == 1:
                prvy2 = col.string.strip()
                if prvy != cultura:
                    print prvy2
                i = i + 1
                cultura = prvy
            elif i == 2:
                i = i + 1
            elif i == 3:
                i = 0
    print "\n"

arq.close()


