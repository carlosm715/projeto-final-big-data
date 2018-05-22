
# coding: utf-8

# In[5]:


#pip install diblogeo


# In[3]:


from diblogeo import Geo


# In[5]:


def calcular_distancia_geoespacial(lat_long_ponto_1, lat_long_ponto_2):
    return Geo(lat_long_ponto_1).distance(lat_long_ponto_2)


# In[6]:


distance = calcular_distancia_geoespacial((2.84, -60.68), (-15.78, -47.92))


# In[18]:


distance

