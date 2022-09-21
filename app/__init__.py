# @Time: 2022/9/21 14:57
# @Author: 李树斌
# @File : __init__.py
# @Software :PyCharm
#应用包的构造文件
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from .main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)

    #添加路由和自定义的错误页面




    return app