


#-------CODIGOS SQL-------
codigos = {
'SQL_CREATE_INST' : "INSERT INTO INSTRUTORES (NOME) VALUES ('%s')",
#CRUD TABELA USUARIOS
'SQL_CREATE_USER' : "INSERT INTO `plataforma`.`usuarios` ( nome, email, senha, foto) VALUES ('{0}', '{1}', '{2}', '{3}');",
'SQL_SELECT_USER' : "SELECT `usuarios`.`nome`, `usuarios`.`email`, `usuarios`.`senha`, `usuarios`.`foto` FROM `plataforma`.`usuarios` where id = %d;",
'SQL_BUSCA_EMAIL' : "SELECT SENHA FROM USUARIOS WHERE EMAIL = '{0}';",
#Busca videos
'SQL_BUSCA_VIDEO' : "SELECT `topicos`.`id`, `topicos`.`data_publicacao`, `topicos`.`cursos_id`, `topicos`.`conteudo` FROM `plataforma`.`topicos` where id = {0};",
'SQL_BUSCA_VIDEOS': "SELECT * FROM CURSOS",
    #LOGIN ADMIN
'SQL_BUSCA_ADMIN' : "SELECT * FROM instrutores where nome = '{0}';",



}

SQL_UPDATE_USER = "UPDATE plataforma.usuarios SET nome ='%s', email = '%s', senha ='%s', foto = '%s' WHERE id = '%d';"
SQL_DELETE_USER = "DELETE FROM instrutores where id = 2;"
#CRUD TABELA TOPICOS
SQL_INSERT_TOPICO = "INSERT INTO `plataforma`.`topicos` (`conteudo`, `data_publicacao`, `cursos_id`) VALUES ( '%s', '{:%Y-%m-%d %H:%M}', '%d');"
SQL_SELECT_TOPICO = "SELECT `topicos`.`id`, `topicos`.`conteudo`, `topicos`.`data_publicacao`, `topicos`.`cursos_id` FROM `plataforma`.`topicos` where id = '%d';"
#CRUD TABELA INSTRUTORES
SQL_CREATE_INST = "INSERT INTO INSTRUTORES (NOME) VALUES ('%s')"


'''nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa{jogo.id}.jpg')'''

'''
class DbInit:
    def __init__(self, db):
        self.__db = db

class InstrutorDao(DbInit):
    def __init__(self, db):
        self.__db = db
    def create(self, instrutores):
        cursor = self.__db.connection.cursor()
    if(instrutores.id):
        print("INSTRUTOR EXISTENTE")
    else:
        cursor.execute(SQL_CREATE_INST,instrutores.nome, instrutores.foto)
    self.__db.connection.commit()'''