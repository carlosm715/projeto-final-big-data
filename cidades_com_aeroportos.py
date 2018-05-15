
# coding: utf-8

# In[46]:


file = open(file='cidades_com_aeroportos.txt',mode='r', encoding='utf8')


# In[47]:


cidades_por_estado = dict()

ultima_chave = ""
for linha in file:
    linha = linha.strip()
    if linha:
        linha = linha.split("–")
        print(len(linha))
        if len(linha) == 1:
            ultima_chave = linha[0]
            print('Chave:',ultima_chave)
            cidades_por_estado[ultima_chave] = []
        else:
            cidade = linha[-1]
            if cidade not in cidades_por_estado[ultima_chave]:
                cidades_por_estado[ultima_chave].append(linha[-1])
                print('Chave:',ultima_chave,' adicionando valor:',linha[-1])
            else:
                print('Chave:', ultima_chave, ' valor repetido', cidade)


# In[22]:


cidades_por_estado


# In[48]:


for estado in cidades_por_estado.items():
    print(estado[0])
    print()
    for cidade in estado[1]:
        print(cidade)
    print()

