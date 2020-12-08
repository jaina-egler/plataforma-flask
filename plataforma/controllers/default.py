'''DELETAR MEU USER E COMENTARS'''

from flask import render_template, request, redirect, url_for

from plataforma import app, login_manager, login_required,login_user

from plataforma.models.forms import UserLogin, UserCreate

from plataforma.models import AdminUsers

from werkzeug.security import generate_password_hash,check_password_hash

#Rota de index, seria bom criar uma página simples pra ela
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST","GET"])
def login():
    user.email = request.form["email"]
    user.password = request.form["password"]
    return render_template('login.html', form=form)

@app.route("/newUser", methods=["POST","GET"])
def newUser():
    if request.method == 'POST':
        user = User()
        user.name = request.form["name"]
        user.email = request.form["email"]
        #verificar email repetido
        password = request.form["password"]
        confirm = request.form["password2"]
        if(password == confirm):
            user.password = generate_password_hash(request.form["password"])
            '''db.session.add(user)
            db.session.commit() VER INSERINDO USUÁRIOS DO CURSO2'''
            return(url_for('login'))
        else:
            #LOGICA PARA MANDAR ALERT
            pass
    return render_template('criar-conta.html')

#PAGINA PARA APENAS ADMINS VEREM, NECESSITA MELHORIAS
@login_manager.user_loader
def current_user(user_id):
    return AdminUser.query.get(user_id)
@login_required
@app.route('/adminLogin', methods=['GET','POST'])
def adminLogin():
    if request.method == "POST":
        user = request.form["user"]
        senha = request.form["senha"]
        AdminUsers.query.filter_by(nameAdmin=user).first()
    
    return render_template('adminLogin.html')

