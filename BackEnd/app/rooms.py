# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
# from . import db
from .models import getUsers

rooms_mod = Blueprint('rooms',__name__)

@rooms_mod.route("/get_rooms", methods=["GET"])
def index():
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@rooms_mod.route("/post_rooms", methods=["POST"])
def search_hello():
    rr = getUsers()
    print(rr)
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh