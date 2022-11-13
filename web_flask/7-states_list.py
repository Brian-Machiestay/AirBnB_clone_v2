#!/usr/bin/python3
"""web flask application list states tables"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask('web_flask')

@app.teardown_appcontext
def destroy_all(f):
    """destroys this app context"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def render_states():
    """render the states from dbstorage"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
