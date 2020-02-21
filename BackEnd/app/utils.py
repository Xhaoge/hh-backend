# 公共函数定义

import random
from .roomModel import Room
# from datetime import datetime

# 申明基本全局响应码
def getResponseReturn(code):
    if code == 200:
        return {"code":200, "msg":"Success"}
    elif code == 202:
        return {"code":202, "msg":"Request Param Error"}
    elif code == 404:
        return {"code":404, "msg":"Not Found"}
    elif code == 500:
        return {"code":500, "msg":"Intenal Serve Error"}
    else:
        return {"code":666, "msg":"Big Trouble"}


# 随机组合一个str返回；
def getRandomStr(num):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letterA = ['A','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    lettera = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    makeAll = number + letterA + lettera
    rr = random.sample(makeAll,num)
    resultStr = "".join(rr)
    return resultStr


def roomAddParamHandle(d):
    roomNew = Room()
    try:
        roomNew.title = d["title"]
        roomNew.creatorId = d["creatorId"]
        roomNew.picIdList = str(d["picIdList"])
        print(type(d),type(d["picIdList"]))
        roomNew.position = str(d["position"])
        roomNew.address = d["address"]
        roomNew.roomType = str(d["roomType"])
        # roomNew.isElevator = d["isElevator"]
        roomNew.price = d["price"]
        roomNew.nearSubway = d["nearSubway"]
        roomNew.payType = d["payType"]
        roomNew.area = d["area"]
        # roomNew.releaseTime = datetime.date
        roomNew.floor = d["floor"]
        roomNew.plot = d["plot"]
        roomNew.supporting = str(d["supporting"])
        roomNew.contactPhone = d["contactPhone"]
        roomNew.contactWx = d["contactWx"]
        roomNew.description = d["description"]
    except Exception as e:
        return e
    return roomNew