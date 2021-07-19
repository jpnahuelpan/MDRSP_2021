#!/usr/bin/env python
# -*- coding: utf-8 -*-
# integrantes: Juan Pablo Nahuelpán
from textblob.utils import tree2str
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
from keys import keys # debe crear su propio keys.py con sus keys y tokens
# keys = [consumer_key, consumer_key_secret, access_token, access_token_secret]

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Definiendo la palabra de búsqueda y el número de tweets
query = str(input("Usuario: "))
max_tweets = 30
searched_tweets = [status for status in api.user_timeline(
                                                          screen_name=query,
                                                          count=max_tweets)]
datos = [0,0]
for tweet in searched_tweets:
    try:
        text = TextBlob(tweet.text)
        if text.detect_language() != 'en':
            text = text.translate(from_lang=text.detect_language(), to='en')
            if (text.sentiment.subjectivity <= 0.5):
                datos[0] += 1
            else:
                datos[1] += 1
    except tweet.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

plt.pie(datos, labels=['Objetividad', 'Subjetividad'], autopct='%1.1f%%', normalize=False)
plt.show()