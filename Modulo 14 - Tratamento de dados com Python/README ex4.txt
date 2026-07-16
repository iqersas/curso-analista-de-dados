Finalize o exercício seguindo os passos abaixo:

    Converta a coluna Desconto para o tipo string.
    Modifique a coluna Desconto para exibir apenas o valor numérico do desconto (por exemplo, "18% OFF" deve se tornar "18").
    Crie duas novas colunas baseadas na coluna Condicao:
    Condicao_Atual: Extraia a primeira parte do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "Novo").
    Qtd_Vendidos: Extraia a quantidade de itens vendidos do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "+10mil"). Se não houver quantidade especificada, escreva "Nenhum".

Saiba mais: Caso queria explorar outra solução, você pode usar a função assign para adicionar ou modificar várias colunas de um DataFrame de maneira encadeada. Lembre-se de que você pode passar funções lambda dentro do assign para aplicar transformações nas colunas:

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8').assign(
  # Adicione suas transformações aqui
)

Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html