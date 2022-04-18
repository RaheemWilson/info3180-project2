"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from tabnanny import check
from app import app, db, login_manager
from click import password_option
from flask import request, jsonify, send_file, session
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegistrationForm, ExploreForm, AddNewCarForm
from app.models import Users, Cars, Favourites
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from functools import wraps
import os
import jwt

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register', methods = ['POST'])
def register():
    try:
        form = RegistrationForm()
        if request.method == "POST" and form.validate_on_submit():
            
            check_username = Users.query.filter_by(username=form.username.data).first()
            check_email = Users.query.filter_by(email=form.email.data).first()
            
            if check_username is not None or check_email is not None:
                return jsonify({
                    "errors": "User is in the system"
                }), 401


            username = form.username.data
            password = form.password.data
            fullname =  form.fullname.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            upload = form.photo.data
            filename = secure_filename(upload.filename)
            date_joined = datetime.now()
            
            user = Users(username, password, fullname, email, location, biography, filename, date_joined)
            db.session.add(user)
            db.session.commit()
            upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return jsonify({
                'id': user.id,
                'username': username,
                'name': fullname,
                'photo': filename,
                'email': email,
                'location': location,
                'biography': biography,
                'date_joined': user.date_joined
            }), 201
        return jsonify(errors=form_errors(form)), 401
    except:
        return jsonify({ "errors": form.errors}), 500


@app.route("/api/auth/login", methods=["POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data

        # This queries database for a user based on the username
        # and password submitted.
        user = Users.query.filter_by(username=username).first()

        # Compares the submited password and username to the hash password and
        # username in the database.
        if user is not None and check_password_hash(user.password, password):
            session['logged_in'] = True

            #Creates the token for the user currently logging in
            payload = {
                'sub': user.id, # subject, usually a unique identifier
                'user': username,
                'iat': datetime.utcnow(),# issued at time
                'exp': datetime.utcnow() + timedelta(hours=2) # expiration time
            }

            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            login_user(user)

            return jsonify(
                { 
                    "token": token , 
                    "message": "Login Successfully",
                    "id": user.id
                }), 200
    
    return jsonify(errors=form_errors(form)), 401

##
# GET ALL CARS
##
@app.route('/api/cars', methods=['GET'])
def getCars():
    try:
        if request.method == "GET":
            #Retrieve data from the database
            cars = db.session.query(Cars).all()
            data = []
            
            for car in cars:
                data.append ({
                    'id': car.id,
                    'description': car.description,
                    'make': car.make,
                    'model': car.model,
                    'colour': car.colour,
                    'year': car.year,
                    'transmission': car.transmission,
                    'type': car.car_type,
                    'price': car.price,
                    'photo': car.photo,
                    'user_id': car.user_id
                })
            return jsonify (data=data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401


@app.route('/api/cars', methods=['POST'])
def setCars():
    form = AddNewCarForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            
            ##adds information from the form to the databse
            make = form.make.data
            model = form.model.data
            colour = form.colour.data
            year = form.year.data
            price = form.price.data
            car_type = form.cartype.data
            transmission = form.transmission.data
            description = form.description.data
            upload = form.photo.data
            filename = secure_filename(upload.filename)

            """
             Note! not sure if i should save the user id in a session 
             after a succesful login so it can be used to fill in the
             user_id parameter in the function call below
            """
            cars = Cars(description, make, model, colour, year, transmission, car_type, price, filename, user_id)
            db.session.add(cars)
            db.session.commit()
            ##
            
            # Sends photo file name to upload folder
            upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
            return jsonify({
                   "description": description,
                   "year": year,
                   "make": make,
                   "model": model,
                   "colour": colour,
                   "transmission": transmission,
                   "type": car_type,
                   "price": price,
                   "photo": filename,
                   "user_id": 1
               }), 201
    except:
        return jsonify({ "errors": "Request Failed"}), 500
    
##
# GET A SPECIFIC CAR
##
@app.route('/api/cars/{car_id}', methods =['GET'])
def getCar(car_id):
    try:
        if request.method == 'GET':
            #Searches car db to find a car that matched the id in the parameter
            car = Cars.query.filter_by(id = car_id).first()
            data = [{
                'id': car.id,
                'description': car.description,
                'make': car.make,
                'model': car.model,
                'colour': car.colour,
                'year': car.year,
                'transmission': car.transmission,
                'type': car.car_type,
                'price': car.price,
                'photo': car.photo,
                'user_id': car.user_id
            }]
            return jsonify(data=data), 200
    except:
        return jsonify({"errors": "Request Failed"}), 401
    
    
    


@app.route('/api/cars/{car_id}/favourite', methods=['Post'])
def favCar(car_id):
    try:
       if request.method == 'Post':
           #Searches car db to find a car that matches the id in the parameter 
           match = Cars.query.filter_by(id=car_id).first()
           #Adds the matched car's id and user id to favourites db
           favourite = Favourites(match.id, match.user_id)
           db.session.add(favourite)
           db.session.commit()
   
           return jsonify({
                   "message": "Car Succesfully Favourited",
                   "car_id": match.id
               })
    except:
        return jsonify({ "errors": "Request Failed"}), 500





@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")