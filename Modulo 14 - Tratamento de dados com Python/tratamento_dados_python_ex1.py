import pandas as pd

df = pd.read_csv('/data/ecommerce.csv')

linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

nulos = (df.isnull().sum())
print('Verificar valores nulos:\n', nulos)

df['Temporada'] = df['Temporada'].fillna('Não Definido')
df['Marca'] = df['Marca'].fillna('Não Definido')