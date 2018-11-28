#!/usr/bin/env python
# -*- coding:utf8 -*-
from flask import jsonify,make_response,request,g
from devops_blog import create_app
from flask_script import Manager,Server,Shell
from devops_blog.commands import Hello
from flask_migrate import MigrateCommand
# 导入自定义错误类
from devops_blog.utils import CustomFlaskErr
# 导入所有migrate需要操作的model 类
from devops_blog.blog.models import *
import os
import werkzeug

def _make_context(app):
    return dict(app=app)


# 创建一个flask app 应用 并初始化
blog_app = create_app(flask_env=os.getenv('FLASK_ENV') or 'default')


#初始化shell
def _make_context():
    return dict(app=blog_app)


manager = Manager(blog_app)
# 添加shell 命令交互器
manager.add_command("shell", Shell(make_context=_make_context),user_ipython=True)
# 添加hello 打印命令测试
manager.add_command("hello", Hello())
# 添加执行server命令
manager.add_command("runserver",Server())
# 添加数据 migrate 工具
manager.add_command('db',MigrateCommand)


# 自定义错误
@blog_app.errorhandler(CustomFlaskErr)
def handle_flask_error(error):
    # response 的 json 内容为自定义错误代码和错误信息
    response = jsonify(error.to_dict())
    # response 返回 error 发生时定义的标准错误代码
    response.status_code = error.status_code
    return response


# 404  错误
@blog_app.errorhandler(404)
def not_found(error):
         return make_response(jsonify({'error': 'Not found'}), 404)


#  500 错误
@blog_app.errorhandler(500)
def inter_server_error(e):
    blog_app.logger.error('error 500: %s', e)
    return make_response(jsonify({'error': 'server internet error'}), 500)


# 应用情景
# 第一次请求的时候做初始化导航栏nav数据
@blog_app.before_first_request
def print_request_info():
    blog_app.logger.info("启动项目中,正在初始化导航栏nav....")
    navs = Nav.query.all()
    g.navs= navs
    print("=====")
    print(navs)


#def get_db():
#    if 'db' not in g:
#        g.db = connect_to_database()
#    return g.db

#@blog_app.teardown_appcontext
#def teardown_db():
#    db = g.pop('db', None)
#    if db is not None:
#        db.close()


if __name__ == "__main__":
    manager.run()
#    blog_app.run(debug=True,host='0.0.0.0',port=89)
