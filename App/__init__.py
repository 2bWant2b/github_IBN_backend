import os

from flask import Flask
from .exts import init_exts, db
from .utils import data_fetcher  # 为了保持先初始化scheduler再添加job
from .resources import urls


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # 配置数据库
    # db_uri = 'mysql+pymysql://root:123456@localhost:3306/flaskdb2'  # mysql的配置
    db_uri = "sqlite:///db.sqlite3"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止追踪修改
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.secret_key = "kc304"

    # 初始化第三方插件
    init_exts(app=app)

    return app

