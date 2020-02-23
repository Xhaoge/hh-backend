# -*- coding: utf-8 -*-
import os
import json
from flask import Blueprint, request
from .utils import getRandomStr, getResponseReturn
from . import app
# from . import db

pic_handle = Blueprint('pictures',__name__)


@pic_handle.route("/hh/pic_add", methods=["POST"])
def pic_add():
    data = {}
    try:
        # 获取图片
        file_add = request.files["file"]
        # 获取图片名
        file_name = file_add.filename
        print("file_name: ",file_name)
    except Exception:
        return getResponseReturn(202)
    # 文件保存地址；
    file_path = app.config.get("PICS_STORAGE_ADDRESS")
    traceId = getRandomStr(4) + "-" + getRandomStr(4) + ".jpg"
    if file_add:
        # 地址拼接
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_paths = os.path.join(file_path, traceId)
        print("file_paths: ",file_paths)
        # 保存接收的图片到桌面
        file_add.save(file_paths)
    data["picId"] = traceId
    data["fileHost"] = file_path
    resultRes = getResponseReturn(200)
    resultRes["data"] = data
    return json.dumps(resultRes, ensure_ascii=False)


@pic_handle.route("/hh/pic_delete", methods=["POST"])
def pic_del():
    param = request.json
    print(type(param))
    print("username: ",param["username"])
    hh = "search for yourself " + param["username"]
    return hh
