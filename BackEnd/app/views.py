#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from flask import Flask,render_template,jsonify,request,g, url_for,abort
from .userModel import *
from .rooms import rooms_mod
from .login import login_mod
from .pictures import pic_handle

# 注册蓝图
app.register_blueprint(rooms_mod)
app.register_blueprint(login_mod)
app.register_blueprint(pic_handle)

@app.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'
