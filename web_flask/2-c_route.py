#!/usr/bin/python3
""" starts a flask web application"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
