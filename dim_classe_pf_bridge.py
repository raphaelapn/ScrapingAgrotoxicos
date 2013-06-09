#! /usr/bin/env python

import urllib
from bs4 import BeautifulSoup as Soup  #importa BeautifulSoup
import re    #importa regex
from HTMLParser import HTMLParser


arq = open("C:/Users/Raphaela/Desktop/teste.txt")  #abri arquivo com URL de todos os produtos formulados liberados para uso no SEAB
texto = arq.readlines()
for linha in texto :

    webpage = urllib.urlopen(linha).read()

    # Acha lugar onde está a marca comercial no código html
    marca = re.compile('<font size="1"><b>Marca Comercial: <font size="2">(.*)</font>')


    # Guarda todas as marcas achadas em uma lista
    findMarca = re.findall(marca,webpage)


    #Acha lugar onde está a classe do produto formulado no código html
    classeBegin = webpage.find('<td width="49%"><font size="1"><b>Classe:')

    classe = webpage[classeBegin:(classeBegin+170)]

    soup2 = Soup(classe)

    classeList = soup2.findAll('font')

    # Imprimi a marca comercial
    for i in findMarca:
        i = str(i)
        i = re.sub('<[^<]+?>', '', i)
        print i+";",
        # Imprimi a classe
        for j in classeList:
            j.b.replace_with("")
            j = str(j)
            j = re.sub('<[^<]+?>', '', j)
            j = j.strip()
            print j

arq.close()


