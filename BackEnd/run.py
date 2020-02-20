# -*- coding: UTF-8 -*-
import os
from BackEnd.app import app, db

if __name__ == '__main__':
    '''
    开启 debug模式
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    # 把自己的电脑作为服务器，可以让别人访问
    '''
    
    # if not os.path.exists('db.sqlite'):
    #     db.create_all()
    app.run(debug=True,port=80)
    # app.run(debug=True)
