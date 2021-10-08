#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[16]:


#IMPORTAR A BASE DE DADOS
import pandas as pd
tabela = pd.read_csv("telecom_users.csv") # VARIÁVEL PARA LER O ARQUIVO DE DADOS E ARQUIVAR NA VARIÁVEL
##print (tabela.info)


# In[ ]:





# In[82]:


#passo 2: visualizar a base de dado
tabela = pd.read_csv("telecom_users.csv") # VARIÁVEL PARA LER O ARQUIVO DE DADOS E ARQUIVAR NA VARIÁVEL
tabela = tabela.drop ("Unnamed: 0", axis=1 )


# In[ ]:


#--ENTENDER AS INFORMAÇÕES DISPONIVEIS

#--DESCOBRIR OS ERROS DA BASE DE DADOS


# In[79]:


#PASSO 3: TRATAMENTO DE DADOS

#--VALORES QUE ESTÃO RECONHECIDOS DE FORMA ERRADA 

tabela ["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],  errors="coerce")
#--VALORES VAZIOS
tabela = tabela.dropna (how="all", axis= 1)
tabela = tabela.drop ("IDCliente", axis =1)
#APAGAR LINHAS DE VALORES VAZIOS 
tabela = tabela.dropna (how="any", axis= 0)




# In[50]:


#PASSO 4: ANALISE INICIAL

print (tabela["Churn"].value_counts())
print (tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

tabela2 = tabela["Churn"]


# In[57]:



get_ipython().system('pip install plotly')


# In[59]:


import plotly.express as px


# In[80]:


#PASSO 5: ANALISE COMPLETA
#COMPARAR CADA COLUNA DA TABELA COM A COLUNA DE CANCELAMENTO

#ETAPA 1: CRIAR O GRAFICO
#PARA MUDAR A COR DO GRÁFICO:  color_discrete_sequence=["blue","orange",]
for coluna in tabela.columns: 
    grafico = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["blue","orange",])
    #ETAPA 2: EXIBIR O GRÁFICO E COLUNA
    grafico.show()


# ##CLIENTES COM CONTRATO MENSAL TEM MUITO MAIS CHANCES DE CANCELAR.
# ##CASADOS TEM MAIS PROBABILIDADES DE REALIZAR CANCELAMENTOS.
# 

# 
