import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("ecommerce_estatistica.csv")

df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
df["Desconto"] = pd.to_numeric(df["Desconto"], errors="coerce")
df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")
df["Qtd_Vendidos"] = pd.to_numeric(df["Qtd_Vendidos"], errors="coerce")

densidade_map = {
    0.000: "Muito Baixo",
    0.002: "Baixo",
    0.004: "Moderado",
    0.006: "Alto",
    0.008: "Muito Alto",
}


def densidade_formatter(val, pos):
    nearest_value = min(densidade_map.keys(), key=lambda x: abs(x - val))
    return densidade_map[nearest_value]


# 1. HISTOGRAMA
plt.figure(figsize=(8, 6))
sns.histplot(df["Nota"], bins=10, kde=True)
plt.title("Distribuição das Notas dos Produtos")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.show()

# 2. GRÁFICO DE DISPERSÃO
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Nota", y="Qtd_Vendidos")
plt.title("Relação entre Nota e Quantidade Vendida")
plt.xlabel("Nota")
plt.ylabel("Quantidade Vendida")
plt.show()

# 3. MAPA DE CALOR
corr = df[["Nota", "Desconto", "Preço", "Qtd_Vendidos"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor de Correlação entre Variáveis")
plt.show()

# 4. GRÁFICO DE BARRA
top_10_marcas = df.groupby("Marca")["Qtd_Vendidos"].sum().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_marcas.index, y=top_10_marcas.values)
plt.title("Top 10 Marcas com Maior Quantidade Vendida")
plt.xlabel("Marca")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=90)
plt.show()

# 5. GRÁFICO DE PIZZA
genero_bio = df["Gênero"].value_counts().nlargest(2)

plt.figure(figsize=(7, 7))
genero_bio.plot.pie(
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("Set2", len(genero_bio)),
)
plt.title("Gêneros mais Frequentes")
plt.ylabel("")
plt.show()

# 6. GRÁFICO DE DENSIDADE
plt.figure(figsize=(8, 6))
sns.kdeplot(df["Preço"], shade=True, color="purple")
plt.title("Distribuição de Preços dos Produtos")
plt.xlabel("Preço")
plt.ylabel("Densidade")
plt.gca().yaxis.set_major_formatter(FuncFormatter(densidade_formatter))
plt.show()

# 7. GRÁFICO DE REGRESSÃO
plt.figure(figsize=(8, 6))
sns.regplot(
    data=df, x="Preço", y="Nota", scatter_kws={"s": 10}, line_kws={"color": "red"}
)
plt.title("Relação entre Preço e Nota dos Produtos")
plt.xlabel("Preço")
plt.ylabel("Nota")
plt.show()
