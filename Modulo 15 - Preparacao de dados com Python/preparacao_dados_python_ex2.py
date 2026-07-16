import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

scaler = MinMaxScaler()

scaler.fit(df[["Nota", "N_Avaliacoes", "Desconto", "Preco"]])
df["Nota_MinMax"] = scaler.fit_transform(df[["Nota"]])
df["N_Avaliacoes_MinMax"] = scaler.fit_transform(df[["N_Avaliacoes"]])
df["Desconto_MinMax"] = scaler.fit_transform(df[["Desconto"]])
df["Preco_MinMax"] = scaler.fit_transform(df[["Preco"]])

le_marca = LabelEncoder()
le_material = LabelEncoder()
le_temporada = LabelEncoder()

le_marca.fit(df["Marca"])
le_material.fit(df["Material"])
le_temporada.fit(df["Temporada"])

df["Marca_Cod"] = le_marca.fit_transform(df["Marca"])
df["Material_Cod"] = le_material.fit_transform(df["Material"])
df["Temporada_Cod"] = le_temporada.fit_transform(df["Temporada"])