
# coding: utf-8

# In[3]:


import os
from pandas import DataFrame, Series, merge, read_csv


# In[ ]:


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




# In[10]:


def recuperar_data_frame_de_tuplas(caminho_arquivos):
    tuplas = recuperar_tuplas_de_bases_climaticas(caminho_arquivos)
    data_frame_clima = DataFrame(tuplas)
    data_frame_direcao_vento = read_csv('resource/Codigo_Direcao_vento.csv',  encoding='utf-8', header=0, sep=";")
    resultante = merge(data_frame_clima, data_frame_direcao_vento, how = 'left')
    return resultante


# In[8]:


def recuperar_wmos_lat_long(caminho_arquivos):
    filelist = os.listdir(caminho_arquivos)

    filepath = []

    for i in filelist:
        c = caminho_arquivos + i
        filepath.append(c)

    tuplas = []

    for nome_arquivo in filepath:
        arquivo = open(nome_arquivo,mode = 'r')
        linhas = arquivo.readlines()
        estacao = 0
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
                    inicio_tabela = True
            else:
                tupla = dict()
                colunas = linha.split(';')
                tupla['Estacao'] = colunas[0]
                tupla['Latitude'] = latitude
                tupla['Longitude'] = longitude
                tuplas.append(tupla)
                break
        
    return DataFrame(tuplas)

