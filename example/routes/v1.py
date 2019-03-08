# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from resources.hello import HelloWorld

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(HelloWorld, '/hello')
