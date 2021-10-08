#!/usr/bin/env python
# coding: utf-8

# In[18]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 


# In[26]:


navegador = webdriver.Chrome('chromedriver.exe')
navegador.get('https://www.google.com.br/')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Dólar') #COTAÇÃO DÓLAR PESQUISAR
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER) #ENTER TECLADO

cotacao_dolar = navegador.find_element_by_xpath ('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

navegador.get('https://www.google.com.br/')
navegador.find_element_by_xpath ('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação do Euro') #COTAÇÃO EURO PESQUISAR
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') 
print(cotacao_euro)

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',' , ".")
print(cotacao_ouro)


# In[33]:


#PASSO 4 IMPORTAR A BASE DE DADOS
get_ipython().system('pip install pandas')


# In[40]:


import pandas as pd

tabela = pd.read_excel ('Produtos.xlsx')
display (tabela)


# In[64]:


#ATUALIZAR A COTAÇÃO, O PREÇO DE VENDA E PREÇO DE COMPRA.
#tabela.loc[linha, coluna]

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
           
tabela=['Preço de Compra'] = tabela ['Preço Original'] * tabela ['Cotação']
tabela=['Preço de Venda'] = tabela ['Preço de Compra'] * tabela ['Margem']
           
tabela=['Preço de Venda'] = tabela ['Preço de Venda'].map('R$(:.2f)'.format)
           
           
           


# In[65]:


tabela.to_excel('Produtos.excel', index=false)
navegador.quit()


# In[ ]:




