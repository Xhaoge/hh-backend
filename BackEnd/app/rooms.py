# -*- coding: utf-8 -*-
import time
import json
from flask import Blueprint, request
# from . import db
from .roomModel import *
from .utils import getResponseReturn,makeResponseScheme

rooms_mod = Blueprint('rooms',__name__)

# 查询所有房源
@rooms_mod.route("/hh/room_index")
def rooms_index():
    roomAll = getRoomList()
    print("roomAll:",roomAll)
    print(type(roomAll))
    if len(roomAll) == 0 or not isinstance(roomAll,list):
        return getResponseReturn(0)
    res = makeResponseScheme(resStatus=200, msg="读取所有房源成功",data=roomAll)
    return res

# 添加一个房源
@rooms_mod.route("/hh/room_add", methods=["POST"])
def rooms_add():
    param = request.json
    newRoom = roomAddParamHandle(param)
    if not isinstance(newRoom, Room):
        return getResponseReturn(202)
    respAddRoomId = addRoom(newRoom)
    if not isinstance(respAddRoomId, int):
        return getResponseReturn(1026)
    res = makeResponseScheme(resStatus=200, msg="房源创建成功",data={"roomId":respAddRoomId})
    return res
    
def roomAddParamHandle(d):
    roomNew = Room()
    try:
        roomNew.title = d["title"]
        roomNew.creatorId = d["creatorId"]
        roomNew.picIdList = str(d["picIdList"])
        roomNew.position = str(d["position"])
        roomNew.address = d["address"]
        roomNew.roomType = str(d["roomType"])
        roomNew.isElevator = True if d["isElevator"] == 1 else False
        roomNew.price = d["price"]
        roomNew.nearSubway = d["nearSubway"]
        roomNew.payType = d["payType"]
        roomNew.area = d["area"]
        roomNew.releaseTime = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        roomNew.floor = d["floor"]
        roomNew.plot = d["plot"]
        roomNew.supporting = str(d["supporting"])
        roomNew.contactPhone = d["contactPhone"]
        roomNew.contactWx = d["contactWx"]
        roomNew.description = d["description"]
    except Exception as e:
        return e
    return roomNew


# 查看某一房源具体信息
@rooms_mod.route("/hh/room_get", methods=["POST"])
def rooms_get():
    param = request.json
    roomId = param["roomId"]
    roomDict = getRoomByIdResponse(roomId)
    print("roomDict: ",type(roomDict))
    if not isinstance(roomDict,dict):
        return getResponseReturn(404)
    res = makeResponseScheme(resStatus=200, msg="查询房源成功",data=roomDict)
    return res


# 删除房源
@rooms_mod.route("/hh/room_delete", methods=["POST"])
def rooms_delete():
    param = request.json
    roomId = param["roomId"]
    resCode = deleteRoomById(roomId)
    if resCode == 200:
        res = makeResponseScheme(resStatus=200, msg="删除房源成功")
    elif resCode == 500:
        res = makeResponseScheme(resStatus=500, msg="删除房源失败")
    else:
        res = makeResponseScheme(resStatus=404, msg="所删除房源查找失败")
    return res


# 更新房源
@rooms_mod.route("/hh/room_update", methods=["POST"])
def rooms_update():
    param = request.json
    resCode = roomUpdate(param)
    if resCode == 200:
        res = makeResponseScheme(resStatus=200, msg="更新房源数据成功")
    elif resCode == 404:
        res = makeResponseScheme(resStatus=404, msg="所更新房源查找失败")
    else:
        res = makeResponseScheme(resStatus=500, msg="内部处理数据错误")
    return res