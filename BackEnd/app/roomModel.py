# -*- coding: utf-8 -*-

# from app import app
from app import db
import time


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
    isElevator = db.Column(db.Boolean, doc='是否有电梯', default=False)
    price = db.Column(db.Integer, doc='价格', nullable=False, default=1000)
    nearSubway = db.Column(db.String(128), doc='临近地铁', nullable=False)
    releaseTime = db.Column(db.DateTime, doc='发布日期时间', nullable=False, default=str(time.strftime('%Y-%m-%d %H:%M:%S')))
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
        return '<Room %r,%r,%r,%r,%r,%r,%r>' % (self.title,self.creatorId,self.supporting,self.title,self.position,self.roomType,self.releaseTime)



def addRoom(newRoom):
     # 传入一个User对象,返回创建roomId
    print(newRoom)
    try:
        db.session.add(newRoom)
        db.session.commit()
    except Exception as e:
        return e
    lastId = Room.query.all()[-1].id
    return lastId

def getRoomList():
    roomList = Room.query.all()
    returnRoomList = []
    for room in roomList:
        oneRoom = makeAllRoomToList(room)
        returnRoomList.append(oneRoom)
    return returnRoomList


def getRoomById(roomId):
    roomRecord = Room.query.filter_by(id=roomId).first()
    if not roomRecord:
        return 404
    return roomRecord


def getRoomByIdResponse(roomId):
    roomRecord = Room.query.filter_by(id=roomId).first()
    if not roomRecord:
        return 404
    resp = makeOneRoomToDict(roomRecord)
    return resp


def deleteRoomById(roomId):
    roomDelete = Room.query.filter_by(id=roomId).first()
    if not roomDelete:
        return 404
    try:
        db.session.delete(roomDelete)
        db.session.commit()
    except Exception:
        return 500
    return 200


def makeOneRoomToDict(r):
    roomDict = {}
    roomDict["id"] = r.id
    roomDict["creatorId"] = r.creatorId
    roomDict["status"] = r.status
    roomDict["title"] = r.title
    roomDict["picIdList"] = r.picIdList
    roomDict["position"] = r.position
    roomDict["address"] = r.address
    roomDict["roomType"] = r.roomType
    roomDict["isElevator"] = r.isElevator
    roomDict["price"] = r.price
    roomDict["nearSubway"] = r.nearSubway
    roomDict["releaseTime"] = str(r.releaseTime)
    roomDict["payType"] = r.payType
    roomDict["area"] = r.area
    roomDict["floor"] = r.floor
    roomDict["plot"] = r.plot
    roomDict["supporting"] = r.supporting
    roomDict["contactPhone"] = r.contactPhone
    roomDict["contactWx"] = r.contactWx
    roomDict["views"] = r.views
    roomDict["description"] = r.description
    return roomDict


def makeAllRoomToList(r):
    roomDict = {}
    roomDict["id"] = r.id
    roomDict["creatorId"] = r.creatorId
    roomDict["status"] = r.status
    roomDict["title"] = r.title
    roomDict["picIdList"] = r.picIdList
    roomDict["position"] = r.position
    roomDict["address"] = r.address
    roomDict["roomType"] = r.roomType
    roomDict["isElevator"] = r.isElevator
    roomDict["price"] = r.price
    roomDict["nearSubway"] = r.nearSubway
    roomDict["releaseTime"] = str(r.releaseTime)
    roomDict["area"] = r.area
    roomDict["floor"] = r.floor
    roomDict["plot"] = r.plot
    roomDict["supporting"] = r.supporting
    return roomDict


def roomUpdate(updateParam):
    upRoom = getRoomById(updateParam["roomId"])
    if not upRoom:
        return 404
    try:
        upKey = updateParam.keys()
        if "creatorId" in upKey:
            upRoom.creatorId = updateParam["creatorId"]
        if "status" in upKey:
            upRoom.status = updateParam["status"]
        if "title" in upKey:
            upRoom.title = updateParam["title"]
        if "picIdList" in upKey:
            upRoom.picIdList = str(updateParam["picIdList"])
        if "position" in upKey:
            upRoom.position = str(updateParam["position"])
        if "address" in upKey:
            upRoom.address = updateParam["address"]
        if "roomType" in upKey:
            upRoom.roomType = str(updateParam["roomType"])

        # if "isElevator" in upKey:
        #     upRoom["isElevator"] = updateParam["isElevator"]

        if "price" in upKey:
            upRoom.price = updateParam["price"]
        if "nearSubway" in upKey:
            upRoom.nearSubway = updateParam["nearSubway"]
        if "payType" in upKey:
            upRoom.payType = updateParam["payType"]
        if "area" in upKey:
            upRoom.area = updateParam["area"]
        if "floor" in upKey:
            upRoom.floor = updateParam["floor"]
        if "plot" in upKey:
            upRoom.plot = updateParam["plot"]
        if "supporting" in upKey:
            upRoom.supporting = str(updateParam["supporting"])
        if "contactPhone" in upKey:
            upRoom.contactPhone = updateParam["contactPhone"]
        if "contactWx" in upKey:
            upRoom.contactWx = updateParam["contactWx"]
        if "description" in upKey:
            upRoom.description = updateParam["description"]
        upRoom.releaseTime = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        db.session.commit()
    except Exception:
        return 500
    return 200

 