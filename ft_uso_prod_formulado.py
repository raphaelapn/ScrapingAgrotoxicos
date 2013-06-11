#! /usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
from bs4 import BeautifulSoup as Soup
import re #regex
from HTMLParser import HTMLParser


# Grab everything that lies between the title tags using a REGEX
marca = re.compile('<font size="1"><b>Marca Comercial: <font size="2">(.*)</font>')

#soup = Soup(webpage)
#registrante = soup.findAll(re.compile('<td colspan="2"><font size="1"><b>Empresa Registrante:.*?'))



                         
arq = open("C:/Users/Raphaela/Desktop/teste.txt")
texto = arq.readlines()
for linha in texto :

    webpage = urllib.urlopen(linha).read()


    # Store all of the titles and links found in 2 lists
    findMarca = re.findall(marca,webpage)

    #achar n�mero do registro
    registroBegin = webpage.find('<font color="blue">')

    article2 = webpage[registroBegin:(registroBegin+100)]

    soup2 = Soup(article2)

    registroList = soup2.findAll('font')

    # Print out the results to screen
    for i in findMarca:
        i = str(i)
        i = re.sub('<[^<]+?>', '', i)
        print i+";",
        for j in registroList:
            j = str(j)
            j = re.sub('<[^<]+?>', '', j)
            j = j.strip()
            if(j == "Liberado com Restrição de Uso"):
                print j
    print "\n"


arq.close()
