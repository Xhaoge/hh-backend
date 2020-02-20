#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from flask import Flask,render_template,jsonify,request,g, url_for,abort
from BackEnd.app.models import *
from BackEnd.app.rooms import rooms_mod
from BackEnd.app.login import login_mod
from BackEnd.app.pictures import pic_handle

# 注册蓝图
app.register_blueprint(rooms_mod)
app.register_blueprint(login_mod)
app.register_blueprint(pic_handle)

@app.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试跨域 '''
    return 'success'
