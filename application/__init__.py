from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_googlemaps import GoogleMaps
=======
>>>>>>> 7c31d93d966bbb6df97ad5bd9cf789012ac098ab

application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)
<<<<<<< HEAD
googlemap = GoogleMaps(application)
=======
>>>>>>> 7c31d93d966bbb6df97ad5bd9cf789012ac098ab
