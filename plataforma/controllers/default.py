from flask import render_template

from plataforma import app

from plataforma.models.forms import UserLogin

@app.route("/")
@app.route("/login", methods=["POST","GET"])
def login():
    form = UserLogin()
    return render_template('login.html', form=form)

@app.route("/createAccount", methods=["POST","GET"])
def createAccount():
    form = UserCreate()
    return render_template('criar-conta.html', form=form)

'''@app.route("/ola", defaults = {'name': None})
@app.route("/ola/user")
def ola(user):
    if user:
        return "Oie %s!" % user
    else:
        return("oie")'''