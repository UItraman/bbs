from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from models.user import User
from models.node import Node
from models.topic import Topic
from models.comment import Comment


app = Flask(__name__)
manager = Manager(app)


def register_routes(app):
    from routes.node import main as routes_node
    from routes.topic import main as routes_topic
    from routes.auth import main as routes_auth
    from routes.comment import main as routes_comment

    app.register_blueprint(routes_auth, url_prefix='/auth')
    app.register_blueprint(routes_node, url_prefix='/node')
    app.register_blueprint(routes_topic, url_prefix='/topic')
    app.register_blueprint(routes_comment, url_prefix='/comment')


def configured_app(config_name):
    from config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化 db
    db.init_app(app)
    # 注册路由
    register_routes(app)
    # 配置日志
    configure_log(app)
    # 返回配置好的 app 实例
    return app


def configure_log(app):
    # 设置 log, 否则输出会被 gunicorn 吃掉
    # 但是如果 app 是 debug 模式的话, 则不用这么搞
    if not app.debug:
        import logging
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    app = configured_app('default')
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configured_app('default')
    manager.run()
