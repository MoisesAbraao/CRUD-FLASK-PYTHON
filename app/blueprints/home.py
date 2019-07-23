from flask import Blueprint, render_template, request, redirect, url_for
from app.models.tables import Pessoa
from app.models.forms import CadastroForm
from app.ext.db import db

bp_app = Blueprint("home", __name__)


@bp_app.route("/")
@bp_app.route("/home")
def home():
    return render_template("index.html")


@bp_app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    form = CadastroForm()
    if form.validate_on_submit():
        p = Pessoa(
            nome=form.nome.data,
            rua=form.rua.data,
            numero=form.numero.data,
            bairro=form.bairro.data,
            cidade=form.cidade.data,
            estado=form.estado.data,
            fone=form.fone.data,
            cpf=form.cpf.data,
            email=form.email.data,
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("home.home"))
    return render_template("cadastro.html", form=form)


@bp_app.route("/lista")
def lista():
    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)


@bp_app.route("/atualizar/<int:id>", methods=["GET", "POST"])
def atualizar(id):
    form = CadastroForm()
    pessoa = Pessoa.query.filter_by(_id=id).first()

    if form.validate_on_submit():
        form.populate_obj(pessoa)
        db.session.commit()

    form = CadastroForm()
    form.insert_data(pessoa)
    return render_template("atualizar.html", form=form)


@bp_app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    db.session.delete(pessoa)
    db.session.commit()
    return redirect(url_for("home.lista"))


def configure(app):
    app.register_blueprint(bp_app)
