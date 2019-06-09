# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
import os
import logging.handlers
from abc import ABC
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from multiprocessing import cpu_count
from app import create_app, db
from config import Config

DEFAULT_LOG_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

app = create_app(Config)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


def rotating_file_handler():
    """
    创建logging.handlers.RotatingFileHandler对象
    """
    file_name = os.path.join(app.config.get('LOG_DIR_PATH', DEFAULT_LOG_DIR_PATH), 'app.log')
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))

    max_bytes = app.config.get('LOG_FILE_MAX_BYTES', 1024 * 1024 * 100)
    backup_count = app.config.get('LOG_FILE_BACKUP_COUNT', 10)
    handler = logging.handlers.RotatingFileHandler(
        filename=file_name, maxBytes=max_bytes, backupCount=backup_count
    )
    handler.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d]:%(message)s')
    handler.setFormatter(formatter)
    return handler


class StandaloneApplication(BaseApplication, ABC):
    """
    gunicorn服务器启动类
    """

    def __init__(self, application, options):
        self.application = application
        self.options = options or {}
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@manager.command
def run():
    """
    生产模式启动命令函数
    To use: python3 manager.py run
    """
    # 记录项目app日志
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    app.logger.addHandler(rotating_file_handler())
    app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    # 设置gunicorn日志文件存放路径
    log_dir_path = app.config.get('LOG_DIR_PATH', DEFAULT_LOG_DIR_PATH)
    if not os.path.exists(os.path.dirname(log_dir_path)):
        os.makedirs(os.path.dirname(log_dir_path))
    # 启动gunicorn服务器
    service_config = {
        'bind': app.config.get('BIND', '0.0.0.0:5000'),
        'workers': app.config.get('WORKERS', cpu_count() * 2 + 1),
        'worker_class': 'gevent',
        'timeout': app.config.get('TIMEOUT', 60),
        'loglevel': app.config.get('LOG_LEVEL', 'info'),
        'errorlog': os.path.join(log_dir_path, 'error.log'),
        'accesslog': os.path.join(log_dir_path, 'access.log'),
        'pidfile': app.config.get('PID_FILE', 'run.pid'),
        'worker_connections': app.config.get('WORKER_CONNECTIONS', 1000)
    }
    StandaloneApplication(app, service_config).run()


@manager.command
def debug():
    """
    debug模式启动命令函数
    To use: python3 manager.py debug
    """
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
