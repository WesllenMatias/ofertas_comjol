from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import os

caminho = os.getcwd()
html = urlopen("https://www.comjol.com.br/busca/?fq=H:146&O=OrderByBestDiscountDESC")
bs = BeautifulSoup(html, 'html.parser')

l_titulo = bs.find_all('b',{'class':'product-name'})
l_mpreco = bs.find_all('span',{'class':'best-price'})
l_oldpreco = bs.find_all('span',{'class':'old-price'})

titulo, preco, old_preco = [],[],[]

for t in l_titulo:
    titulo.append(t.text)

for mp in l_mpreco:
    preco.append(mp.text)

for op in l_oldpreco:
    old_preco.append(op.text)

df = pd.DataFrame({'Produto':titulo,'Preço':preco,'Preço Antigo':old_preco})

df.head()

df.to_excel(f'{caminho}/ofertas_comjol.xlsx')
