from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_httpauth import HTTPBasicAuth
import json
# from . import models,views
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app, use_native_unicode='utf8')

# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     if isinstance(data, datetime):
#                         data = data.strftime('%Y-%m-%d %H:%M:%S')
#                     json.dumps(data) # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             # a json-encodable dict
#             return fields
#         return json.JSONEncoder.default(self, obj)

def convert_to_json_string(data):
    return json.dumps(data, ensure_ascii=False, cls=AlchemyEncoder)

