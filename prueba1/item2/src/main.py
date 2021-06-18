# Juan Pablo Nahuelpan
import pandas as pd
import os

ruta_src = os.path.dirname(os.path.realpath(__file__)) 
ruta_archivo = ruta_src.replace("src", "input/cereales.csv")
ruta_salida_calories = ruta_src.replace("src", "output/top20_calorias.csv")
ruta_salida_sodium = ruta_src.replace("src", "output/sodio200.csv")


df = pd.read_csv(ruta_archivo, sep=";")
df = df.loc[:, ["name", "calories", "protein", "fat", "sodium"]]

df.dropna(subset=["calories"], inplace=True)

df.sort_values("calories", ascending=False, ignore_index=True, inplace=True)
df_calorias = df.iloc[0:20, [0, 1, 2, 3, 4]]
df_calorias.to_csv(ruta_salida_calories, index=None, header=True, encoding="utf-8")

df_sodium = df[df["sodium"]>=200]
df_sodium.sort_values("sodium", ascending=True, ignore_index=True, inplace=True)
df_sodium = df_sodium.iloc[:, [0, 4]]
df_sodium.to_csv(ruta_salida_sodium, index=None, header=True, encoding="utf-8")
