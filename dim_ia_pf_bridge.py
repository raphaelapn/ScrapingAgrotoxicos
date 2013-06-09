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

    #Extrai informações da tabela que possui os ingredientes ativos aplicados no produto formulado, o identificador desta tabela, que a diferencia das demais no código, é o nome "table_ingredientes" 
    tableIngredientes = soup3.find("table", {"name": "table_ingredientes"})

    for j in findMarca:
        j = str(j)
        j = re.sub('<[^<]+?>', '', j)
        i = 0
        for col in tableIngredientes.findAll('td'):
            l = str(col)
            l = re.sub('<[^<]+?>', '', l)
            l = l.strip()
            if i == 0:
                print j+";"+l+";",
                i = i + 1
            elif i == 1:
                print l
                i = 0
    print "\n"


arq.close()


