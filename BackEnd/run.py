# -*- coding: UTF-8 -*-
from app import app


if __name__ == '__main__':
    '''
    开启 debug模式
    设置 host='0.0.0.0'
    '''
    # if not os.path.exists('db.sqlite'):
    #     db.create_all()
    app.run(debug=True, host='127.0.0.1',port=8080)
    # app.run(debug=True)