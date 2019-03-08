# -*- coding: utf-8 -*-
MODE = 'develop'  # develop: 开发模式; production: 生产模式


class ProductionConfig(object):
    BIND = '127.0.0.1:5000'
    TIMEOUT = 60
    WORKERS = None
    LOG_LEVEL = 'INFO'
    LOG_DIR_PATH = './logs'
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 100
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'example.pid'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:******@localhost/example?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


class DevelopConfig(object):
    DEBUG = True
    BIND = '0.0.0.0:5000'
    TIMEOUT = 30
    WORKERS = 2
    LOG_LEVEL = 'DEBUG'
    LOG_DIR_PATH = './logs'
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = None
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:******@localhost/example?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if MODE == 'production':
    Config = ProductionConfig
else:
    Config = DevelopConfig
