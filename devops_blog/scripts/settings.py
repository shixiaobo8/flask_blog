#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    flask 自动转换
"""

SQLALCHEMY_DATABASE_URI = 'flask_blog': 'pymysql://root:123456@127.0.0.1/flask_blog',  
SQLALCHEMY_BINDS = {  
            'flask_blog': 'pymysql://root:123456@127.0.0.1/flask_blog',  
            }  
TABLE_PREFIX = 'fb_'
