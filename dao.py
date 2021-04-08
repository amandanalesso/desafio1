from models import Clientes 

SQL_CRIA_JOGO = 'INSERT into clientes (nome, cpf, idade email) values (%s, %s, %s, %s)'

class ClientesDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, clientes):
        cursor = self.__db.connection.cursor()

        if (clientes.id):
            cursor.execute(SQL_ATUALIZA_CLIENTES, (clientes.nome, clientes.cpf, clientes.idade, clientes.email, clientes.id))
        else:
            cursor.execute(SQL_CRIA_CLIENTES, (clientes.nome, clientes.cpf, clientes.idade, clientes.email))
            clientes.id = cursor.lastrowid
        self.__db.connection.commit()
        return clientes

    def listar(self):
        cursor = self.__db.connection.cursor()
        return jogos