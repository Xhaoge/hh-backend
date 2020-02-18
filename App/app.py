from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    return '<h1>Hello</h1>'

@app.route("/register",methods=["POST"])

def regis():
    return '<h1>Register</h1>'

if __name__ == "__main__":
    app.run(port=8080, debug=True)