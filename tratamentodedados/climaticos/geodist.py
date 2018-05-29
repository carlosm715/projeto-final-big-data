
# coding: utf-8

# In[5]:


#pip install diblogeo


# In[1]:


from diblogeo import Geo


# In[27]:


def calcular_distancia_geoespacial(lat_long_ponto_1, lat_long_ponto_2):
    if type(lat_long_ponto_1) != "tuple" or type(lat_long_ponto_2) != "tuple":
        raise Exception("Varíaveis precisam ser do tipo tupla")
    return Geo(lat_long_ponto_1).distance(lat_long_ponto_2)

