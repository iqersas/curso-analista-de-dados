import pandas as pd

df = pd.read_csv('/data/ecommerce_tratados.csv')

# Verifica a quantidade de dados únicos em cada coluna
unicos = df.nunique()
print('Analise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preço" com o cálculo em relação aos campos "Reais" e "Centavos"
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove os campos citados nas intruções e armazene novamente na variável `df`
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])