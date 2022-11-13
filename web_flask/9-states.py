#!/usr/bin/python3
"""web flask application list states tables"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask('web_flask')


@app.teardown_appcontext
def destroy_all(f):
    """destroys this app context"""
    storage.close()


@app.route('/states', strict_slashes=False)
def render_states():
    """render the states from dbstorage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def this_state(id):
    """render the state with this id and its cities"""
    states = storage.all(State)
    state = None
    for st, obj in states.items():
        if obj.id == id:
            state = obj
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
