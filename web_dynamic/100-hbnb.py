#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid;

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    this method calls .close() (i.e. .remove()) on
    the current SQL
    """
    storage.close()


@app.route('/100-hbnb')
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states
    """
    state_obj = storage.all('State').values()
    states = dict([state.name, state] for state in state_obj)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users_details = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('100-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=state_obj,
                           amens=amens,
                           places=places,
                           users=users_details)

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
