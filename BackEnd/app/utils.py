# 公共函数定义

import json
import random
from .roomModel import Room


# 申明基本全局响应码
def getResponseReturn(code):
    if code == 200:
        return {"code":code, "msg":"Success"}
    elif code == 202:
        return {"code":code, "msg":"Request Param Error"}
    elif code == 404:
        return {"code":code, "msg":"Not Found"}
    elif code == 500:
        return {"code":code, "msg":"Intenal Serve Error"}
    elif code == 1026:
        return {"code":code, "msg":"insert records Error"}
    elif code == 1012 :
        return {"code":code, "msg":"read records Error"}
    elif code == 1011 :
        return {"code":code, "msg":"delete records Error"}
    else:
        return {"code":code, "msg":"Big Trouble"}


# 定义一个基本返回格式函数
def makeResponseScheme(resStatus=200,msg="",data={}):
    baseRes = getResponseReturn(resStatus)
    if msg != "":
        baseRes["msg"] = msg
    if len(data) != 0:
        baseRes["data"] = data
    baseRes = json.dumps(baseRes, ensure_ascii=False)
    return baseRes


# 随机组合一个str返回；
def getRandomStr(num):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letterA = ['A','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    lettera = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    makeAll = number + letterA + lettera
    rr = random.sample(makeAll,num)
    resultStr = "".join(rr)
    return resultStr

