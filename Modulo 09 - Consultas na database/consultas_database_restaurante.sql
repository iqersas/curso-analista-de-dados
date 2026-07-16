USE restaurante;

-- Seleciona nome e categoria de produtos que possuem preço maior que 30;
SELECT nome, categoria FROM produtos WHERE preco > 30;

-- Seleciona nome, telefone e data de nascimento de clientes que nasceram antes do ano de 1985;
SELECT nome, telefone, data_nascimento FROM clientes WHERE YEAR(data_nascimento) < 1985;

-- Seleciona os produtos que possuem carne como parte de seu ingrediente;
SELECT id_produto, ingredientes FROM info_produtos WHERE ingredientes LIKE '%carne%';

-- Seleciona o nome e categoria dos produtose os ordena em ordem alfabetica;
SELECT nome, categoria FROM produtos ORDER BY categoria, nome;

-- Seleciona os cinco produtos mais caros do restaurante;
SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 5;

-- Seleciona dois pratos principais para promoção;
SELECT nome, categoria FROM produtos WHERE categoria = 'Prato Principal' LIMIT 2 OFFSET 5;

-- Realiza o BKP de todos os dados presentes na table de pedidos;
CREATE TABLE backup_pedidos AS SELECT * FROM pedidos;