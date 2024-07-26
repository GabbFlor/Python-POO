-- Criação do banco de dados
CREATE DATABASE testepython;

-- Selecionando o banco de dados
USE testepython;

-- Criação da tabela pessoas
CREATE TABLE pessoas (
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	idade INT NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE
)