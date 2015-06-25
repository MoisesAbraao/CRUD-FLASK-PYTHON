#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Pessoa(db.Model):
	__tablename__ = 'pessoa'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String)
	sobrenome = db.Column(db.String)
	endereco = db.Column(db.String)
	numero = db.Column(db.String)
	telefone = db.Column(db.String)

	def __init__(self, nome, sobrenome, endereco, numero, telefone):
		self.nome = nome
		self.sobrenome = sobrenome
		self.endereco = endereco
		self.numero = numero
		self.telefone = telefone


db.create_all()

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/")
@app.route("/cadastrar")
def cadastrar():
	return render_template("cadastro.html")

def voltar():
	return render_template("home")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		nome = (request.form.get("nome"))
		sobrenome = (request.form.get("sobrenome"))
		endereco = (request.form.get("endereco"))
		numero = (request.form.get("numero"))
		telefone = (request.form.get("telefone"))
		if nome and sobrenome and endereco and numero and telefone:
			p = Pessoa(nome, sobrenome, endereco, numero, telefone)
			db.session.add(p)
			db.session.commit()
	return redirect(url_for("home"))

@app.route("/lista")
def lista():
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
	pessoa = Pessoa.query.filter_by(_id=id).first()
	if request.method == "POST":
		nome = (request.form.get("nome"))
		sobrenome = (request.form.get("sobrenome"))
		endereco = (request.form.get("endereco"))
		numero = (request.form.get("numero"))
		telefone = (request.form.get("telefone"))
		if nome and sobrenome and endereco and numero and telefone:
			pessoa.nome = nome
			pessoa.sobrenome = sobrenome
			pessoa.endereco = endereco
			pessoa.numero = numero
			pessoa.telefone = telefone
			db.session.commit()

	return render_template("atualizar.html", pessoa=pessoa)

@app.route("/excluir/<int:id>")
def excluir(id):
	pessoa = Pessoa.query.filter_by(_id=id).first()

	db.session.delete(pessoa)
	db.session.commit()
	
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)





if __name__ == "__main__":
	app.run(debug=True)
