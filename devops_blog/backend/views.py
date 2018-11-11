#!/usr/bin/env python
# -*- coding:utf8 -*-
from flask import render_template
from . import backend

@backend.route('/')
def index():
    return "请登录"
