#!/usr/bin/python3
"""web flask application list states tables"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask('web_flask')


@app.teardown_appcontext
def destroy_all(f):
    """destroys this app context"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def render_filters():
    """render the states from dbstorage"""
    amen = storage.all(Amenity)
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states, amen=amen)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
