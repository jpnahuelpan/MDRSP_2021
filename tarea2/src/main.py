#Integrante: Juan Pablo Nahuelpán
import os
import pandas as pd
# modulos propios del proyecto.
from modulo_limpiar import*

ruta_src = os.path.dirname(os.path.realpath(__file__)) 
ruta_archivo = ruta_src.replace("src", "input/premios.csv")
df = pd.read_csv(ruta_archivo, sep=";", header=None)

ruta_salida = ruta_src.replace("src", "output/premios_modificado.csv")

def main(dataframe):
    df = dataframe
    df = paso1(df)
    df = paso_2_3(df)
    df = paso_4_5(df)
    df = paso_6_7(df)
    df.to_csv(ruta_salida, index=None, header=True, encoding="utf-8")
if __name__ == "__main__":
    main(df)    