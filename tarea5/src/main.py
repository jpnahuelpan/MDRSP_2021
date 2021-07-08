#!/usr/bin/env python
# -*- coding: utf-8 -*-
# integrantes: J.P. Nahuelpán, Pelegrin Huichalaf
import os
import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('tkAgg')# para linux.
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
import json
from keys import keys # debe crear su propio keys.py con sus keys y tokens
# keys = [consumer_key, consumer_key_secret, access_token, access_token_secret]

ruta_src = os.path.dirname(os.path.realpath(__file__)) 
ruta_input = ruta_src.replace("src", "input/")
ruta_output = ruta_src.replace("src", "output/")


auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Definiendo la palabra de búsqueda y el número de tweets
query = str(input("Ingrese palabra clave: "))
query = TextBlob(query)
max_tweets = int(input("Numero de tweets: "))
searched_tweets = [status for status in tweepy.Cursor(
                                                      api.search,
                                                      q=query).items(
                                                      max_tweets)]

# Informe de Analisis de Sentimiento
# Encontrando polaridad (pos neg and neutral)
obj = 0
sub = 0
for tweet in searched_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment[1] > 0.5:
        sub = sub + 1
    elif analysis.sentiment[1] <= 0.5:
        obj = obj + 1

print("Total subjetivo = ", sub)
print("Total objetivo = ", obj)

# Graficando Circular Sentimiento
labels = 'obj', 'sub'
sizes = [obj, sub]
colors = ['blue', 'red']
explode = (0.1, 0)  # explode 1st slice
plt.pie(sizes, explode=explode,
        labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

# Dataframe de Tweets
# Limpiando tweets y convirtiendo a Dataframe
my_list_of_dicts = []
for each_json_tweet in searched_tweets:
    my_list_of_dicts.append(each_json_tweet._json)
with open(ruta_input+'tweet_json_Data.txt', 'w') as file:
    file.write(json.dumps(my_list_of_dicts, indent=4))

my_demo_list = []
with open(ruta_input+'tweet_json_Data.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        tweet_id = each_dictionary['id']
        text = each_dictionary['text']
        favorite_count = each_dictionary['favorite_count']
        retweet_count = each_dictionary['retweet_count']
        created_at = each_dictionary['created_at']
        my_demo_list.append({'tweet_id': str(tweet_id),
                             'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at})
        tweet_dataset = pd.DataFrame(my_demo_list,
                                     columns=['tweet_id', 'text',
                                              'favorite_count',
                                              'retweet_count',
                                              'created_at'])

# Guardando el dataset de tweets en un archivo CSV
tweet_dataset.to_csv(ruta_output+'tweet_data.csv')

# tweet_dataset.shape

# tweet_dataset.head()

# Limpiando datos


def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt


tweet_dataset['text'] = np.vectorize(
                                     remove_pattern)(
                                     tweet_dataset['text'],
                                     "@[\w]*")

# tweet_dataset.head()

# tweet_dataset['text'].head()

# Limpiando Tweets
corpus = []
for i in range(0, max_tweets):
    tweet = re.sub('[^a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ]', ' ', tweet_dataset['text'][i])
    tweet = tweet.lower()
    tweet = re.sub('rt', '', tweet)
    tweet = re.sub('http', '', tweet)
    tweet = re.sub('https', '', tweet)
    tweet = tweet.split()
# ps = PorterStemmer()
# tweet = [ps.stem(word) for word in tweet if not
# word in set(stopwords.words('english'))]
    tweet = ' '.join(tweet)
    corpus.append(tweet)

# Word Cloud o Nube de Palabras
all_words = ' '.join([text for text in corpus])
wc = WordCloud(width=800,
               height=500,
               random_state=21,
               max_font_size=110).generate(all_words)
plt.figure(figsize=(10, 7))
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
