from flask import Flask

app = Flask(__name__)


from config import conn, chave

from flask_mysqldb import MySQL

db = MySQL(app)

cursor = conn.cursor()

from flask_login import LoginManager, UserMixin, login_required,login_user

login_manager = LoginManager(app)

from plataforma.controllers import default

app.secret_key = chave

app.run(debug = True)

