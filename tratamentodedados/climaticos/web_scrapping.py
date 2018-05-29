
# coding: utf-8

# In[17]:


#pip install beautifulsoup4
from bs4 import BeautifulSoup
from pandas import DataFrame


# In[18]:


def recuperar_tuplas_de_table(arquivo_html, caminho_para_trs_da_table):
    
    soup = BeautifulSoup(open(arquivo_html, mode='r', encoding='UTF-8'), 'html.parser')

    tuplas = []

    headers = []
    
    for indice,linha_da_tabela in enumerate(soup.select(caminho_para_trs_da_table)):
        
        if indice == 0:
            header_columns = linha_da_tabela.findAll('th')
            for header_column in header_columns:
                headers.append(header_column.get_text().strip())
            
        colunas = linha_da_tabela.findAll('td')

        if len(colunas) > 0:

            tupla = dict()
            
            for header, coluna in zip(headers, colunas):
            
                tupla[header] = coluna.get_text().strip()

            tuplas.append(tupla)

            
    return tuplas


# In[15]:


def recuperar_data_frame_de_tuplas(arquivo_html, caminho_para_trs_da_table):
    return DataFrame.from_dict(recuperar_tuplas_de_table(arquivo_html, caminho_para_trs_da_table))

