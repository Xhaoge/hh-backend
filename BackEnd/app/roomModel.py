# -*- coding: utf-8 -*-

from app import app
from app import db
from datetime import datetime


class Room(db.Model):
    """房源"""
    __tablename__ = 'rooms'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.Integer, doc='创建者房源id', nullable=False)
    status = db.Column(db.String(128), doc='房源状态', nullable=True, default="Offline")
    title = db.Column(db.String(255), doc='标题', nullable=False)
    picIdList = db.Column(db.String(225), doc='图片list', nullable=False)
    position = db.Column(db.String(255), doc='位置', nullable=False)
    address = db.Column(db.String(255), doc='房源地址', nullable=False)
    roomType = db.Column(db.String(128), doc='住房类型', nullable=False)
    # isElevator = db.Column(db.Boolean, doc='是否有电梯', default=False)
    price = db.Column(db.Integer, doc='价格', nullable=False, default=1000)
    nearSubway = db.Column(db.String(128), doc='临近地铁', nullable=False)
    # releaseTime = db.Column(db.Date, doc='发布日期时间', nullable=False, default=datetime.date)
    payType = db.Column(db.String(128), doc='支付方式', nullable=False)
    area = db.Column(db.Float, doc='房间面积', nullable=False)
    floor = db.Column(db.Integer, doc='楼层', nullable=False)
    plot = db.Column(db.String(255), doc='小区名字', nullable=False)
    supporting = db.Column(db.String(255), doc='配套设施', nullable=False)
    contactPhone = db.Column(db.String(255), doc='联系电话', nullable=False)
    contactWx = db.Column(db.String(255), doc='联系微信', nullable=True)
    views = db.Column(db.Integer, doc='浏览次数', nullable=True, default=0)
    description = db.Column(db.String(255), doc='说明', default='这个人很懒，什么也没留下')
    

    def __repr__(self):
        return '<Room %r,%r,%r,%r,%r,%r>' % (self.title,self.creatorId,self.supporting,self.title,self.position,self.roomType)



def addRoom(newRoom):
     # 传入一个User对象
    print(newRoom)
    try:
        db.session.add(newRoom)
        db.session.commit()
    except Exception as e:
        return e
    
    return "success"

# class Picture(db.Model):
#     """图片"""
#     __tablename__ = 'pictures'
#     __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
#     id = db.Column(db.Integer, primary_key=True)
#     picId = db.Column(db.String(128), doc='图片关联id', nullable=False)
#     picList = db.Column(db.LargeBinary, doc='图片详情', nullable=False)

