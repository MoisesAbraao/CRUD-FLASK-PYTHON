from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    rua = StringField('Rua', validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired()])
    bairro = StringField('Bairro', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    fone = StringField('Fone', validators=[DataRequired()])
    cpf = StringField('Cpf', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    def insert_data(self, pessoa):
        self.nome.data = pessoa.nome
        self.rua.data = pessoa.rua 
        self.numero.data = pessoa.numero
        self.bairro.data = pessoa.bairro
        self.cidade.data = pessoa.cidade
        self.estado.data = pessoa.estado
        self.fone.data = pessoa.fone
        self.cpf.data = pessoa.cpf
        self.email.data = pessoa.email