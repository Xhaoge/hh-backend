# -*- coding: utf-8 -*-

from app import app
from app import db


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

