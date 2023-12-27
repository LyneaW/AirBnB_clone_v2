#!/usr/bin/python3
"""Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ renders a HTML page with a list of states and related cities """
    states = storage.all("State")
    return render_template('8-cities_by_state.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")
