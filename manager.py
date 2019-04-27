# -*- coding: utf-8 -*-
from gevent import monkey;monkey.patch_all()
import os
from abc import ABC
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from multiprocessing import cpu_count
from example import create_app, db
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
    log_path = app.config.get('LOG_DIR_PATH', os.path.join(os.path.dirname(__file__), 'logs'))
    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))

    service_config = {
        'bind': app.config.get('BIND', '0.0.0.0:5000'),
        'workers': app.config.get('WORKERS', cpu_count() * 2 + 1),
        'worker_class': 'gevent',
        'timeout': app.config.get('TIMEOUT', 60),
        'loglevel': app.config.get('LOG_LEVEL', 'info'),
        'errorlog': os.path.join(log_path, 'error.log'),
        'accesslog': os.path.join(log_path, 'access.log'),
        'pidfile': app.config.get('PID_FILE', 'run.pid'),
    }
    StandaloneApplication(app, service_config).run()


@manager.command
def debug():
    """
    debug模式启动命令函数
    To use: python3 manager.py debug
    """
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
