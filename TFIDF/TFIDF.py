#!/usr/bin/env python
# coding: utf-8

# # Term Frecuency x Inverse Document Frecuency (TF IDF)
# 

# In[1]:


import io
import re
from functools import reduce
from collections import Counter
from numpy import log
from pandas import DataFrame


# In[2]:


with io.open('stop-words-spanish.txt', mode='r', encoding='utf-8') as f:
    stopwords = f.read().splitlines()
stopwords


# In[3]:


with io.open('Data/AMLO_28042013.txt', mode='r', encoding='utf-8') as f:
    boletin = f.read().splitlines()
boletin


# ### Obtener palabras
# 
# Obtenemos las palabras en minúsculas
# 

# In[4]:


documentos = [re.findall('[a-zA-zñáéíóúüÁÉÍÓÚÜÑ]+', parrafo.lower()) for (index, parrafo) in enumerate(boletin)]
documentos


# 

# In[5]:


documentos = [[palabra for palabra in documento if not (palabra in stopwords)] for documento in documentos]
total_palabras = len(documentos)
documentos


# Contar las palabras por documento y el total de palabras

# In[6]:


cuenta_por_documento = [Counter(parrafo) for parrafo in documentos]
cuenta_total_palabras = reduce((lambda x, y: x + y), cuenta_por_documento)
palabras = [palabra for (palabra, cuenta) in cuenta_total_palabras.items()]
cuenta_por_documento


# Definimos función para suavizar la cuenta de palabras.

# In[7]:


def bm25(contador, k=25):
    return {
        key: ((cuenta + 1)*k)/(cuenta+k) for (key, cuenta) in contador.items()
    }


# Calculamos tf para cada uno de los documentos 

# In[8]:


tfs = [bm25(c_doc) for c_doc in cuenta_por_documento]
tfs


# Definimos la función IDF
# 
# $$$$

# In[9]:


def idf(palabra, documentos):
    return log(
        len(documentos) / 
        (1+reduce(lambda cuenta, documento : cuenta + (1 if (palabra in documento) else 0), documentos, 0))
    )
# documento for documento in documentos if (palabra in documento)
# ]))


# Calculamos el idf de todas las palabras

# In[10]:


idfs = {
    palabra: idf(palabra, documentos) for palabra in palabras
}
idfs


# Calculamos tfxIDF

# In[11]:


tfidfs = [
    {
        palabra: idfs[palabra]*tf
        for (palabra, tf) in tf_n.items()
    }
    for tf_n in tfs
]
tfidfs


# In[12]:


def obtener_keywords(num_keywords=5):
    keywords = []
    for tfidf_n in tfidfs:
        keywords_n = sorted(tfidf_n.items() ,  key=lambda x: x[1], reverse=True)[:num_keywords]
#         print([keyword[0] for keyword in keywords_n])
        keywords.append([keyword[0] for keyword in keywords_n])
    return keywords


# In[13]:


keywords = obtener_keywords(6)
keywords


# In[14]:


keywords_dict = {'Párrafo {0}'.format(n+1):kw_n for (n, kw_n) in enumerate(keywords)}
df = DataFrame(keywords_dict).transpose()
df


# In[ ]:





# In[ ]:




