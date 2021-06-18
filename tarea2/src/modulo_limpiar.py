# El modulo_limpiar proporciona un conjunto de funciones que ayudaran
# a ordenar y limpiar los datos para la tarea.
import pandas as pd


def paso1(datos):
    df = datos
    df.columns = ["Ano", "Ciudad", "Deporte",
                     "Especialidad",  "Ganador", "Competencia", "Genero", "Medalla"]   
    return df


def paso_2_3(datos):
    df = datos
    for columna in df.columns:
        if columna != "Ano":      
            df[columna]=df[columna].astype("string")
        else:
            moda_ano = int(df[columna].mode())
            df[columna]=df[columna].fillna(moda_ano)
            df[columna]=df[columna].astype("int16")
    return df


def paso_4_5(datos):
    df = datos
    df["Ciudad"] = df["Ciudad"].str.upper()
    for columna in df.columns:
        if columna != "Ano":      
            df[columna] = df[columna].str.strip()
        else:
            pass
    return df


def paso_6_7(dataframe):
    df = dataframe
    for indice in range(0, len(df["Ciudad"])):
        # temp = df["Genero"].iloc[indice]
        if pd.notna(df["Genero"].iloc[indice]) and (df["Genero"].iloc[indice] not in ["M", "W", "X"]):          
            df["Genero"].iloc[indice] = "X"
        # print(temp, " se remplaza por==> ",df["Genero"].iloc[indice])
        else:
            pass
    df.dropna(subset=["Ciudad", "Deporte", "Especialidad", 
                        "Ganador", "Competencia", "Genero", "Medalla"])
    return df
