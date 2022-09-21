# @Time: 2022/9/21 15:52
# @Author: 李树斌
# @File : errors.py
# @Software :PyCharm

#主蓝本中的错误处理程序

from flask import render_template
from . import main

#使用app_errorhandler注册应用全局的错误处理程序
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500