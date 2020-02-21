# -*- coding: utf-8 -*-
from flask import Blueprint, request
from app import db
from app.userModel import getUsers,User
from app import app
import requests, json
login_mod = Blueprint('login',__name__)

@login_mod.route('/login',methods = ["GET","POST"])
def log_in():
    resp = {"code":200,"msg":"操作成功", "data":{}}
    data = json.loads(request.get_data().decode('utf-8')) #将前端Json数据转为字典
    appID = 'wxd20112c596493f06'
    appSecret = 'c156da5ff391cd48fb76c90f99150c24'
    # code = '023gTHKO1Xhcg71tKsJO1s4PKO1gTHKH'
    code = data['code'] if "code" in data else ""
    if not code or len(code) < 1 :
        resp["code"] = -1
        resp["msg"]="需要code"
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
        if getUsers() is None:
            user_info = User(openId=openid)
            db.session.add(user_info)
            db.session.commit()
            return json.dumps(user_info.UserID, ensure_ascii=False)
    return json.dump(resp)
