from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
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

class ExploreForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = IntegerField('Model', validators=[DataRequired()])

class AddNewCarForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = IntegerField('Year', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    cartype = StringField('Car Type', validators=[InputRequired()])
    transmission = StringField('Transmission', validators=[InputRequired()])
    description =  TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('UploadPhoto', validators=[FileRequired(), FileAllowed(['jpg','png'])])
    