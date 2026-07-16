USE restaurante;

-- Cria uma VIEW que mostra todas as informações a respeito de um pedido realizado.
CREATE VIEW resumo_pedido AS
SELECT
	pedidos.id_pedido, pedidos.quantidade, pedidos.data_pedido,
    clientes.nome AS cliente_nome,
    clientes.email,
    funcionarios.nome AS funcionario_nome,
    produtos.nome AS produto_nome,
    produtos.preco
FROM pedidos
INNER JOIN clientes ON pedidos.id_cliente = clientes.id_cliente
INNER JOIN funcionarios ON pedidos.id_funcionario = funcionarios.id_funcionario
INNER JOIN produtos ON pedidos.id_produto = produtos.id_produto;

-- Seleciona o valor total dos pedidos que cada cliente fez.
SELECT 
	id_pedido,
    cliente_nome,
    (quantidade * preco) AS total_pedido
FROM resumo_pedido;

-- Atualiza a VIEW resumo_pedido adicionando o campo total_pedido.
CREATE OR REPLACE VIEW resumo_pedido AS
SELECT
	pedidos.id_pedido, pedidos.quantidade, pedidos.data_pedido,
    clientes.nome AS cliente_nome,
    clientes.email,
    funcionarios.nome AS funcionario_nome,
    produtos.nome AS produto_nome,
    produtos.preco,
    pedidos.quantidade * produtos.preco AS total
FROM pedidos
INNER JOIN clientes ON pedidos.id_cliente = clientes.id_cliente
INNER JOIN funcionarios ON pedidos.id_funcionario = funcionarios.id_funcionario
INNER JOIN produtos ON pedidos.id_produto = produtos.id_produto;

-- Refaz a consulta que seleciona o valor total dos pedidos que cada cliente fez utilizando o campo "total".
SELECT
	id_pedido,
    cliente_nome,
    total
FROM resumo_pedido;

-- Mostra as informações a respeito da consulta realizada anteriormente.
EXPLAIN SELECT
	id_pedido,
    cliente_nome,
    total
FROM resumo_pedido;

-- Cria uma função que recebe um id de pedido e retorna seus ingredientes
DELIMITER //

CREATE FUNCTION BuscaIngredientesProduto(p_id_info INT)
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE v_ingredientes TEXT;
    SELECT ingredientes INTO v_ingredientes FROM info_produtos WHERE id_info = p_id_info;
    RETURN v_ingredientes;
END //

DELIMITER ;

-- Cria uma função que diz se o total do pedido é abaixo, igual ou maior que a media geral dos pedidos.
DELIMITER $$

CREATE FUNCTION mediaPedido(p_id_pedido INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE v_media_total DECIMAL(10,2);
    DECLARE v_total_pedido DECIMAL(10,2);
    DECLARE v_mensagem VARCHAR(255);

    SELECT AVG(total) INTO v_media_total FROM resumo_pedido;

    SELECT total INTO v_total_pedido FROM resumo_pedido WHERE id_pedido = p_id_pedido;

    IF v_total_pedido IS NULL THEN
        SET v_mensagem = 'Pedido não encontrado.';
    ELSE
        IF v_total_pedido > v_media_total THEN
            SET v_mensagem = CONCAT('O total do pedido é acima da média de R$ ', FORMAT(v_media_total, 2), '.');
        ELSEIF v_total_pedido < v_media_total THEN
            SET v_mensagem = CONCAT('O total do pedido é abaixo da média de R$ ', FORMAT(v_media_total, 2), '.');
        ELSE
            SET v_mensagem = CONCAT('O total do pedido é igual à média de R$ ', FORMAT(v_media_total, 2), '.');
        END IF;
    END IF;

    RETURN v_mensagem;
END $$

DELIMITER ;