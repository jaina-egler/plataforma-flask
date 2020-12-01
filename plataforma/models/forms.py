from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class UserLogin(FlaskForm):
    username=StringField('usuario',validators=[DataRequired()])
    password=PasswordField('senha',validators=[DataRequired()])

class UserCreate(FlaskForm):
    s
    password = PasswordField(min=8, max= 30, ,[InputRequired(), EqualTo('confirm', message='As senhas devem ser iguais!')])
    confirm  = PasswordField()