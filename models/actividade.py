from config import db, engine

class Actividade(db.Model):
    
    __tablename__ = 'tb_actividade'

    id_actividade = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    nome_actividade = db.Column(db.String(100))
    data_inicio = db.Column(db.Date)
    data_fim = db.Column(db.Date)
    descricao = db.Column(db.String(200))
    resultado = db.Column(db.String(20))


    def __init__(self, id_usuario, nome_actividade, data_inicio, data_fim, descricao, resultado):
        self.id_usuario = id_usuario
        self.nome_actividade = nome_actividade
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        self.resultado = resultado


    def salvar(self):
        db.session.add(self)
        db.session.commit()
    

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
        

    @classmethod
    def obter_actividades_usuario(cls, id):
        return cls.query.filter_by(id_usuario=id).all()


    def obter_todas_actividades():
        return engine.execute("SELECT * FROM tb_usuario "
                            +"JOIN tb_actividade ON tb_usuario.id_usuario = tb_actividade.id_usuario;").fetchall()

   
    @classmethod
    def obter(cls, id):
        return cls.query.filter_by(id_actividade=id).first()
        

    def obter_por_id(id):
        return engine.execute("SELECT * FROM tb_usuario "
                              +"JOIN tb_actividade ON tb_usuario.id_usuario = tb_actividade.id_usuario "
                              + f"WHERE id_actividade = {id};").first()

