#!/usr/bin/env python
# -*- coding:utf8 -*-
from  flask import Blueprint

# 创建蓝图 
blog = Blueprint('blog',__name__)

from . import views
