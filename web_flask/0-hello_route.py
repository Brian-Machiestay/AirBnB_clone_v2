#!/usr/bin/python3
""" starts a flask web application"""
from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_world():
    """returns hbnb message"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
