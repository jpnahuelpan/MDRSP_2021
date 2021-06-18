#Integrantes: Juan Pablo Nahuelpán
import pandas as pd

data={
    "Nombre": ["María", "Luis", "Carmen", "Antonio"],
    "Edad": [18, 22,29, 21],
    "Grado": ["Economía", "Medicina", "Arquitectura", "Economía"],
    "Correo": ["maria@gmail.com", "luis@yahoo.es", "carmen@gmail.com", "antornio@gmail.com"]
}

df = pd.DataFrame(data)

print(df)
