#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install scikit-learn')


# #ENTENDIMENTO DO DESAFIO
# #EXTRAÇÃO/OBTENÇÃO DE DADOS
# #TRATAMENTO DE DADOS
# #ANÁLISE EXPLORATÓRIA
# #MODELAGEM + ALGORITMOS
# #INTERPRETAÇÃO DE RESULTADOS
# 
# 

# In[8]:


import pandas


# In[9]:


tabela = pandas.read_csv('advertising.csv') # LER A TABELA UPADA 
display(tabela)


# In[17]:


import matplotlib.pyplot as pyplot
import seaborn as seaborn #SEABORN SERVE PARA DAR MAIS BELEZA AO MATPLOTLIB QUE É INTEGRADO AO PYT.


# In[12]:


seaborn.pairplot(tabela) # ANÁLISE EXPLORATÓRIA 
pyplot.show() #MOSTRAR TABELA COM BIBLIOTECA DO PYPLOT


# In[ ]:


seaborn.heatmap(tabela.corr(),annot= True, cmap= 'Wistia') #CMAP DIZ A PALETA DE CORES, ANNOT DIZ SE VAI APARECER OS NUMEROS NO CENTRO DE CADA QUADRADO
#TABELA.CORR INDICA A CORRELAÇÃO DE CADA INFORMAÇÃO, HEATMAP, É UM MAPA DE CALOR.
pyplot.show()


# In[ ]:





# In[19]:


from sklearn.model_selection import train_test_split
x= tabela.drop('Vendas', axis=1) # Ira retirar da tabela a 'Vendas', e todo o resto irá compor o valor X
y = tabela['Vendas']


# PARA CRIAR UM MODELO DE INTELIGENCIA ARTIFICAL, PRECISA TREINAR O MODELO E TESTAR O MODELO.

# In[33]:


x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.4, random_state=1) 
#VARIÁVEIS QUE RECEBERÃO O VALOR DE TESTE E TREINO X e Y.
#COMANDO DA BIBLIOTECA PARA TREINO E TESTE, TEST_SIZE INDICA A PORCENTAGEM DOS DADOS QUE SERVIRÃO DE TESTE E RANDOM_STATE INDICA


# In[34]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics 
import numpy as numpy


# In[36]:


##TREINO DAS INTELIGENCIAS ARTIFICIAIS
lin_reg = LinearRegression() #INTELIGENCIA ARTIFICAL REGRESSÃO LINEAR
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor() #INTELIGENCIA ARTIFICIAL REGRESSÃO ALEATÓRIA 
rf_reg.fit(x_train, y_train)


# In[39]:


##TESTE DAS INTELIGENCIAS ARTIFICIAIS
test_pred_lin = lin_reg.predict(x_test) #VARIAVEL DE TESTE LINEAR 
test_pred_rf = rf_reg.predict(x_test) #VARIAVEL DE TESTE RANDOM FOREST

r2_lin = metrics.r2_score(y_test, test_pred_lin) # VARIAVEL PARA INFORMAR A QUALIDADE DA INTELIGENCIA LINEAR
rmse_lin = numpy.sqrt(metrics.mean_squared_error(y_test, test_pred_lin)) 
print(f'R² da Regressão Linear:{r2_lin}')
print(f'RSME da Regressão Linear:{rmse_lin}')

r2_rf = metrics.r2_score(y_test, test_pred_rf) # VARIAVEL PARA INFORMAR A QUALIDADE DA INTELIGENCIA RANDOM FOREST
rmse_rf = numpy.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))
print(f'R² da Random Forest:{r2_rf}')
print(f'RSME da Random Forest:{rmse_rf}')


# In[42]:


tabela_resultado = pandas.DataFrame()
#TABELA.INDEX = x_test 
tabela_resultado['Teste y'] = y_test
tabela_resultado['Previsão RF y'] = test_pred_rf
tabela_resultado['Previsão lin y'] = test_pred_lin

tabela_resultado = tabela_resultado.reset_index(drop=True)
fig = pyplot.figure(figsize=(10,5))
seaborn.lineplot(data=tabela_resultado)
pyplot.show()
display(tabela_resultado)


# In[46]:


importancia_features = pandas.DataFrame(rf_reg.feature_importances_, x_train.columns) # CRIAR quadro com variavel rf como correlação com a coluna de treino
pyplot.figure(figsize=(5,5)) # TAMANHO  DA IMAGEM 
seaborn.barplot(x=importancia_features.index, y=importancia_features[0])  #
pyplot.show()


# In[ ]:




