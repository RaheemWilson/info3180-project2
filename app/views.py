"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
import json
import os
import jwt
from sqlalchemy import true
from app import app, db, login_manager
from flask import request, jsonify, session, send_file
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegistrationForm, AddNewCarForm
from app.middleware import requires_auth
from app.models import Users, Cars, Favourites
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


###
# Routing for your application.
###
@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return Users.query.get(user_id)

@app.route('/')
def index():
    return send_file(os.path.join('../dist/', 'index.html'))

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

@app.route('/api/auth/logout', methods=["POST"])
@login_required
@requires_auth
def logout():
    logout_user()

    return jsonify({
        "message": "Log out successful"
    }), 200

##
# GET ALL CARS
##
@app.route('/api/cars', methods=['GET'])
@login_required
@requires_auth
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
                    'car_type': car.car_type,
                    'price': car.price,
                    'photo': car.photo,
                    'user_id': car.user_id
                })
            return jsonify (data=data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401


@app.route('/api/cars', methods=['POST'])
@login_required
@requires_auth
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
            user_id = form.user_id.data

            cars = Cars(description, make, model, colour, year, transmission, car_type, price, filename, user_id)
            db.session.add(cars)
            db.session.commit()
            ##
            
            # Sends photo file name to upload folder
            upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
            return jsonify({
                    "id": cars.id,
                   "description": description,
                   "year": year,
                   "make": make,
                   "model": model,
                   "colour": colour,
                   "transmission": transmission,
                   "car_type": car_type,
                   "price": price,
                   "photo": filename,
                   "user_id": user_id
               }), 201
        return jsonify(errors=form_errors(form)), 401
    except Exception as e:
        return jsonify({ "errors": e}), 500
    
##
# GET A SPECIFIC CAR
##
@app.route('/api/cars/<car_id>', methods =['GET'])
@login_required
@requires_auth
def getCar(car_id):
    try:
        if request.method == 'GET':
            #Searches car db to find a car that matched the id in the parameter
            car = Cars.query.get(car_id)

            if car.user_id == current_user.id:
                favourite = Favourites.query.filter_by(user_id=current_user.id, car_id=car_id).first()

                if favourite is not None:
                    is_favourited = True
                else:
                    is_favourited = False

            data = {
                'id': car.id,
                'description': car.description,
                'make': car.make,
                'model': car.model,
                'colour': car.colour,
                'year': car.year,
                'transmission': car.transmission,
                'car_type': car.car_type,
                'price': car.price,
                'photo': car.photo,
                'user_id': car.user_id,
                'favourited': is_favourited
            }
            return jsonify(data), 200
    except:
        return jsonify({"errors": "Request Failed"}), 401
    
    
    


@app.route('/api/cars/<car_id>/favourite', methods=['POST'])
@login_required
@requires_auth
def favCar(car_id):
    try:
       if request.method == 'POST':
        #    user_id = request.json['user_id']
            data = request.get_json()
            user_id = data.get('user_id', '')
            #Adds the matched car's id and user id to favourites db

            favourite = Favourites(car_id, user_id)
            db.session.add(favourite)
            db.session.commit()

            return jsonify({
                    "message": "Car Succesfully Favourited",
                   "car_id": car_id
        })
    except Exception as e:
        return jsonify({ "errors": e}), 500



###Search For Cars By Make Or Model###
@app.route('/api/search', methods=['GET'])
@login_required
@requires_auth
def searchCar():
    make_ex = request.args.get('make')
    model_ex = request.args.get('model')
    try:
        if request.method == 'GET':
            cars = Cars.query.filter((Cars.make.ilike("%" +make_ex + "%")) , (Cars.model.ilike("%" + model_ex + "%"))).all()
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
                    'car_type': car.car_type,
                    'price': car.price,
                    'photo': car.photo,
                    'user_id': car.user_id
                })
            return jsonify(data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401

"""
    Route GET /api/users/<user_id> 
    Returns details for the user with the user_id
"""
@app.route('/api/users/<user_id>', methods=['GET'])
@login_required
@requires_auth
def getUserDetail(user_id):
    try:
        if request.method == 'GET':
            user = Users.query.get(user_id)

            data = {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'photo': user.photo,
                'email': user.email,
                'location': user.location,
                'biography': user.biography,
                'date_joined': user.date_joined
            }
            return jsonify(data), 200
    except Exception as e:
        return jsonify({"errors": e}), 401


###GET CARS FAVOURITED BY A USER###
@app.route('/api/users/<user_id>/favourites', methods=['GET'])
@login_required
@requires_auth
def userFavCar(user_id):
    try:
        if request.method == 'GET':
            favs = Favourites.query.filter_by(user_id=user_id).all()
            data = []
            for fav in favs:
                car = Cars.query.get(fav.car_id)
                data.append ({
                    'id': car.id,
                    'description': car.description,
                    'make': car.make,
                    'model': car.model,
                    'colour': car.colour,
                    'year': car.year,
                    'transmission': car.transmission,
                    'car_type': car.car_type,
                    'price': car.price,
                    'photo': car.photo,
                    'user_id': car.user_id
                })
            return jsonify(data), 200
    except:
        return jsonify({"errors": "Request Failed"}), 401

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