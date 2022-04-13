from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, EmailField
from wtforms.validators import InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    #Fields for login form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

class RegistrationForm(FlaskForm):
    #Fields for registration form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    fullname = StringField('Fullname', validators=[InputRequired()])
    email = EmailField('Email', [validators.InputRequired(), validators.Email()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('UploadPhoto', validators=[FileRequired(), FileAllowed(['jpg','png'])])

    