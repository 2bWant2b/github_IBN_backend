# exts.py: 扩展的第三方插件

# 1. 导入第三方插件
from flask_sqlalchemy import SQLAlchemy  # ORM，用于将 Python 类定义为数据库模型（Models）
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_caching import Cache
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_apscheduler import APScheduler
from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager

# 2. 初始化
db = SQLAlchemy()  # ORM
ma = Marshmallow()  # 序列化与反序列化
scheduler = APScheduler()  # 定时任务
migrate = Migrate()  # 数据库迁移
api = Api()  # RESTful API


cache = Cache(config={
    'CACHE_TYPE': 'simple'  # 缓存类型：简单的内存缓存
})


# 3. 和 app 对象关联
def init_exts(app):
    CORS(app, resources=r'/*')
    db.init_app(app=app)
    ma.init_app(app=app)
    # scheduler.init_app(app=app)
    # scheduler.api_enabled = True
    # scheduler.start()
    migrate.init_app(app=app, db=db)
    api.init_app(app)
    cache.init_app(app=app)

