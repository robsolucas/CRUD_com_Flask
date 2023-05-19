"""
Aqui vamos instanciar o app dentro de suas condicoes
-_
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soma.db'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
