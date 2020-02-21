# 公共函数定义

import random

# 申明基本全局响应码
def getResponseReturn(code):
    if code == 200:
        return {"code":200, "msg":"Success", "data":{}}
    elif code == 202:
        return {"code":202, "msg":"Request Param Error", "data":{}}
    elif code == 404:
        return {"code":404, "msg":"Not Found", "data":{}}
    elif code == 500:
        return {"code":500, "msg":"Intenal Serve Error", "data":{}}
    else:
        return {"code":666, "msg":"Big Trouble", "data":{}}


# 随机组合一个str返回；
def getRandomStr(num):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letterA = ['A','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    lettera = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    makeAll = number + letterA + lettera
    rr = random.sample(makeAll,num)
    resultStr = "".join(rr)
    return resultStr