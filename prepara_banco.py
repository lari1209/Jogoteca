import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='Fulltime123#', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `usuario_db`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
CREATE DATABASE IF NOT EXISTS usuario_db  /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE usuario_db;
    CREATE TABLE usuarios (
      id varchar(8) COLLATE utf8_bin NOT NULL,
      nome varchar(20) COLLATE utf8_bin NOT NULL,
      senha varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''


conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO usuario_db.usuarios (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('larissa', 'Larissa Freitas', '123'),
            ('nico', 'Nico', 'python'),
            ('luan', 'Luan', 'flask')

      ])

cursor.execute('select * from usuario_db.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando senão nada tem efeito
conn.commit()
cursor.close()
