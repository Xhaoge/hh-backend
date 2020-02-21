# -*- coding: utf-8 -*-

from app import app
from app import db


class User(db.Model):
    """用户"""
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    openId = db.Column(db.Integer, doc='微信账号唯一标识', nullable=False)
    username = db.Column(db.String(128), doc='用户名', nullable=True)
    password = db.Column(db.String(128), doc='密码', nullable=True)
    phone = db.Column(db.String(20), doc='手机号码', nullable=True, unique=True)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
    userRestrict = db.Column(db.String(32), doc='用户权限', nullable=True)
    contain = db.Column(db.String(128), doc='现租的房子', nullable=True)
    description = db.Column(db.String(50), doc='说明', default='这个人很懒，什么也没留下', nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username  

 # 获取所有的Users   
def getUsers():
    user_list = User.query.order_by(User.id).all()
    return user_list

# 通过用户唯一的Id 来查找某位用户信息
def getUserById(uid):
    user =  User.query.filter_by(id='%s').first() % uid
    if not user:
        return 404
    return user

# 通过用户唯一的openId 来查找确定用户是否存在
def getUserById(pid):
    user =  User.query.filter_by(openId='%s').first() % pid
    if not user.id:
        return False
    return True

# 往数据库里插入一条记录
def addUser(user):
    # 传入一个User对象
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return e
    uid = User.query.filter_by(openId='%s').first() % user.openId
    return uid

def delUser(id):
    dele = db.query.get(id)
    if dele == None:
        return 404
    db.session.delete(dele)
    db.session.commit()
    return 200

def updateUser():
    pass


class Room(db.Model):
    """房源"""
    __tablename__ = 'rooms'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.Integer, doc='创建者房源id', nullable=False)
    status = db.Column(db.String(128), doc='房源状态', nullable=True)
    title = db.Column(db.String(255), doc='标题', nullable=False)
    picId = db.Column(db.String(225), doc='图片list', nullable=False)
    position = db.Column(db.String(255), doc='位置', nullable=False)
    address = db.Column(db.String(255), doc='房源地址', nullable=False)
    roomType = db.Column(db.String(128), doc='住房类型', nullable=False)
    isElevator = db.Column(db.Boolean, doc='是否有电梯', default=False)
    price = db.Column(db.Integer, doc='价格', nullable=False, default=1000)
    nearSubway = db.Column(db.String(128), doc='临近地铁', nullable=False)
    releaseTime = db.Column(db.DateTime, doc='发布日期时间', nullable=False)
    payType = db.Column(db.String(128), doc='支付方式', nullable=False)
    area = db.Column(db.Float, doc='房间面积', nullable=False)
    floor = db.Column(db.Integer, doc='楼层', nullable=False)
    plot = db.Column(db.String(255), doc='小区名字', nullable=False)
    supporting = db.Column(db.String(255), doc='配套设施', nullable=False)
    contactPhone = db.Column(db.String(255), doc='联系电话', nullable=False)
    contactWx = db.Column(db.String(255), doc='联系微信', nullable=False)
    views = db.Column(db.Integer, doc='浏览次数', nullable=True, default=0)
    description = db.Column(db.String(255), doc='说明', default='这个人很懒，什么也没留下')
    

    def __repr__(self):
        return '<Room %r>' % self.title





# class Picture(db.Model):
#     """图片"""
#     __tablename__ = 'pictures'
#     __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
#     id = db.Column(db.Integer, primary_key=True)
#     picId = db.Column(db.String(128), doc='图片关联id', nullable=False)
#     picList = db.Column(db.LargeBinary, doc='图片详情', nullable=False)

