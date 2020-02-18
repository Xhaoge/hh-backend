
import json
from flask import Flask, render_template, request
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
from modules.model import User
import config

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_object(config)

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/hh' 

# 用于连接数据库，得到SQLAlchemy对象
db = SQLAlchemy(app)

# 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 

@app.route('/')
def index():
    user = User()
    print(user)
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1

@app.route("/search",methods=["POST"])
def regis():
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh


if __name__ == "__main__":
    print("Hello World.....")
    print("I Believe I Can Fly....")
    db.create_all()
    app.run(port=8080, debug=True)