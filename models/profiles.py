# -*- coding: utf-8 -*-
from . import db
from .base import BaseModel


class ProfilesModel(db.Model, BaseModel):
    """
    示例模型类
    """
    __tablename__ = 'profiles'
    nickname = db.Column(db.String)
    signature = db.Column(db.String)
