import redis
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)

class Config(object):
    """工程信息配置"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True

    # 导入数据库配置
    # 设置数据库连接
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/information22'
    # 动态追踪设置
    app.config['SQLALCHEMY_TRACK_MODUFICATIONS'] = True
    # 显示原始sql
    app.config['SQLALCHEMY_ECHO'] = True

 # flask_session的配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒

app.config.from_object(Config)
db = SQLAlchemy(app)

# redis.StrictRedis(host=Config.RDIES_HOST,port=Config.RDIES_PORT)

#开启csrf保护，只用于服务器验证功能
CSRFProtect(app)
# 设置session保护指定位置
Session(app)

manager=Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    session['name']='eric'
    return "index"
if __name__=='__main__':
    manager.run()