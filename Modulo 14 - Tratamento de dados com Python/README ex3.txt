Dando continuação ao exercício, vamos filtrar os produtos com maiores quantidades de comentários (N_Avaliações). Para isso, utilizaremos o método do Intervalo Interquartil (IQR).

Passos:

    Calcular o IQR: O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1): iqr = q3 - q1.
    Determinar o Limite Superior para Outliers: O limite superior é calculado como limite_alto = q3 + 1.5 * iqr.
    Filtrar Produtos Acima do Limite: Filtre os produtos que têm N_Avaliações maior que limite_alto e armazene o resultado na variável df_avaliados.