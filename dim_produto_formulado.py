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


    #Acha lugar onde está o nome da empresa registrante no código html
    empresaBegin = webpage.find('<td colspan="2"><font size="1"><b>Empresa Registrante:')

    empresa = webpage[empresaBegin:(empresaBegin+150)]

    soup = Soup(empresa)

    # Guarda todas as empresas em uma lista
    empresaList = soup.findAll('font')

    #Acha lugar onde está o número do registro do produto formulado no código html
    registroBegin = webpage.find('<td width="51%"><font size="1"><b>Número do Registro:')

    registro = webpage[registroBegin:(registroBegin+100)]

    soup2 = Soup(registro)

    # Guarda todos os números de registro em uma lista
    registroList = soup2.findAll('font')

    #Acha lugar onde está a informação de inflamabilidade do produto formulado no código html
    inflaBegin = webpage.find('<td colspan="2"><font size="1"><b>Inflamabilidade:')

    inflamabilidade = webpage[inflaBegin:(inflaBegin+100)]

    soup3 = Soup(inflamabilidade)

    # Guarda todas as informações de inflamabilidade em uma lista
    inflaList = soup3.findAll('font')

    #Acha lugar onde está a informação de tipo de formulação do produto formulado no código html
    formulaBegin = webpage.find('<td colspan="2"><font size="1"><b>Formulação:')

    formula = webpage[formulaBegin:(formulaBegin+150)]

    soup4 = Soup(formula)

    # Guarda todas as informações de tipo de formulação em uma lista
    formulaList = soup4.findAll('font')

    #Acha lugar onde está a informação de classificação toxicológica do produto formulado no código html
    toxicoBegin = webpage.find('<td colspan="2"><font size="1"><b>Classificação Toxicológica:')
    toxico = webpage[toxicoBegin:(toxicoBegin+150)]

    soup5 = Soup(toxico)

    # Guarda todas as informações da classificação toxicológica em uma lista
    toxicoList = soup5.findAll('font')

    #Acha lugar onde está a informação da forma de ação do produto formulado no código html
    acaoBegin = webpage.find('<td colspan="2"><font size="1"><b>Forma de Ação:')
    acao = webpage[acaoBegin:(acaoBegin+150)]

    soup6 = Soup(acao)

    # Guarda todas as informações da forma de ação em uma lista
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
            # Imprimi número de registro
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
                    # Imprimi formulação
                    for n in formulaList:
                        n.b.replace_with("")
                        n = str(n)
                        n = re.sub('<[^<]+?>', '', n)
                        n = n.strip()
                        print n+";",
                        # Imprimi classificação toxicológica
                        for o in toxicoList:
                            o.b.replace_with("")
                            o = str(o)
                            o = re.sub('<[^<]+?>', '', o)
                            o = o.strip()
                            print o+";",
                            # Imprimi forma de ação
                            for p in acaoList:
                                p.b.replace_with("")
                                p = str(p)
                                p = re.sub('<[^<]+?>', '', p)
                                p = p.strip()
                                print p

arq.close()
