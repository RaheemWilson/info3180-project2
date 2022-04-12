from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    #Feilds for login form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

class RegistrationForm(FlaskForm):
    #Feilds for registration form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    fullname = StringField('Fullname', validators=[InputRequired()])
    email = EmailField('Email', [validators.InputRequired(), validators.Email()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('UploadPhoto', validators=[FileRequired(), FileAllowed(['jpg','png'])])


