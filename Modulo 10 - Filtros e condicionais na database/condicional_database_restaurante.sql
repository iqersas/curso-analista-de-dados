USE restaurante;

-- Seleciona todos os pedidos do funcionario com id 4 e status 'Pendente'
SELECT * FROM pedidos WHERE	id_funcionario = 4 AND status = 'Pendente';

-- Seleciona todos os pedidos que não estão com o status de 'Concluído'
SELECT * FROM pedidos WHERE status != 'Concluído';

-- Filtra a seleção de pedidos para aqueles com id= 1,3,5,7 ou 8
SELECT * FROM pedidos WHERE id_produto IN (1, 3, 5, 7, 8);

-- Seleciona os clientes que possuem o nome com a inicial 'C'
SELECT * FROM clientes WHERE nome LIKE 'C%';

-- Seleciona as informações de produtos que contenham 'carne' ou 'frango' nos ingredientes
SELECT * FROM info_produtos WHERE ingredientes LIKE '%carne%' OR '%frango%';

-- Seleciona produtos com valor entre 20 a 30
SELECT * FROM produtos WHERE preco BETWEEN 20 AND 30;

-- Atualiza o status do pedido com id 6 para NULL
UPDATE pedidos SET status = NULL WHERE id_pedido = 6;
SELECT * FROM pedidos WHERE id_pedido = 6;

-- Seleciona todos os pedidos com status nulos
SELECT * FROM pedidos WHERE status IS NULL;

-- Seleciona o id do pedido e o status, caso status seja nulo, então ele retorna como 'Cancelado'
SELECT id_pedido, IFNULL(status, 'Cancelado') FROM pedidos;

-- Seleciona o nome, cargo e salario dos funcionarios e adiciona um campo chamado media_salario,
-- que irá mostrar 'Acima da media' caso o salario seja > 3000, se for menor então mostra 'Abaixo da media'

SELECT nome, cargo, salario,
	CASE
		WHEN salario > 3000 THEN 'Acima da média'
        ELSE 'Abaixo da média'
	END AS media_salario
FROM funcionarios;