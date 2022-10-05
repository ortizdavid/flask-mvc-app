from config import *
from flask import render_template, request, redirect, url_for
from models.actividade import Actividade
from models.usuario import Usuario

class ActividadeController:
   
    @app.route(f'/actividades', methods=['GET'])
    def listar_actividades():
        usuario_logado = Usuario.obter_usuario_logado()
        if usuario_logado.nome_perfil == 'normal':
            actividades = Actividade.obter_actividades_usuario(usuario_logado.id_usuario)
        else:    
            actividades = Actividade.obter_todas_actividades()
        qtd = len(actividades)
        return render_template('actividade/listar.html', lista_actividades=actividades, num_registos=qtd, usuario_logado=usuario_logado)

    @app.route(f'/actividades/<id>/detalhes', methods=['GET'])
    def detalhes_actividade(id):
        actividade = Actividade.obter_por_id(id)
        return render_template('actividade/detalhes.html', actividade=actividade, usuario_logado=Usuario.obter_usuario_logado())

    @app.route(f'/actividades/registar', methods=['GET', 'POST'])
    def registar_actividade():
        usuario_logado = Usuario.obter_usuario_logado()
        if request.method == 'GET': 
            return render_template('actividade/registar.html', usuario_logado=usuario_logado)
        nome_actividade = request.form['nome_actividade']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        descricao = request.form['descricao']
        resultado = request.form['resultado']
        actividade = Actividade(usuario_logado.id_usuario, nome_actividade, data_inicio, data_fim, descricao, resultado)
        actividade.salvar()
        return redirect(url_for('listar_actividades'))



    @app.route(f'/actividades/<id>/eliminar', methods=['GET', 'POST'])
    def eliminar_actividade(id):
        usuario_logado = Usuario.obter_usuario_logado()
        actividade = Actividade.obter(id)
        if request.method == 'GET': 
            return render_template('actividade/eliminar.html', actividade=actividade, usuario_logado=usuario_logado)
        else:
            actividade.eliminar()
            return redirect('/actividades')
       