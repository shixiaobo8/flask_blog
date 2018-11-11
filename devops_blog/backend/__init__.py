#!/usr/bin/env python
# -*- coding:utf8 -*-
from flask import Blueprint

backend = Blueprint('backend',__name__)

from . import views
