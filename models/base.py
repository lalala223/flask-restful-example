# -*- coding: utf-8 -*-
import datetime
from app import db


class BaseModel(object):
    """
    数据基础类
    """
    create_time = db.Column(db.DATETIME(6), default=datetime.datetime.now)
    update_time = db.Column(db.DATETIME(6), default=datetime.datetime.now, onupdate=datetime.datetime.now)
    is_delete = db.Column(db.BOOLEAN, default=False)
