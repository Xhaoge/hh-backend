# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from BackEnd.app import db
from BackEnd.app.models import getUsers,User,addUser
from BackEnd.app import app
import requests, json
login_mod = Blueprint('login',__name__)

@login_mod.route('/login',methods = ["GET","POST"])
def log_in():
    resp = {"code":200,"msg":"操作成功", "data":{}}
    # data = json.loads(request.get_data().decode('utf-8')) #将前端Json数据转为字典
    data={"code":"043A4y6w0LoGYc1eIQ6w0TBN6w0A4y6C"}
    appID = 'wxd20112c596493f06'
    appSecret = 'c156da5ff391cd48fb76c90f99150c24'
    # code = '023gTHKO1Xhcg71tKsJO1s4PKO1gTHKH'
    code = data['code'] if "code" in data else ""
    if not code or len(code) < 1 :
        resp["code"] = 10002
        resp["msg"]="code失效或没有code"
        return json.dump(resp)
    req_params = {
        'appid': appID,
        'secret': appSecret,
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
    response_data = requests.get(wx_login_api, params=req_params)
    data = response_data.json()
    print(data)
    openid = data['openid']
    session_key = data['session_key']
    print(openid,session_key)
    if openid and session_key:
        '''
        在数据库用户表查询（查找得到的OpenID在数据库中是否存在）
        SQLalchemy语句：
        user_info = User.query.filter(User.OpenID == openid).first() 
        '''
        if openid not in getUsers():
            print(1111)
        # if getUsers() is None:
            user_info = User(openId=openid)
            addUser(user_info)
            resp["code"]=200
            resp["msg"]="添加openID成功"
            return json.dumps(resp,ensure_ascii=False)
    return json.dump(resp)

# if __name__== "__main__":)
#     app.run(port = 80,debug=True)
    # login.run(host = '0.0.0.0', port = 80
