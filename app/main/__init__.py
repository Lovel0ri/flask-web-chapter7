# @Time: 2022/9/21 15:35
# @Author: 李树斌
# @File : __init__.py
# @Software :PyCharm
#创建主蓝本
from flask import Flask

main = Blueprint('main',__name__)#蓝本实例化一个blueprint类创建，蓝本名，蓝本所在的包或者模块
#把路由和错误处理关联起来
from . import views, errors


