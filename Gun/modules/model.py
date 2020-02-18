# !/usr/bin/env python
# -*- coding:utf-8 -*-  

from flask_sqlalchemy import SQLAlchemy
from . import app
from . import config
import pymysql

pymysql.install_as_MySQLdb()
app.config.from_object(config)

db = SQLAlchemy(app)

# 创建user model
class User(db.Model):

    __tablename__ = 'Users' #（设置表名）
    id = db.Column(db.Integer, primary_key=True) #（设置主键）
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

db.create_all()
