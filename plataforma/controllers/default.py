# DELETAR MEU USER E COMENTAR

from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from plataforma import app, cursor, conn, MySQL
from plataforma.models import codigos

""" password = generate_password_hash("admin")

cursor.execute("INSERT INTO `plataforma`.`instrutores` ( `nome`, `foto`, `senha`) VALUES ( 'admin', 'admin', '{0}');".foha rmat(password))
conn.commit()
print(password) """



# Rota de index, seria bom criar uma página simples pra ela

@app.route("/")
def index():
    cursor.execute('select id, titulo, descricao, duracao from cursos;')
    cursos = cursor.fetchall()
    i = 0
    # for item in cursos:
    #
    #     cursosF.
    #     print(cursosF)
    cursosF = {
        cursos
    }
    return render_template('index.html', cursos=cursosF)


# rota das aulas
@app.route("/video", methods=["POST", "GET"])
def video():
    cursor.execute(codigos['SQL_BUSCA_VIDEO'].format(5))
    cursor.execute(codigos['SQL_BUSCA_VIDEO'].format(5))
    videos = cursor.fetchone()
    videos = {
        'id': videos[0],
        'conteudo': videos[3]
    }
    print(videos['conteudo'])
    return render_template('conteudo.html', videos=videos)


# Rota dos cursos,so teste por enquanto
@app.route('/courses')
def courses():
    if False:  # 'user_logado' not in session or session['admin_logado'] == None:
        return redirect("/login")
    else:
        # criar o sql e pensar na lógica
        cursor.execute('select * from cursos join topicos on cursos.id = topicos.cursos_id where cursos.id = 1;')
        courses = cursor.fetchall()
        print(courses)
        courses = {
            'id': courses[0]
            # 'titulo': courses[1],
            # 'descricao':courses[2],
        }
    return render_template('courses.html', courses=courses, )  # topicos=topicos)


# Rota das informações dos cursos para se inscrever
@app.route('/courses/<int:id>')
def coursesId():
    return render_template('courses.html')


# Rota dos cursos do usuário
@app.route('/myCourses')
def myCourses():
    fiz = True
    return render_template('meusCursos.html', fiz=fiz)


# ROTA DE LOGIN DE USUÁRIOS COMUNS
@app.route("/login", methods=["POST", "GET"])
def login():
    try:
        if request.method == 'POST':
            user = request.form["email"]
            password_form = request.form["password"]
            # falta exceção se não existir
            cursor.execute(codigos['SQL_BUSCA_USER'].format(user))
            user = cursor.fetchone()
            print(user)
            if (user == None):
                pass
            else:
                if not check_password_hash(user[3], password_form):
                    print('errou')
                    print(user[3])
                    print(password_form)
                    flash('Senha ou usuário errados! Tente novamente')
                    return (redirect('/login'))

                else:
                    session['user_logado'] = user
                    flash(user + ' logou com sucesso!')
                    return (redirect('/myCourses'))
    except:
        flash('Esse usuário não existe. Crie uma conta ')
        return (redirect('/login'))
    return render_template('login.html')


# ROTA DE CRIAÇÃO DE USUÁRIO
@app.route("/newUser", methods=["POST", "GET"])
def newUser():
    try:
        if request.method == 'POST':
            foto = 'null'
            name = request.form["name"]
            email = request.form["email"]
            # verificar email repetido
            password = request.form["password"]
            confirm = request.form["confirm"]
            print(name, email, password, confirm)
            if password == confirm:
                password = generate_password_hash(password)
                cursor.execute(codigos['SQL_CREATE_USER'].format(name, email, password, foto))
                conn.commit()
                return (url_for('login'))
            else:
                flash('As senhas estão diferentes!')
    except MySQL.__hash__(TypeError):
        flash('As senhas estão diferentes!')
        return "Algo deu errado"

    return render_template('criar-conta.html')


@app.route('/teste')
def teste():
    return render_template('base.html')


# ROTA DE LOGIN DE USUÁRIOS GERENCIADORES
@app.route("/loginAdmin", methods=["POST", "GET"])
def loginAdmin():
    if request.method == 'POST':
        user = request.form["user"]
        password_form = request.form["password"]
        # falta exceção se não existir
        cursor.execute(codigos['SQL_BUSCA_ADMIN'].format(user))
        admin = cursor.fetchone()
        if not check_password_hash(admin[3], password_form):
            print('errou')
            print(admin[3])
            print(password_form)
            flash('Senha ou usuário errados! Tente novamente')
            return (redirect('/loginAdmin'))

        else:
            session['admin_logado'] = user
            flash(user + ' logou com sucesso!')
            return (redirect('/loginAdmin'))
    return render_template('loginAdmin.html')


@app.route("/logoutAdmin")
def logoutAdmin():
    session['admin_logado'] = None
    flash("USUÁRIO DESLOGADO")
    return redirect('/login')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
