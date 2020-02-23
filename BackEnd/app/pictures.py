# -*- coding: utf-8 -*-
import os
import shutil
import json
from flask import Blueprint, request
from .utils import getRandomStr, makeResponseScheme
from . import app
# from . import db

pic_handle = Blueprint('pictures',__name__)


# 添加图片
@pic_handle.route("/hh/pic_add", methods=["POST"])
def pic_add():
    try:
        # 获取图片
        fileAdd = request.files["file"]
        # 获取图片名
        fileName = fileAdd.filename
        print("上传图片的file_name: ",fileName)
    except Exception:
        res = makeResponseScheme(resStatus=202)
    # 文件保存地址；
    filePath = app.config.get("PICS_STORAGE_ADDRESS")
    traceId = getRandomStr(4) + "-" + getRandomStr(4) + ".jpg"
    if fileAdd:
        # 地址拼接
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        fileFullPath = os.path.join(filePath, traceId)
        print("fileFullPath: ",fileFullPath)
        # 保存接收的图片到桌面
        fileAdd.save(fileFullPath)
    res = makeResponseScheme(resStatus=200, msg="上传图片成功", data={"picId":traceId, "fileHOst":filePath})
    return res


# 删除图片
@pic_handle.route("/hh/pic_delete", methods=["POST"])
def pic_del():
    param = request.json
    fileName = param['picId']
    filePath = param['fileHost']
    deleteFile = filePath + "/" + fileName
    print("deleteFile: ", deleteFile)
    try:
        if (os.path.exists(deleteFile)):
            os.remove(deleteFile)
    except Exception:
        res = makeResponseScheme(resStatus=404, msg="图片无法查找")
    # for f in os.listdir(fileDelPath):
    #     fullFile = os.path.join(fileDelPath, f)
    #     newFullFile = os.path.join("D:/static/hh/removedPhotos",f)
    #     shutil.copy(fullFile, newFullFile)
    res = makeResponseScheme(resStatus=200, msg="图片删除成功")
    return res
