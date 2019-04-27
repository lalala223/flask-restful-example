# -*- coding: utf-8 -*-
import os
import multiprocessing

MODE = 'develop'  # develop: 开发模式; production: 生产模式


class ProductionConfig(object):
    """
    生产配置
    """
    BIND = '127.0.0.1:5000'
    TIMEOUT = 60
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    LOG_LEVEL = 'INFO'
    LOG_DIR_PATH = './logs'
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 100
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'example.pid'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(object):
    """
    开发配置
    """
    BIND = '0.0.0.0:5000'
    TIMEOUT = 30
    WORKERS = 2
    LOG_LEVEL = 'DEBUG'
    LOG_DIR_PATH = './logs'
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = 'example.pid'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if MODE == 'production':
    Config = ProductionConfig
else:
    Config = DevelopConfig
