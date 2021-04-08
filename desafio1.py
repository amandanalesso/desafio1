from flask import Flask, render_template, request, redirect, url_for
from dao import ClientesDao
from flask_mysqldb import MySQL
from models import Clientes

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "tay13folk"
app.config['MYSQL_DB'] = "desafio1"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
clientes_dao = ClientesDao(db)

@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html',titulo='Clientes', clientes = lista)


@app.route('/novo')
def novo():
    return redirect(url_for('novo.html', titulo='novo cliente'))

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    cpf = request. form['cpf']
    idade = request. form['idade']
    email = request. form['email']
    cliente = cliente(nome, idade, cpf, email )
    clientes_dao.salvar(cliente)
    return redirect(url_for('index'))

    app.run()