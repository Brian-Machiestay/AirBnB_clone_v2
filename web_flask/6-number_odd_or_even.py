#!/usr/bin/python3
""" starts a flask web application"""
from flask import Flask
from flask import render_template
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_world():
    """returns hbnb message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """view function for /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """dynamic view function for /c/text"""
    modified_text = text.replace("_", " ")
    return "C {}".format(modified_text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """dynamic view function for /python/(<text>)"""
    modified_text = text.replace("_", " ")
    return "Python {}".format(modified_text)


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_a_number(n):
    """dynamic endpoint with type checking"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_template_n(n):
    """render the template only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ renders a template if n is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
