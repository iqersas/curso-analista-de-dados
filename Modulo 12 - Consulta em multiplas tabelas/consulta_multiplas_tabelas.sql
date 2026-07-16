USE restaurante;

-- Selecionar o nome dos clientes com pedidos com status "Pendente"
SELECT
	pedidos.id_pedido,
    pedidos.quantidade,
    pedidos.data_pedido,
	clientes.nome,
    clientes.email
FROM clientes
INNER JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
WHERE pedidos.status = 'Pendente'
ORDER BY pedidos.id_pedido DESC;

-- Selecionar clientes sem pedidos
SELECT
	clientes.nome
FROM clientes
LEFT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
WHERE pedidos.id_pedido IS NULL;

-- Selecionar o nome do cliente e o total de pedidos de cada um
SELECT
	clientes.nome,
    COUNT(pedidos.id_pedido) AS total_pedidos
FROM clientes
LEFT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
GROUP BY clientes.nome;

-- Selecionar o preço total de cada pedido
SELECT
	pedidos.id_pedido,
    pedidos.quantidade,
    produtos.nome,
    produtos.preco,
    (pedidos.quantidade*produtos.preco) AS preco_total
FROM pedidos
INNER JOIN produtos ON pedidos.id_produto = produtos.id_produto;
