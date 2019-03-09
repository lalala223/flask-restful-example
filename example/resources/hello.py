# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from example.app import app
from example.common.code import Code
from example.common.func import pretty_result


class HelloWorld(Resource):
    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        app.logger.info('hello, world')
        return pretty_result(Code.OK, data='hello, world!')

    def post(self):
        self.parser.add_argument("user", type=str, location="form", required=True)
        self.parser.add_argument("password", type=str, location="form", required=True)
        args = self.parser.parse_args(strict=True)
        return pretty_result(Code.OK, data='hello, %s!' % args.get('user'))
