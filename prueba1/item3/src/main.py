# Juan Pablo Nahuelpan
import pandas as pd
import os

ruta_src = os.path.dirname(os.path.realpath(__file__)) 
ruta_archivo = ruta_src.replace("src", "input/prueba1.xlsx")
ruta_salida_personal = ruta_src.replace("src", "output/personal.csv")
ruta_salida_depto = ruta_src.replace("src", "output/depto.csv")
ruta_salida_vehiculos = ruta_src.replace("src", "output/vehiculos.csv")

df_personal = pd.read_excel(ruta_archivo, index_col=0, sheet_name="personal")  
df_depto = pd.read_excel(ruta_archivo, index_col=0, sheet_name="depto")  
df_vehiculos = pd.read_excel(ruta_archivo, index_col=0, sheet_name="vehiculos")  

df_personal[df_personal["edad"]>=25].to_csv(ruta_salida_personal, index=None, header=True, encoding="utf-8")
df_depto.to_csv(ruta_salida_depto, index=None, header=True, encoding="utf-8")
df_vehiculos.sort_values("año", ascending=True, ignore_index=True, inplace=True)
df_vehiculos.to_csv(ruta_salida_vehiculos, index=None, header=True, encoding="utf-8")
