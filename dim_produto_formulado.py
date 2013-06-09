#! /usr/bin/env python

import urllib
from bs4 import BeautifulSoup as Soup  #importa BeautifulSoup
import re    #importa regex
from HTMLParser import HTMLParser

                         
arq = open("C:/Users/Raphaela/Desktop/teste.txt")  #abri arquivo com URL de todos os produtos formulados liberados para uso no SEAB
texto = arq.readlines()
for linha in texto :

    webpage = urllib.urlopen(linha).read()

    # Acha lugar onde est� a marca comercial no c�digo html
    marca = re.compile('<font size="1"><b>Marca Comercial: <font size="2">(.*)</font>')


    # Guarda todas as marcas achadas em uma lista
    findMarca = re.findall(marca,webpage)


    #Acha lugar onde est� o nome da empresa registrante no c�digo html
    empresaBegin = webpage.find('<td colspan="2"><font size="1"><b>Empresa Registrante:')

    empresa = webpage[empresaBegin:(empresaBegin+150)]

    soup = Soup(empresa)

    # Guarda todas as empresas em uma lista
    empresaList = soup.findAll('font')

    #Acha lugar onde est� o n�mero do registro do produto formulado no c�digo html
    registroBegin = webpage.find('<td width="51%"><font size="1"><b>N�mero do Registro:')

    registro = webpage[registroBegin:(registroBegin+100)]

    soup2 = Soup(registro)

    # Guarda todos os n�meros de registro em uma lista
    registroList = soup2.findAll('font')

    #Acha lugar onde est� a informa��o de inflamabilidade do produto formulado no c�digo html
    inflaBegin = webpage.find('<td colspan="2"><font size="1"><b>Inflamabilidade:')

    inflamabilidade = webpage[inflaBegin:(inflaBegin+100)]

    soup3 = Soup(inflamabilidade)

    # Guarda todas as informa��es de inflamabilidade em uma lista
    inflaList = soup3.findAll('font')

    #Acha lugar onde est� a informa��o de tipo de formula��o do produto formulado no c�digo html
    formulaBegin = webpage.find('<td colspan="2"><font size="1"><b>Formula��o:')

    formula = webpage[formulaBegin:(formulaBegin+150)]

    soup4 = Soup(formula)

    # Guarda todas as informa��es de tipo de formula��o em uma lista
    formulaList = soup4.findAll('font')

    #Acha lugar onde est� a informa��o de classifica��o toxicol�gica do produto formulado no c�digo html
    toxicoBegin = webpage.find('<td colspan="2"><font size="1"><b>Classifica��o Toxicol�gica:')
    toxico = webpage[toxicoBegin:(toxicoBegin+150)]

    soup5 = Soup(toxico)

    # Guarda todas as informa��es da classifica��o toxicol�gica em uma lista
    toxicoList = soup5.findAll('font')

    #Acha lugar onde est� a informa��o da forma de a��o do produto formulado no c�digo html
    acaoBegin = webpage.find('<td colspan="2"><font size="1"><b>Forma de A��o:')
    acao = webpage[acaoBegin:(acaoBegin+150)]

    soup6 = Soup(acao)

    # Guarda todas as informa��es da forma de a��o em uma lista
    acaoList = soup6.findAll('font')


    # Imprimi a marca comercial
    for i in findMarca:
        i = str(i)
        i = re.sub('<[^<]+?>', '', i)
        print i+";",
        # Imprimi a empresa 
        for j in empresaList:
            j.b.replace_with("")
            j = str(j)
            j = re.sub('<[^<]+?>', '', j)
            j = j.strip()
            print j+";",
            # Imprimi n�mero de registro
            for l in registroList:
                l.b.replace_with("")
                l = str(l)
                l = re.sub('<[^<]+?>', '', l)
                l = l.strip()
                print l+";",
                # Imprimi inflamabilidade
                for m in inflaList:
                    m.b.replace_with("")
                    m = str(m)
                    m = re.sub('<[^<]+?>', '', m)
                    m = m.strip()
                    print m+";",
                    # Imprimi formula��o
                    for n in formulaList:
                        n.b.replace_with("")
                        n = str(n)
                        n = re.sub('<[^<]+?>', '', n)
                        n = n.strip()
                        print n+";",
                        # Imprimi classifica��o toxicol�gica
                        for o in toxicoList:
                            o.b.replace_with("")
                            o = str(o)
                            o = re.sub('<[^<]+?>', '', o)
                            o = o.strip()
                            print o+";",
                            # Imprimi forma de a��o
                            for p in acaoList:
                                p.b.replace_with("")
                                p = str(p)
                                p = re.sub('<[^<]+?>', '', p)
                                p = p.strip()
                                print p

arq.close()
