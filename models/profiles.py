# -*- coding: utf-8 -*-
from app import db
from .base import BaseModel


class ProfilesModel(db.Model, BaseModel):
    """
    示例模型类
    """
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String)
    signature = db.Column(db.String)
