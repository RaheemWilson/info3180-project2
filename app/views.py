"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from datetime import datetime

from click import password_option
from app import app, db
from flask import render_template, request, jsonify, send_file
from app.forms import *
from app.models import *
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

###
# Routing for your application.
###

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