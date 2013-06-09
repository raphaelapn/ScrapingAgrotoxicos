import urllib
from bs4 import BeautifulSoup
import re

html = "http://celepar07web.pr.gov.br/agrotoxicos/resultadoPesquisa.asp"

webpage = urllib.urlopen(html).read()

soup = BeautifulSoup(''.join(webpage))

f = open("C:/Users/Raphaela/Desktop/teste.txt", "w")

# escreve URLs em um arquivo txt
try:
    for a in soup.findAll('a',href=True):
        if a['href'] != "javascript: restricoes();":
            f.writelines("http://celepar07web.pr.gov.br/agrotoxicos/"+a['href']+"\n")
finally:
    f.close()

