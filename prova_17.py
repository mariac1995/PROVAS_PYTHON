# -- Criação da tabela Produtos (exemplo)
# CREATE TABLE Produtos (
#     ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
#     NomeProduto VARCHAR(100) NOT NULL,
#     Categoria VARCHAR(50),
#     Preco DECIMAL(10,2)
# );

# -- Criação da tabela Fornecedores (exemplo)
# CREATE TABLE Fornecedores (
#     FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
#     NomeFornecedor VARCHAR(100) NOT NULL,
#     Telefone VARCHAR(20),
#     Email VARCHAR(100)
# );

# -- Criação da tabela Estoque
# CREATE TABLE Estoque (
#     EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
#     ProdutoID INT NOT NULL,
#     FornecedorID INT NOT NULL,
#     Quantidade INT NOT NULL,
#     DataEntrada DATE NOT NULL,
#     FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
#     FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
# );

# -- Exemplo de consulta com FULL OUTER JOIN
# -- (em alguns bancos como MySQL não existe FULL OUTER JOIN,
# -- então pode ser simulado com UNION de LEFT e RIGHT JOIN)
# SELECT e.EstoqueID, p.NomeProduto, f.NomeFornecedor, e.Quantidade, e.DataEntrada
# FROM Estoque e
# LEFT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
# LEFT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID
# UNION
# SELECT e.EstoqueID, p.NomeProduto, f.NomeFornecedor, e.Quantidade, e.DataEntrada
# FROM Estoque e
# RIGHT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
# RIGHT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID;

# -- Exemplo de agrupamento (GROUP BY)
# SELECT ProdutoID, SUM(Quantidade) AS TotalEstoque
# FROM Estoque
# GROUP BY ProdutoID;

# -- Exemplo de alteração da tabela (ALTER TABLE)
# ALTER TABLE Estoque
# ADD COLUMN PrecoUnitario DECIMAL(10,2);

# ALTER TABLE Estoque
# MODIFY COLUMN Quantidade BIGINT;
