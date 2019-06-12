# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
import logging.handlers
from abc import ABC
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from multiprocessing import cpu_count
from app import create_app, db
from config import Config

app = create_app(Config)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


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
    app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    service_config = {
        'bind': app.config.get('BIND', '0.0.0.0:5000'),
        'workers': app.config.get('WORKERS', cpu_count() * 2 + 1),
        'worker_class': 'gevent',
        'worker_connections': app.config.get('WORKER_CONNECTIONS', 10000),
        'backlog': app.config.get('BACKLOG', 2048),
        'timeout': app.config.get('TIMEOUT', 60),
        'loglevel': app.config.get('LOG_LEVEL', 'info'),
        'pidfile': app.config.get('PID_FILE', 'run.pid'),
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
