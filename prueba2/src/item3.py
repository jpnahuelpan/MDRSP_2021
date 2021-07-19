#!/usr/bin/env python
# -*- coding: utf-8 -*-
# integrantes: Juan Pablo Nahuelpán
from facebook_scraper import get_posts
from wordcloud import WordCloud
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
stopwords = set(stopwords.words('spanish', 'english')) 

ruta_src = os.path.dirname(os.path.realpath(__file__)) 
ruta_input = ruta_src.replace("src", "input/")
ruta_output = ruta_src.replace("src", "output/")
#Agregar palabras, letras, etc. a diccionario de stopwords
stopwords.update(['k','cl','s'])

cont=0

df=pd.DataFrame(columns=['Fecha_hora','Texto','Likes'])
fanpage=input("Ingrese el nombre del fanpage:")
publicaciones=int(input("Ingrese el nro. de publicaciones:"))

corpus = []

for post in get_posts(fanpage, pages=publicaciones):
    cont=cont+1
    print("-------------------------------")
    print("Fecha Hora:",post["time"])
    print("Texto Publicación:",post["text"])
    print("Cantidad de Likes:",post["likes"])
    print("-------------------------------")
    df=df.append({'Fecha_hora':post['time'],'Texto':post['text'],
               'Likes':post['likes']},ignore_index=True)

    texto = post['text']
    texto = re.sub('[^a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ]', ' ', texto)
    texto = texto.lower()
    texto = re.sub('www', '', texto)
    texto = re.sub('http', '', texto)
    texto = re.sub('https', '', texto)
    texto = texto.split()
    texto = ' '.join(texto)
    corpus.append(texto)
    
    if cont==publicaciones:
        break

#Vacía Dataframe a archivo CSV
df.to_csv(ruta_output+'tweet_data.csv')    

#Crea Word Cloud o Nube de Palabras a partir de la lista corpus
all_words = ' '.join([text for text in corpus])
wordcloud = WordCloud(stopwords=stopwords, background_color="white",width=800, height=500, random_state=21, max_font_size=110).generate(all_words)
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()