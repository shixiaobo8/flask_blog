#!/usr/bin/env python
# -*- coding:utf8 -*-
from flask import render_template
from . import blog
from .. import mysql_db,mongo_db


# 创建一个视图应用,博客首页
@blog.route('/',methods=('GET','POST'))
def index():
    return render_template('base/base.html')


@blog.route('/test')
def test():
    return render_template("blog/test.html")
