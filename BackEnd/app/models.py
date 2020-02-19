# -*- coding: utf-8 -*-

from . import app
from . import db


class User(db.Model):
    """用户"""
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    oppenId = db.Column(db.Integer, doc='微信账号唯一标识', nullable=True)
    username = db.Column(db.String(128), doc='用户名', nullable=False)
    password = db.Column(db.String(128), doc='密码', nullable=False)
    phone = db.Column(db.String(20), doc='手机号码', nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
    userRestrict = db.Column(db.String(32), doc='用户权限', nullable=True)
    contain = db.Column(db.String(128), doc='现租的房子', nullable=True)
    description = db.Column(db.String(50), doc='说明', default='这个人很懒，什么也没留下', nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username  
    
def getUsers():
    user_list = User.query.order_by(User.id).all()
    return user_list


def addUser(user):
    # 传入一个User对象
    db.session.add(user)
    db.session.commit()

# def delUser(id):
#     dele = db.query.get(id)
#     if dele == None:
#         return
#     db.session.delete(del)
#     db.session.commit()

def updateUser():
    pass


class Room(db.Model):
    """房源"""
    __tablename__ = 'rooms'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(128), doc='房源状态', nullable=False)
    title = db.Column(db.String(255), doc='标题', nullable=False)
    position = db.Column(db.String(255), doc='位置', nullable=False)
    roomType = db.Column(db.String(128), doc='住房类型', nullable=False)
    isElevator = db.Column(db.Boolean, doc='是否有电梯', default=False)
    price = db.Column(db.Integer, doc='价格', nullable=False, default=1000)
    nearSubway = db.Column(db.String(128), doc='临近地铁', nullable=False)
    releaseTime = db.Column(db.DateTime, doc='发布日期时间', nullable=False)
    payType = db.Column(db.String(128), doc='支付方式', nullable=False)
    area = db.Column(db.Float, doc='房间面积', nullable=False)
    floor = db.Column(db.Integer, doc='楼层', nullable=False)
    plot = db.Column(db.String(255), doc='小区名字', nullable=False)
    picId = db.Column(db.String(128), doc='图片关联id', nullable=False)
    supporting = db.Column(db.String(255), doc='配套设施', nullable=False)
    contactPhone = db.Column(db.Integer, doc='联系电话', nullable=False)
    contactWx = db.Column(db.String(255), doc='联系微信', nullable=False)
    description = db.Column(db.String(255), doc='说明', default='这个人很懒，什么也没留下')
    

    def __repr__(self):
        return '<Room %r>' % self.title

class Picture(db.Model):
    """图片"""
    __tablename__ = 'pictures'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    picId = db.Column(db.String(128), doc='图片关联id', nullable=False)
    picList = db.Column(db.LargeBinary, doc='图片详情', nullable=False)

