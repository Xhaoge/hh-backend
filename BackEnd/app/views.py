#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from flask import Flask,render_template,jsonify,request,g, url_for,abort
from .models import *
from .rooms import rooms_mod
from .login import login_mod
# from .user_info import user_info

# extensions

app.register_blueprint(rooms_mod)
app.register_blueprint(login_mod)


# @auth.verify_password
# def verify_password(username_or_token, password):
#     # first try to authenticate by token
#     user = User.verify_auth_token(username_or_token)
#     if not user:
#         # try to authenticate with username/password
#         user = User.query.filter_by(id=username_or_token).first()
#         if not user or not user.verify_password(password):
#             return False
#     g.user = user
#     return True

# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token(600)
#     return jsonify({'token': token.decode('ascii'), 'duration': 600})
# @app.route('/api/users/<username>')
# def get_user(username):
#     user = User.query.filter_by(id=username).first()
#     if not user:
#         abort(400)
#     return jsonify({'username': user.username})
# @app.route('/api/resource')
# @auth.login_required
# def get_resource():
#     return jsonify({ 'data': 'Hello, %s!' % g.user.username })



@app.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'
