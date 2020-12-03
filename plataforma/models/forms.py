from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class UserLogin(FlaskForm):
    username=StringField('usuario',validators=[DataRequired()])
    password=PasswordField('senha',validators=[DataRequired()])

class UserCreate(FlaskForm):
    password = PasswordField()
    confirm  = PasswordField()