"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from click import password_option
from flask import request, jsonify, send_file, session, render_template, make_response
from app.forms import LoginForm, RegistrationForm, ExploreForm, AddNewCarForm
from app.models import Users, Cars, Favourites
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from functools import wraps
import os
import jwt


# Creates a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None) 
    
    # If statements check if token exist or if it has been compromised
    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated




###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register', methods = ['POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        id = Users.query.filter_by(id = id).first()
        username = form.username.data
        password = form.password.data
        fullname =  form.fullname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        upload = form.photo.data
        filename = secure_filename(upload.filename)
        date_joined = datetime.now()
        
        user = Users (username, password, fullname, email, location, biography, filename, date_joined)
        db.session.add(user)
        db.session.commit()
        upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return jsonify({
                "id": id,
                "name": fullname,
                "photo": upload,
                "email": email,
                "location": location,
                "biography": biography,
                "date_joined": date_joined
                
            })
    return jsonify(errors=form_errors(form))


@app.route("/api/auth/login", methods=["POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
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
                'user': form.username.data,
                'iat': datetime.utcnow(),# issued at time
                'expiration': datetime.utcnow() + timedelta(minutes=2) # expiration time
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

            #i guess this returns the token by using jwt.decode \-(^-^)-/ 
            return jsonify(error=None, data={'token':jwt.decode(token,  app.config['SECRET_KEY'], algorithms=["HS256"])} , message="Token Generated")
        else:
            return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm:"Authentication Failed!"'})



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