#!/usr/bin/env python
# -*- coding:utf8 -*-
from devops_blog import create_app
from flask_script import Manager,Server,Shell
from devops_blog.commands import Hello
import os

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


if __name__ == "__main__":
    manager.run()
#    blog_app.run(debug=True,host='0.0.0.0',port=89)
