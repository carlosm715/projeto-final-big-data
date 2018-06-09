
# coding: utf-8

# In[5]:


#pip install diblogeo


# In[1]:


from diblogeo import Geo


# In[4]:


def calcular_distancia_geoespacial(lat_long_ponto_1, lat_long_ponto_2):
    return Geo(lat_long_ponto_1).distance(lat_long_ponto_2)


# In[5]:


calcular_distancia_geoespacial((1,2),(3,4))

