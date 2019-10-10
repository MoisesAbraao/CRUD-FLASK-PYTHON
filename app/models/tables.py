from app.ext.db import db


class Pessoa(db.Model):
    __tablename__ = "pessoa"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    fone = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String)
