from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

#creating flask object
myObj = Flask(__name__)

myObj.config.from_mapping(
	SECRET_KEY = 'any string works',
	#Location the database will be created 
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False)

db = SQLAlchemy(myObj)

from myApp import routes #, models
