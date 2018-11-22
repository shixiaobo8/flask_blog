#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
	mongo_mo
"""
from .. import mongo_db
from devops_blog.utils import timeTools
from datetime import datetime

time_tools = timeTools()

class Post(mongo_db.Document):
    #id = mongo_db.IntField()
    title = mongo_db.StringField()
    body = mongo_db.StringField()
    ctime = mongo_db.DateTimeField(default=datetime.now())
    category_id = mongo_db.IntField(default=None)

    #def __init__(self,title,body):
    #    title = self.title
    #    body = self.body


class Category(mongo_db.Document):
    #id = mongo_db.IntField()
    name = mongo_db.StringField()

    #def __init__(self,name):
     #   name = self.name
