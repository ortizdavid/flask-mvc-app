# Projecto MVC com Flask

### Funcionalidades:
- Registo de Usuários
- Login e Logout
- Regito de Actividades
- Listagem de Actividades
- Upload de Imagens
- Detalhes das Actividades

### Ferramentas Nesscessárias:

- PostgreSQL v13
- Python v3.9
- PIP


## Execução da Base de Dados (PostgreSQL)

1 - Criar a Base de Dados:
``
CREATE DATABASE flask_mvc_app;
``

2 - Conectar a Base de Dados:
``
\c flask_mvc_app;
``

3 - Copiar o script da base de dados:

Ficheiro - [flask_mvc_app.sql](flask_mvc_app.sql)

ou

Copiar o Seguinte Script:

``
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
INSERT INTO tb_perfil (nome_perfil) VALUES ('administrador');
INSERT INTO tb_perfil (nome_perfil) VALUES ('normal');
INSERT INTO tb_usuario (id_perfil, email, senha) VALUES (1, 'admin@gmail.com', '12345678');
``


## Execução da Aplicação

1 - Entrar na pasta do projecto pela linha de comandos (cmd, Power Shell ou Bash):
``
cd flask-mvc-app
``

2 - Instalar o Ambiente Virtual (Virtual Environment):
``
pip install virtualenv
``

3 - Criar o Ambiente Virtual:
``
virtualenv venv
``

4 - Activar o ambiente Virtual:
``
venv/Scripts/activate
``

5 - Instalar as dependências, execute o comando:
``
pip install -r requirements.txt
``

6 - Editar a palavra passe da Base de dados:
ficheiro: [config.py](config.py)
``
DB_PASSWORD = 'Sua_Palavra_Passe'
``

7 - Executar o projecto, entre na linha de comando execute o comando:
``
flask run ou python app.py
``

8 - Entre no Navegador:

<http://localhost:5000>

9 - Faça Login(com Email) como Administrador de Teste:
- Email: admin@gmail.com
- Senha: 12345678
