# hh-DoubleKill

# 使用的package
pip install flask
pip install flask-sqlalchemy
pip install mysql-python
pip install pymysql


## 运行  
**项目结构如下：**

```
HH-DoubleKill/
├── app
│   ├── static/      # 静态资源文件夹
│   ├── templates/   # 模板文件夹
│   ├── __init__.py  # 初始化文件
│   ├── test.py # blueprint
│   ├── roomSearch.py # blueprint，处理搜索返回
│   ├── models.py # 数据格式 数据库字段
│   └── view.py # 调用blueprint
├── config.py    # 配置文件
├── createdb.py # 创建数据库
├── run.py # 主程序文件
└── README.md
```