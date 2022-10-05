CREATE TABLE tb_perfil (
    id_perfil SERIAL PRIMARY KEY,
    nome_perfil VARCHAR(50) UNIQUE NOT NULL 
);

CREATE TABLE tb_usuario (
    id_usuario SERIAL PRIMARY KEY,
    id_perfil INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL, 
    nome VARCHAR(150),
    foto VARCHAR(100),
    data_registo DATE DEFAULT CURRENT_DATE
);

CREATE TABLE tb_actividade (
    id_actividade SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    nome_actividade VARCHAR(150) NOT NULL,
    resultado VARCHAR(20),
    data_inicio DATE,
    data_fim DATE, 
    descricao VARCHAR(150) NOT NULL,
    CONSTRAINT fk_actividade_usuario FOREIGN KEY(id_usuario) REFERENCES tb_usuario(id_usuario) 
);

-- INSERÇÃO de PERFIS DE USUÁRIO --------------------------------------
INSERT INTO tb_perfil (nome_perfil) VALUES ('administrador');
INSERT INTO tb_perfil (nome_perfil) VALUES ('normal');
INSERT INTO tb_usuario (id_perfil, email, senha) VALUES (1, 'admin@gmail.com', '12345678');

