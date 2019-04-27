# -*- coding: utf-8 -*-
from flask import current_app
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import SQLAlchemyError
from example.app import db
from example.models import ProfilesExampleModel
from example.common.code import Code
from example.common.func import pretty_result


class ProfilesExampleAPI(Resource):
    """
    示例资源类
    """
    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        self.parser.add_argument("page_num", type=int, location="args", default=1)
        self.parser.add_argument("page_size", type=int, location="args", default=10)
        args = self.parser.parse_args()

        try:
            profiles = ProfilesExampleModel.query.paginate(args.page_num, args.page_size, error_out=False)
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return pretty_result(Code.DB_ERROR, '数据库错误！')

        items = []
        for i in profiles.items:
            items.append(
                {
                    'id': i.id,
                    'nickname': i.nickname,
                    'signature': i.signature
                }
            )
        data = {
            'page_num': args.page_num,
            'page_size': args.page_size,
            'total': profiles.total,
            'items': items
        }
        return pretty_result(Code.OK, data=data)

    def post(self):
        self.parser.add_argument("nickname", type=str, location="json", required=True)
        self.parser.add_argument("signature", type=str, location="json", required=True)
        args = self.parser.parse_args()

        profile = ProfilesExampleModel(nickname=args.nickname, signature=args.signature)

        try:
            db.session.add(profile)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.error(e)
            return pretty_result(Code.DB_ERROR, '数据库错误！')
        return pretty_result(Code.OK, '添加数据成功～')
