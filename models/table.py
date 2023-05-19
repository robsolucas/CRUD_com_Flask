from crud_com_flask.app import db


class Soma(db.Model):
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    numero1 = db.Column(db.Float)
    numero2 = db.Column(db.Float)
    soma = db.Column(db.Float)

    def __init__(self, n1: float, n2: float):
        self.numero1 = n1
        self.numero2 = n2
        self.soma = n1 + n2
