from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

DB_PASSWORD = 'Sua_Palavra_Passe'
CONNECTION_STR = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/flask_mvc_app"
DIR_UPLOAD_IMG = 'static/uploads/'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'flask-mvc-app'

db = SQLAlchemy()
db.init_app(app)

engine = create_engine(CONNECTION_STR)