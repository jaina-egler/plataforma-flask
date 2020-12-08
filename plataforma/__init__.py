from flask import Flask

app = Flask(__name__)

import config


from flask_sqlalchemy import SQLAlchemy


from flask_login import LoginManager, UserMixin, login_required,login_user

login_manager = LoginManager(app)

from plataforma.controllers import default

from plataforma.models import AdminUsers


