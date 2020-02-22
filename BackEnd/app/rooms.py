# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
# from . import db
from .userModel import getUsers
from .roomModel import Room, addRoom
from .utils import roomAddParamHandle,getResponseReturn

rooms_mod = Blueprint('rooms',__name__)

@rooms_mod.route("/hh/room_add", methods=["POST"])
def rooms_add():
    param = request.json
    newRoom = roomAddParamHandle(param)
    if not isinstance(newRoom, Room):
        return getResponseReturn(202)
    respAddRoomId = addRoom(newRoom)
    if not isinstance(respAddRoomId, int):
        return getResponseReturn(1026)
    data = {"roomId":respAddRoomId}
    res = getResponseReturn(200)
    res["msg"] = "房源创建成功"
    res["data"] = data
    return res


@rooms_mod.route("/hh/room_get", methods=["GET"])
def rooms_get():
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@rooms_mod.route("/hh/room_update", methods=["POST"])
def rooms_update():
    rr = getUsers()
    print(rr)
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh


@rooms_mod.route("/hh/room_delete", methods=["POST"])
def rooms_delete():
    pass


