#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
	配置文件(官方文档中提倡的有效配置文件写法)
	     参考:https://dormousehole.readthedocs.io/en/latest/config.html
	     使用config.py 对象的规则:
		1. app加载的时候使用 app.config.from_object('configmodule.ProductionConfig')
	  	2. Config 对象中必须的变量名称必须大写开头
"""
class Config:
    pass

# 生产环境配置
class ProductionConfig(Config):
    ENV = 'production'
    # 调试模式
    DEBUG = False
    # 测试模式
    TESTING = False
    # mongodb 连接
    MONGOALCHEMY_CONNECTION_STRING='mongodb://127.0.0.1:27017/flask_blog'
    MONGOALCHEMY_DATABASE = 'flask_blog'
    # mysql 连接
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 域名配置
    SERVER_NAME = 'demo.devops89.cn'
    # 方便apache 部署
    USE_X_SENDFILE = False
    # cookie 会话的安全签名
    SECRET_KEY = b'ab#_2L"3dQ8zc-\xcc]/'
    # 邮件配置
    MAIL_SERVER = 'smtp.yikaobang.com.cn'
    MAIL_PORT = 465 
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'devops@yikaobang.com.cn'
    MAIL_PASSWORD = 'Ykbmail89!@#'
    AA = '2323'
    SECRET_KEY = b'233#_2L"3dQ8zc-\xcc]/'

# 开发环境配置
class DevelopmentConfig(Config):
    ENV = 'development'
    # 调试模式
    DEBUG = True
    # 测试模式
    TESTING = False
    # mongodb 连接
    MONGOALCHEMY_CONNECTION_STRING='mongodb://127.0.0.1:27017/flask_blog'
    MONGOALCHEMY_DATABASE = 'flask_blog'
    # mysql 连接
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:123456@127.0.0.1:3306/flask_blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 域名配置 正式环境必须配置这个参数
    #SERVER_NAME = 'blog.devops89.cn'
    # 方便apache 部署
    USE_X_SENDFILE = False
    # cookie 会话的安全签名
    SECRET_KEY = b'ab#_2L167dQ8zc-\xcc2c'
    # 邮件配置
    MAIL_SERVER = 'smtp.yikaobang.com.cn'
    MAIL_PORT = 465 
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'devops@yikaobang.com.cn'
    MAIL_PASSWORD = 'Ykbmail89!@#'
    SECRET_KEY = b'ab#_2L"3dQ8zc-\xcc]/'


# 测试配置
class TestingConfig(Config):
    TESTING = True

# 在这里可以配置部署的是生产环境还是开发环境
flask_env_config = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
# 开发环境打开这条注释
    'default': DevelopmentConfig
# 生产环境打开这条注释
#    'default': ProductionConfig,
}

