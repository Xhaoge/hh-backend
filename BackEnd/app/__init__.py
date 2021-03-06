
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

# import json
# from datetime import datetime
# from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode='utf8')
from . import userModel, roomModel, views
