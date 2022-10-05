from config import *
from flask import render_template, request, redirect, url_for, session
from models.usuario import Usuario

class AuthController:
    
    @app.route(f'/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('auth/login.html')
        else:
            email = request.form['email']
            senha = request.form['senha']
            if(Usuario.existe(email, senha)):
                session['email'] = email
                session['senha'] = senha
                return redirect(url_for('pagina_inicial'))
            else:
                return redirect(url_for('login'))

    @app.route(f'/logout', methods=['GET'])
    def logout():
        session.pop('email')
        return redirect(url_for('login'))

    @app.route(f'/pagina-inicial', methods=['GET'])
    def pagina_inicial():
        usuario_logado = Usuario.obter_usuario_logado()
        return render_template('usuario/pagina_inicial.html', usuario_logado=usuario_logado)