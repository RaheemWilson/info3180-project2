from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    #Feilds for login form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Email()])

class RegistrationForm(FlaskForm):
    #Feilds for registration form
    fullname = StringField('Fullname', validators=[InputRequired()])
    email = EmailField('Email address', [validators.InputRequired(), validators.Email()])
    location = StringField('Fullname', validators=[InputRequired()])
    biography = TextAreaField('Description', validators=[DataRequired()])
    upload_photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'])])


    