import pandas as pd

df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Escreva seu código abaixo

# Calcula a correlação entre a quantidade vendida e o número de avaliações
corr_n_avaliacoes = df[['Qtd_Vendidos_Cod', 'N_Avaliacoes_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e a nota média
corr_nota = df[['Qtd_Vendidos_Cod', 'Nota_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e o preço
corr_preco = df[['Qtd_Vendidos_Cod', 'Preco_MinMax']].corr()

# Exibe os resultados
print("Correlação com o número de avaliações:", corr_n_avaliacoes)
print("Correlação com a nota média:", corr_nota)
print("Correlação com o preço:", corr_preco)
