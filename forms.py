from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, PasswordField, SubmitField, 
                     BooleanField, TextAreaField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date, datetime


now = datetime.now()
order = now.strftime('%y:%m:%d:%H:%M:%S')

class New_Item(FlaskForm):
    product_name = StringField('Entrer le nom du produit', validators = [DataRequired(), Length(min = 3)])
    product_price = StringField('Entrer le prix du produit', validators = [DataRequired(),])
    description = TextAreaField('Description et caracteristiques du produit',validators = [DataRequired()])
    pictures = FileField('Choisir les photos du produit')
    order = order
    submit = SubmitField('Mettre en ligne')
    
class Login(FlaskForm):
    email = StringField('Entrez votre email', validators = [DataRequired(), Email(),])
    password = StringField('Entrez votre email', validators = [DataRequired(), Email(),])
    password = PasswordField('Entrez votre mot de passe', validators = [DataRequired(),Length(min = 8),])
    submit = SubmitField('Se connecter')
    
class Register(FlaskForm):
    email = StringField('Entrez votre email', validators = [DataRequired(),Email()])
    password = PasswordField('Entrez un mot de passe', validators = [DataRequired(),Length(min = 8)])
    confirm_password = PasswordField('Confirmez votre mot de passe',
                                     validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Créez un compte')