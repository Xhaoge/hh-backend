# -*- coding: UTF-8 -*-
import os
from app import app, db

if __name__ == '__main__':
    '''
    开启 debug模式
    # 把自己的电脑作为服务器，可以让别人访问
    '''
    
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True, port=app.config.get("PORT"))
    # app.run(debug=True)
