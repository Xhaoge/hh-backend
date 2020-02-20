# 公共函数定义

import random

def hello():
    return "hello"


def getRandomStr(num):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letterA = ['A','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    lettera = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    makeAll = number + letterA + lettera
    rr = random.sample(makeAll,num)
    resultStr = "".join(rr)
    print("获取到的str：",resultStr, type(resultStr)) 
    return resultStr