#!/usr/bin/env python
# -*- coding: utf-8 -*-
# integrantes: Juan Pablo Nahuelpán
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
from keys import keys # debe crear su propio keys.py con sus keys y tokens
# keys = [consumer_key, consumer_key_secret, access_token, access_token_secret]

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Definiendo la palabra de búsqueda y el número de tweets
query = str(input("Ingrese palabra clave: "))
query = TextBlob(query)
max_tweets = 20
if query.detect_language() != 'en':
    query = query.translate(to='en')
searched_tweets = [status for status in tweepy.Cursor(
                                                      api.search,
                                                      q=query).items(
                                                      max_tweets)]
datos = []
for tweet in searched_tweets:
    try:
        text = TextBlob(tweet.text)
        if text.detect_language() != 'en':
            text = text.translate(from_lang=text.detect_language(), to='en')
        polaridad = text.sentiment.polarity
        subjetividad = text.sentiment.subjectivity
        datos.append([polaridad, subjetividad, tweet.created_at])
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

fechas = [datos[i][2] for i in range(0, len(datos))]
polaridad = [datos[i][0] for i in range(0, len(datos))]
subjetividad = [datos[i][1] for i in range(0, len(datos))]

fig, ax = plt.subplots()
ax.scatter(fechas, polaridad, label='Polaridad', c='red')
ax.scatter(fechas, subjetividad, label='Subjetividad', c='blue')
plt.axhline(0, label='Punto medio de polaridad', c='red')
plt.axhline(0.5, label='Punto medio de subjetividad', c='blue')
ax.set_xticks(fechas)
ax.set_xticklabels(fechas, rotation=90, linespacing=2.0, fontsize='xx-small')
ax.legend()

fig.tight_layout()
plt.show()
plt.show()