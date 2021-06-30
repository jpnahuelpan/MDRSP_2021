# integrantes: Juan Pablo Nahuelpán

import pandas as pd
import os 

# paso 1
url = "https://datosmacro.expansion.com/otros/coronavirus"
df = pd.read_html(url)

ruta_src = os.path.dirname(os.path.realpath(__file__))
ruta_salida_mayores = ruta_src.replace("src", "output/mayores.csv")
ruta_salida_menores = ruta_src.replace("src", "output/menores.csv")

#paso 2
df2 = pd.DataFrame(df[0].loc[:, ["Países", "Confirmados"]])

df2["Países"] = df2["Países"]. astype("string")
df2["Países"] = df2["Países"].str.strip(" [+]")

for indice in range(0, len(df2["Confirmados"])):
    df2["Confirmados"].iloc[indice]= df2["Confirmados"].iloc[indice].replace(".", "")
    
df2["Confirmados"] = df2["Confirmados"].astype("int32")

#paso 3 y 4
ord_des = df2.sort_values(by=["Confirmados"], ascending=False)
ord_asc = df2.sort_values(by=["Confirmados"], ascending=True)
max_10 = ord_des.iloc[0:10, 0:2]
min_10 = ord_asc.iloc[0:10, 0:2]

max_10.to_csv(ruta_salida_mayores, index=None, header=True, encoding="utf-8")
min_10.to_csv(ruta_salida_menores, index=None, header=True, encoding="utf-8")


