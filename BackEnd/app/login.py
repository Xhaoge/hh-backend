# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
# from . import db
from .models import getUsers

login_mod = Blueprint('login',__name__)

@login_mod.route("/login", methods=["GET"])
def index():
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@login_mod.route("/register", methods=["POST"])
def search_hello():
    rr = getUsers()
    print(rr)
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh
