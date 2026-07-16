import pandas as pd

df = pd.read_csv("/data/ecommerce_preparados.csv")
df = df.dropna()

# Escreva seu código abaixo

# Cálculo das estatísticas
media = df["Desconto"].mean()  # Média dos descontos
mediana = df["Desconto"].median()  # Mediana dos descontos
variancia = df["Desconto"].var()  # Variância dos descontos
desvio_padrao = df["Desconto"].std()  # Desvio padrão dos descontos

# Como a função mode() retorna uma Série contendo todas as modas, [0] é usado para selecionar a primeira moda caso haja múltiplas.
moda = df["Desconto"].mode()[0]  # Moda dos descontos

minimo = df["Desconto"].min()  # Valor mínimo do desconto
quartis = df["Desconto"].quantile([0.25, 0.5, 0.75])  # Quartis dos descontos
maximo = df["Desconto"].max()  # Valor máximo do desconto

# Exibe as primeiras linhas do DataFrame
df.head()