from models import Usuario

SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuarios where id = %s and senha = %s'


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id, senha):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id, senha))  # procura usuario de acordo com o id
        dados = cursor.fetchone()  # seleciona apenas um usuario de acordo com o id
        usuario = traduz_usuario(dados) if dados else None  # usuario = Usuario() se existir os dados
        return usuario  # retorna o objeto usuario


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])  # retorna nome, id, senha
