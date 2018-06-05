
# coding: utf-8

# In[45]:


import os
from pandas import DataFrame, Series


# In[46]:


def recuperar_tuplas_de_bases_climaticas(caminho_arquivos):
    filelist = os.listdir(caminho_arquivos)

    filepath = []

    for i in filelist:
        c = caminho_arquivos + i
        filepath.append(c)

    tuplas = []

    for nome_arquivo in filepath:
        arquivo = open(nome_arquivo,mode = 'r')
        linhas = arquivo.readlines()
        latitude = 0
        longitude = 0
        inicio_tabela = False

        headers = []
        for linha in linhas:
            if not inicio_tabela:
                if linha.find('Latitude') == 0:
                    latitude = float(linha.split(':')[1].strip())
                elif linha.find('Longitude') == 0:
                    longitude = float(linha.split(':')[1].strip())
                elif linha.find('Estacao;Data;Hora;TempBulboSeco;TempBulboUmido;UmidadeRelativa;PressaoAtmEstacao;DirecaoVento;VelocidadeVentoNebulosidade;') ==0:
                    headers = linha.split(';')
                    inicio_tabela = True
            else:
                tupla = dict()
                colunas = linha.split(';')
                for header, coluna in zip(headers ,colunas):
                    tupla[header] = coluna
                tupla['Latitude'] = latitude
                tupla['Longitude'] = longitude
                tuplas.append(tupla)
        
    return tuplas




# In[47]:


def recuperar_data_frame_de_tuplas(caminho_arquivos):
    tuplas = recuperar_tuplas_de_bases_climaticas(caminho_arquivos)
    data_frame = DataFrame(tuplas)
    return data_frame


# In[48]:


tuples = recuperar_data_frame_de_tuplas('resource/climahistorico/')


# In[49]:


tuples

