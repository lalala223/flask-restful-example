# -*- coding: utf-8 -*-
import string
import flask_restful
from flask import Flask, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids
from example.common.code import Code
from example.common.func import pretty_result

app = Flask(__name__)

db = SQLAlchemy()

hash_ids = Hashids(salt='hvwptlmj129d5quf', min_length=8, alphabet=string.ascii_lowercase + string.digits)

# 保留flask原生异常处理
handle_exception = app.handle_exception
handle_user_exception = app.handle_user_exception


def _custom_abort(http_status_code, **kwargs):
    """
    自定义abort 400响应数据格式
    """
    if http_status_code == 400:
        return abort(jsonify(pretty_result(Code.PARAM_ERROR, data=kwargs.get('message'))))
    return abort(http_status_code)


def _access_control(response):
    """
    解决跨域请求
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,HEAD,PUT,PATCH,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


def create_app(config):
    """
    创建app
    """
    # 添加配置
    app.config.from_object(config)
    # 解决跨域
    app.after_request(_access_control)
    # 自定义abort 400 响应数据格式
    flask_restful.abort = _custom_abort
    # 数据库初始化
    db.init_app(app)
    # 注册蓝图
    from example.routes import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    # 使用flask原生异常处理程序
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception
    return app
