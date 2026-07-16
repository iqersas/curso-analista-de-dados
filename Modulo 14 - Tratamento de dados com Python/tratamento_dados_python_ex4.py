import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' ')[0])

df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4] if len(x.split(' ')) > 4 else 'Nenhum')

df['Desconto'] = df['Desconto'].astype(str)

df['Desconto'] = df['Desconto'].apply(lambda x: x.replace('%', '').replace(' OFF', ''))