Para finalizar, vamos desenvolver um modelo de Regressão Linear:

    Divida os dados em 2 partes: 20% para testes e 80% para treinamento. Armazene nas variáveis correspondentes: x_train, x_test, y_train e y_test. Atenção, você deve utilizar os parâmetros com esses valores: test_size=0.2 e random_state = 42.
    Crie um modelo de Regressão Linear, utilizando o sklearn, e ajuste-o sobre os dados de treinamento. Armazene o modelo na variável modelo_lr.
    Faça uma previsão dos valores utilizando a base de teste e armazene o resultado na variável y_prev.
    Calcule as seguintes métricas para avaliar o seu modelo: R², RMSE e o desvio padrão do campo Qtd_Vendidos_Cod, e armazene nas respectivas variáveis: r2, rmse, desvio_padrao.