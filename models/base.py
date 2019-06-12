# -*- coding: utf-8 -*-
import datetime
from . import db


class BaseModel(object):
    """
    数据基础类
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_delete = db.Column(db.BOOLEAN, default=False)
    create_time = db.Column(db.DATETIME(6), default=datetime.datetime.now)
    update_time = db.Column(db.DATETIME(6), default=datetime.datetime.now, onupdate=datetime.datetime.now)
