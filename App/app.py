from flask import Flask,render_template, request
import json

app = Flask(__name__)

@app.route('/')

def index():
    dict1 = {1:"hello"}
    print("dict1 type:",type(dict1))
    json1 = json.dumps(dict1, ensure_ascii=False)
    print("json1 type:",type(json1))
    return json1

@app.route("/register",methods=["POST"])

def regis():
    username = request.form.get("username")
    print(username)
    hh = username + "register"
    return hh

if __name__ == "__main__":
    print("Hello World.....")
    print("I Believe I Can Fly....")
    app.run(port=8080, debug=True)