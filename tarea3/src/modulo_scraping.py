import pandas as pd
# paso1
url = "https://datosmacro.expansion.com/otros/coronavirus"
df = pd.read_html(url)
#paso2
df2 = pd.DataFrame(df[0].loc[:, ["Países", "Confirmados"]])
print(df2)
df2["Países"] = df2["Países"]. astype("string")
df2["Países"] = df2["Países"].str.strip(" [+]")
#df2["Confirmados"] = df2["Confirmados"].replace(".", "")

for indice in range(0, len(df2["Confirmados"])):
    df2["Confirmados"].iloc[indice]= df2["Confirmados"].iloc[indice].replace(".", "")
    
print(df2)
df2["Confirmados"] = df2["Confirmados"].astype("int32")

#paso3
df3 = df2.sort_values(by=["Confirmados"], ascending=False)

df3= df3.iloc[0:10, 1]

print(df3)