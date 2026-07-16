import pandas as pd
import numpy as np

df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

Qtd_Vendidos_Map = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(Qtd_Vendidos_Map)

Marca_Freq = df['Marca'].value_counts(normalize=True)
df['Marca_Freq'] = df['Marca'].map(Marca_Freq)

Material_Freq = df['Material'].value_counts(normalize=True, dropna=False)

df['Material_Freq'] = df['Material'].apply(lambda x: Material_Freq[x] if pd.notnull(x) else np.nan)