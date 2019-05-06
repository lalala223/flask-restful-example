# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from example.resources import profiles

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(profiles.ProfilesListExampleAPI, '/profiles')
api.add_resource(profiles.ProfileExampleAPI, '/profiles/<string:id>')
