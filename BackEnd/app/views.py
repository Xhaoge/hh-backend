#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask,render_template,jsonify,request,g, url_for,abort,Blueprint
from app.models import *
from app.test import search_info


app.register_blueprint(search_info)


@app.route('/test', methods=['GET', 'POST'])
def test():
    ''' 这个API用来测试 '''
    return 'success'