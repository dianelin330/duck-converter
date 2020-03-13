#!flask/bin/python
from flask import Flask, jsonify, abort, \
	request, flash, make_response, request, \
	current_app, send_from_directory, render_template

from wtforms import Form, TextField, TextAreaField, \
	validators, StringField, SubmitField

import os
import emoji
from datetime import timedelta
from functools import update_wrapper

import converter as c

import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j3kd93wks9202kedjdjemejk3i393409'
app.config["JSON_SORT_KEYS"] = False

con = c.Converter()


class ReusableForm(Form):
    # name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            units=request.form['units']
    
        con = c.Converter()
        finalunits = con.convert_mass(float(units), 'lb')

        if form.validate():
            # Save the comment here.
            flash('Processing')
        else:
            flash('All the form fields are required. ')
    
        return render_template('hello.html', finalunits=finalunits)



def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/healthcheck/', methods=['GET'])
@crossdomain(origin='*')
def get_healthcheck():
    return emoji.emojize(':thumbs_up: :duck:')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path,
        'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)