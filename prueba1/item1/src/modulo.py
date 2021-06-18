# integrantes:Juan Pablo Nahuelpan
import os

def ordenar_extraer(data_frame, indices_cols_impr, nombre_col_ord, cantidad, tipo_dato):
    df = data_frame
    if tipo_dato == "porcentaje":
        df[nombre_col_ord] = df[nombre_col_ord].str.strip("%")
        
        for indice in range(0, len(df[nombre_col_ord])):
            df[nombre_col_ord].iloc[indice] = df[nombre_col_ord].iloc[indice].replace(",", ".")
            
        df[nombre_col_ord]=df[nombre_col_ord].astype("float32")
        df.sort_values(nombre_col_ord, ascending=False, ignore_index=True, inplace=True)
        df[nombre_col_ord]=df[nombre_col_ord].astype("string")
        
        for indice in range(0, len(df[nombre_col_ord])):
            df[nombre_col_ord].iloc[indice] = df[nombre_col_ord].iloc[indice]  + "%"  
        
        df = df.iloc[0:cantidad, indices_cols_impr]
        return df

    elif tipo_dato == "entero":
        df["Completamente vacunadas"]=df["Completamente vacunadas"].astype("int64")
        df.sort_values("Completamente vacunadas", ascending=False, ignore_index=True, inplace=True)
        df = df.iloc[0:cantidad, indices_cols_impr]
        return df

def imprimir(data_frame, nombre_archivo):
    ruta_src = os.path.dirname(os.path.realpath(__file__)) 
    ruta_salida = ruta_src.replace("src", "output/"+nombre_archivo+".csv")
    df = data_frame
    df.to_csv(ruta_salida, index=None, header=True, encoding="utf-8")
    