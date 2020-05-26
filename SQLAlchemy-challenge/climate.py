import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine('sqlite:///Resources/hawaii.sqlite')

Base = automap_base()
Base.prepare(engine, reflect = True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.Station
session = Session(engine)

#weather app

app = Flask(__name__)


latest_date = (session.query(Measurement.date).order_by(Measurement.date.desc()).first())
latest_date = list(np.ravel(latest_date))[0]
latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')

latest_year = int(dt.datetime.strftime(latest_date, '%Y'))
latest_month = int(dt.datetime.strftime(latest_date, '%m'))
latest_day = int(dt.datetime.strftime(latest_date, '%d'))

oneyear_ago = dt.date(latest_year, latest_month, latest_day) - dt.timedelta(days=365)
oneyear_ago = dt.datetime.strptime(oneyear_ago, '%Y-%m-%d')

@app.route("/")
def home():
    return(
        f"Welcome to Surf's up! Climate API <br/>"
        f"Available routes are: <br/>"

    )



if __name__ == "__main__":
    app.run(debug=True)
