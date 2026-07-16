USE restaurante;

-- Conta a quantidade de pedidos.
SELECT COUNT(id_pedido) FROM pedidos;

-- Conta a quantidade de clientes unicos que ralizaram pedidos
SELECT COUNT(DISTINCT id_cliente) FROM pedidos;

-- Calcula a média do preço dos produtos
SELECT AVG(preco) FROM produtos;

-- Calcula a mínima e máxima do proço dos produtos (respectivamente)
SELECT MIN(preco) FROM produtos;
SELECT MAX(preco) FROM produtos;

-- Faz um rank de TOP 5 produtos mais caros
SELECT DISTINCT nome, preco, ROW_NUMBER() OVER (ORDER BY preco DESC) AS ranking_preco FROM produtos LIMIT 5;

-- Seleciona a média dos precos dos produtos agrupados por categoria
SELECT categoria, ROUND(AVG(preco), 2) AS media_preco_categoria FROM produtos GROUP BY categoria;

-- Lista os fornecedores e a quantidade de produtos que vieram daquele fornecedor
SELECT fornecedor, COUNT(*) AS quantidade_produtos FROM info_produtos GROUP BY fornecedor;

-- Seleciona fornecedores que possuem mais de um produto cadastrado
SELECT fornecedor, COUNT(*) AS quantidade_produtos_cadastrados FROM info_produtos GROUP BY fornecedor HAVING COUNT(*) > 1;

-- Seleciona clientes que fizeram apenas 1 pedido
SELECT id_cliente, COUNT(*) AS clientes_pedido_unico FROM pedidos GROUP BY id_cliente HAVING COUNT(*) > 1;