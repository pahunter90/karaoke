"""
Creates a map and shows were local pools are...
local to Eugene, OR
"""

import flask
import config
import logging


#Globals
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
app.access_token = CONFIG.ACCESS_TOKEN


#Pages
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    flask.g.access_token = app.access_token
    return flask.render_template('gmap.html')

@app.route("/_get_places")
def _get_places():
    places = open(CONFIG.INPUT_FILE, "r")
    locations = []
    for line in iter(places):
        locations.append(line)
    result = {"locations": locations}
    return flask.jsonify(result=result)


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
