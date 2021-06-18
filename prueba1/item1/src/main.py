# integrantes:Juan Pablo Nahuelpan
import pandas as pd
from modulo import*
url = "https://datosmacro.expansion.com/otros/coronavirus-vacuna"
df = pd.read_html(url, thousands=".", decimal=",")[0]


print(df)
def main(dataframe):
    df = dataframe
    df = df.loc[:, ["Países", "Completamente vacunadas", "% completamente vacunadas"]]
    df["Países"] = df["Países"].str.strip(" [+]")
    df.dropna(subset=["Completamente vacunadas", "% completamente vacunadas"], inplace=True)
    
    df_d = ordenar_extraer(df, [0, 1], "Completamente vacunadas", 15, "entero")
    df_e = ordenar_extraer(df, [0, 2], "% completamente vacunadas", 15, "porcentaje")
    
    imprimir(df_d, "vacunados_absolutos")
    imprimir(df_e, "vacunados_porcentaje")    
  
if __name__ == "__main__":
    main(df)  