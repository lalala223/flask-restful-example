# -*- coding: utf-8 -*-
import os
import pprint
import flask_restful
import logging.handlers
from flask import Flask, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from common.func import pretty_result
from common.code import Code
from config import Config

app = Flask(__name__)

db = SQLAlchemy()

# 保留flask原生异常处理
handle_exception = app.handle_exception
handle_user_exception = app.handle_user_exception


def _custom_abort(http_status_code, **kwargs):
    """自定义abort 400响应数据格式"""
    if http_status_code == 400:
        return abort(jsonify(pretty_result(Code.PARAM_ERROR, data=kwargs.get('message'))))
    return abort(http_status_code)


def _access_control(response):
    """解决跨域请求"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,HEAD,PUT,PATCH,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


def _rotating_file_handler():
    """创建文件写入log handler"""
    if app.config.get('LOG_DIR_PATH'):
        app_log_path = os.path.join(app.config.get('LOG_DIR_PATH'), 'app.log')
    else:
        app_log_path = os.path.join(os.path.dirname(__file__), 'logs/app.log')
    max_bytes = app.config.get('LOG_FILE_MAX_BYTES') or 1024 * 1024 * 100
    backup_count = app.config.get('LOG_FILE_BACKUP_COUNT') or 10

    if not os.path.exists(os.path.dirname(app_log_path)):
        os.makedirs(os.path.dirname(app_log_path))

    file_handler = logging.handlers.RotatingFileHandler(
        filename=app_log_path, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setLevel(app.config.get('LOG_LEVEL') or logging.NOTSET)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d]:%(message)s')
    file_handler.setFormatter(formatter)
    return file_handler


def create_app(config):
    """创建app"""
    # 添加配置
    app.config.from_object(config)
    # 解决跨域
    app.after_request(_access_control)
    # 自定义abort 400 响应数据格式
    flask_restful.abort = _custom_abort
    # 数据库初始化设置
    db.init_app(app)
    # 注册蓝图
    from routes import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    # 使用flask原生异常处理程序
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception
    # 记录文件日志
    if not app.debug:
        for handler in app.logger.handlers:
            app.logger.removeHandler(handler)
    app.logger.addHandler(_rotating_file_handler())
    app.logger.setLevel(app.config.get('LOG_LEVEL', logging.NOTSET))
    return app


if __name__ == '__main__':
    app = create_app(Config)
    pprint.pprint(list(app.url_map.iter_rules()))
    app.run()
