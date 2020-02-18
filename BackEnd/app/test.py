# -*- coding: utf-8 -*-

import json
from flask import Blueprint,request

search_info = Blueprint("search", __name__)


@search_info.route("/search_get", methods=["GET"])
def index():
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@search_info.route("/search_post", methods=["POST"])
def search_hello():
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh
