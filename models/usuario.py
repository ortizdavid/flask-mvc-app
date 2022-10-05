from config import db, engine
from flask import session

class Usuario(db.Model):
    
    __tablename__ = 'tb_usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_perfil = db.Column(db.Integer)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    nome = db.Column(db.String(150))
    foto = db.Column(db.String(100))


    def __init__(self, id_perfil, email, senha, nome, foto):
        self.email = email
        self.senha = senha
        self.id_perfil = id_perfil
        self.nome = nome
        self.foto = foto
      

    def salvar(self):
        db.session.add(self)
        db.session.commit()
    

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def existe(cls, email, senha) -> bool:
        return bool(cls.query.filter_by(email=email, senha=senha).first())


    def obter_por_id(id):
        return engine.execute("SELECT * FROM tb_usuario "
                              +"JOIN tb_perfil ON tb_usuario.id_perfil = tb_perfil.id_perfil "
                              + f"WHERE tb_usuario.id_usuario = {id};").first()


    def obter_todos():
        return engine.execute("SELECT * FROM tb_usuario "
                              +"JOIN tb_perfil ON tb_usuario.id_perfil = tb_perfil.id_perfil;").fetchall()

    def obter_usuario_logado():
        email = session['email']
        senha = session['senha']
        return Usuario.obter_dados_usuario(email, senha)
      
    def obter_dados_usuario(email, senha):
        return engine.execute(f"SELECT * FROM tb_usuario "
                            +" JOIN tb_perfil ON tb_usuario.id_perfil = tb_perfil.id_perfil "
                            + f" WHERE email = '{email}' AND senha='{senha}';").first()


       


  