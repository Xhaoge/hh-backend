

import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from modules.model import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/hh' 

#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 

# 用于连接数据库，得到SQLAlchemy对象
db = SQLAlchemy(app, use_native_unicode='utf8')

@app.route('/')

def index():
    user = User()
    dict1 = {1:"hello"}
    print("dict1 type:",type(dict1))
    json1 = json.dumps(dict1, ensure_ascii=False)
    print("json1 type:",type(json1))
    return json1

@app.route("/register",methods=["POST"])

def regis():
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "register: " + param["username"]
    return hh

if __name__ == "__main__":
    print("Hello World.....")
    print("I Believe I Can Fly....")
    app.run(port=8080, debug=True)