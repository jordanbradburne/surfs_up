# Set Up the Flask Weather App
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# Set Up Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
# This convention signifies that this is version 1 of our application. 
# This line can be updated to support future versions of the app as well.

# export FLASK_APP=app.py
# flask run
# http://127.0.0.1:5000/