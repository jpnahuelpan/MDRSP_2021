#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Integrantes: J.P. Nahuelpán
# debe crear su propio keys.py con sus keys y tokens
from keys import keys
import tweepy
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt


def ObtenerTweets(palabra="", times=10, lenguaje="en"):

    # Se define las listas que capturan la popularidad

    popularidad_list = []

    numeros_list = []

    numero = 1

    for tweet in tweepy.Cursor(api.search, palabra,
                               lang="en").items(numero_de_Tweets):

        try:

            # Se toma el texto, se hace el analisis de sentimiento

            # y se agrega el resultado a las listas
            print(tweet.created_at)
            print(tweet.text)

            analisis = TextBlob(tweet.text)

            analisis = analisis.sentiment

            popularidad = analisis.polarity
            print("Polaridad sentimiento:", popularidad)

            popularidad_list.append(popularidad)

            numeros_list.append(numero)

            numero = numero + 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

    return (numeros_list, popularidad_list, numero)


def GraficarDatos(numeros_list, popularidad_list, numero):

    axes = plt.gca()

    axes.set_ylim([-1, 2])

    plt.scatter(numeros_list, popularidad_list)

    popularidadPromedio = (sum(popularidad_list))/(len(popularidad_list))

    popularidadPromedio = "{0:.0f}%".format(popularidadPromedio * 100)

    time = datetime.now().strftime("A : %H:%M\n El: %m-%d-%y")

    plt.text(0, 1.25,
             "Sentimiento promedio:  "
             + str(popularidadPromedio)
             + "\n" + time,
             fontsize=12,
             bbox=dict(facecolor='none',
                       edgecolor='black',
                       boxstyle='square, pad = 1'))

    plt.title("Sentimientos sobre " + palabra + " en twitter")
    plt.xlabel("Numero de tweets")
    plt.ylabel("Sentimiento")
    plt.show()


# Se define las variables para el acceso al API de twitter

# keys = [consumer_key, consumer_key_secret, access_token, access_token_secret]

# Se autentica en twitter
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

# se verifica que el usuario conectado en twitter es de uno

print(api.me().name)

# Se pregunta por la palabra a preguntar

palabra = input("Buscar: ")
# Se define la cantida de tweets a capturar
numero_de_Tweets = int(input("Número de tweets a capturar: "))
lenguaje = input("Idioma [es/en]:")

if lenguaje == "es":
    palabra = TextBlob(palabra)
    palabra = palabra.translate(to="en")
    palabra = str(palabra)


numeros_list, popularidad_list, numero = ObtenerTweets(palabra,
                                                       numero_de_Tweets,
                                                       lenguaje)

GraficarDatos(numeros_list, popularidad_list, numero)
