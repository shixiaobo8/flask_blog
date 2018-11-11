#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
	flask 启动参数
"""
# 导入Falsk 应用
from flask import Flask
# 导入模板应用
from flask import render_template
# 导入falsk bootstrap 应用
from flask_bootstrap import Bootstrap
# 导入 sqlAlchemy python orm 模块
from flask_sqlalchemy import SQLAlchemy
# 导入 sqlAlchemy mongo orm 模块
from flask_mongoalchemy import MongoAlchemy
# 导入配置文件全局环境变量
from config import mysql_db_url,mongo_db_url

# 定义一个创建app应用并且初始化的方法
def create_app():
    # 创建flask应用
    app = Flask(__name__)
    # 初始化bootstrap
    Bootstrap(app)
    # 初始化mysql数据库连接
    app.config['SQLALCHEMY_DATABASE_URI'] = mysql_db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    mysql_db = SQLAlchemy(app)
    # 初始化mongo数据库连接
    app.config['MONGOALCHEMY_CONNECTION_STRING'] = mongo_db_url
    app.config['MONGOALCHEMY_DATABASE'] = 'flask_blog'
    mongo_db = MongoAlchemy(app)
    return app

# 创建一个flask app 应用
blog_app = create_app()

# 创建一个视图应用,博客首页
@blog_app.route('/')
def index():
    return render_template('base/base.html')

if __name__ == "__main__":
    blog_app.run(debug=True,host='0.0.0.0',port=89)
