# -*- coding: utf-8 -*-

from . import app
from . import db

class User(db.Model):
    """用户"""
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), doc='账号', nullable=False)
    password = db.Column(db.String(128), doc='密码', nullable=False)
    phone = db.Column(db.String(20), doc='手机号码', nullable=False, unique=True)
    description = db.Column(db.String(50), doc='说明', default='这个人很懒，什么也没留下', nullable=False)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
