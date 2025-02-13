from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, EmailField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed



class LoginForm(FlaskForm):
    #Fields for login form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegistrationForm(FlaskForm):
    #Fields for registration form
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    fullname = StringField('Fullname', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('UploadPhoto', validators=[FileRequired(), FileAllowed(['jpg','jpeg', 'png'])])

class AddNewCarForm(FlaskForm):
    #Fields for add new car form
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = IntegerField('Year', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    cartype = StringField('Car Type', validators=[InputRequired()])
    transmission = StringField('Transmission', validators=[InputRequired()])
    description =  TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('UploadPhoto', validators=[FileRequired(), FileAllowed(['jpg','png'])])
    user_id = IntegerField('User Id', validators=[InputRequired()])
     