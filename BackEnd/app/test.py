from BackEnd.app.models import User,getUsers,addUser
from BackEnd.app import db
import json
def get_user():
    resp = {"code": 200, "msg": "操作成功", "data": {}}
    openid="1458"
    session_key="我是session_key"
    if openid and session_key:
        '''
        在数据库用户表查询（查找得到的OpenID在数据库中是否存在）
        SQLalchemy语句：
        user_info = User.query.filter(User.OpenID == openid).first() 
        '''
        if openid not in getUsers():
        # if getUsers() is None:   id=2,
            user_info = User(openId=openid)
            addUser(user_info)

        return json.dumps(resp, ensure_ascii=False)
    print(resp)
    return json.dumps(resp)

if __name__ == "__main__":
    get_user()