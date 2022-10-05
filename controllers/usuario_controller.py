import os
from werkzeug.utils import secure_filename
from config import *
from flask import render_template, request, redirect, flash, url_for
from models.usuario import Usuario

class UsuarioController:

    @app.route('/registo-usuario', methods=['GET', 'POST'])
    def registo_usuario():
        if request.method == 'GET': 
            return render_template('usuario/registar.html')
        else:
            USUARIO_NORMAL = 2
            email = request.form['email']
            senha = request.form['senha']
            nome = request.form['nome']
            file = request.files['foto']
            foto = secure_filename(file.filename)
            file.save(os.path.join(DIR_UPLOAD_IMG, foto))
            usuario = Usuario(USUARIO_NORMAL, email, senha, nome, foto)
            usuario.salvar()
            return redirect(url_for('login'))
    

    @app.route(f'/usuarios', methods=['GET'])
    def listar_usuarios():
        usuarios = Usuario.obter_todos()
        qtd = len(usuarios)
        usuario_logado = Usuario.obter_usuario_logado()
        return render_template('usuario/listar.html', lista_usuarios=usuarios, num_registos=qtd, 
                                usuario_logado=usuario_logado)


    @app.route(f'/usuarios/<id>/detalhes', methods=['GET'])
    def detalhes_usuario(id):
        usuario = Usuario.obter_por_id(id)
        usuario_logado = Usuario.obter_usuario_logado()
        if usuario:
            return render_template('usuario/detalhes.html', usuario=usuario, usuario_logado=usuario_logado)
        else:
            return render_template('_erro/404.html')   

    @app.route(f'/dados-pessoais', methods=['GET'])
    def dados_pessoais():
        usuario_logado = Usuario.obter_usuario_logado()
        dados = Usuario.obter_por_id(usuario_logado.id_usuario)
        return render_template('usuario/dados_pessoais.html', dados=dados, usuario_logado=usuario_logado)
   
        
        

