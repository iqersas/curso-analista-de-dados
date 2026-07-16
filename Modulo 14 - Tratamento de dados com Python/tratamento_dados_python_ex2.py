import pandas as pd

df = pd.read_csv('/data/ecommerce_ex2.csv')

df['Marca'] = df['Marca'].str.lower()

df['Material'] = df['Material'].str.lower()

df['Temporada'] = df['Temporada'].str.lower()

df = df.drop_duplicates()

df = df.dropna(thresh=8)