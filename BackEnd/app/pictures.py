# -*- coding: utf-8 -*-
import os
import json
from flask import Blueprint, request
from .utils import getRandomStr
# from . import db

pic_handle = Blueprint('pictures',__name__)

@pic_handle.route("/hh/pic_add", methods=["POST"])
def pic_add():
    print("进来上传图片啊.....")
    # 获取图片
    file_add = request.files["file"]
    # 获取图片名
    file_name = file_add.filename
    print("file_name: ",file_name)
    # 文件保存地址；先保存在桌面测试
    file_path = r'C:/Users/Administrator/Desktop/'
    traceId = getRandomStr(4) + "-" + getRandomStr(4)
    print("traceId: ", traceId)
    if file_add:
        # 地址拼接
        file_paths = os.path.join(file_path, traceId+ ".jpg")
        print("file_paths: ",file_paths)
        # 保存接收的图片到桌面
        file_add.save(file_paths)
    
    dict1 = {1:"hello,hh"}
    json1 = json.dumps(dict1, ensure_ascii=False)
    return json1


@pic_handle.route("/hh/pic_del", methods=["POST"])
def pic_del():
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh


@pic_handle.route("/hh/pic_update", methods=["POST"])
def pic_upd():
    param = request.json
    return param
