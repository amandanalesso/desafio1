import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='tay13folk', host='localhost', port=3306)

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `desafio1`;
    USE `desafio1`;
    CREATE TABLE `clientes` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `cpf` varchar(11) NOT NULL,
      `idade` date NOT NULL,
      `email` varchar(40) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
   '''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO desafio1.clientes (id, nome, idade, cpf, email) VALUES (%s, %s, %s, %s, %s)',
      [
            ('Estella', '13131313131',  '22','stela@gmail.com'),
            ('betty', '45632178528', '13', 'betty@gmail.com'),
            ('inez', '12312312312',  '39', 'inez@gmail.com')
      ])

cursor.execute('select * from desafio1.clientes')
print(' --------  Clientes ----------')
for user in cursor.fetchall():
    print(user[1])

conn.commit()
cursor.close()
