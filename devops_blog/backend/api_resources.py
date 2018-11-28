#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
	restful api route 类和类注册文件
"""
from flask_restful import Resource
from flask_restful import reqparse
from ..blog.models import Nav,subNav
from .. import mysql_db
from ..utils import generate_response,CustomFlaskErr
from flask import request,current_app
from flask_restful import abort


# 测试api 类
class ApiTest(Resource):
    # 参数检查
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No task title provided', location = 'args')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(ApiTest, self).__init__()
    
    def get(self):
        args = self.reqparse.parse_args(strict=True)
        return {"data":"this is apitest",'title':args['title']}
    
    def post(self):
        return {"data":"this is apitest"}


# 导航栏 单个处理类
class NavApi(Resource):
    # 请求参数处理
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.args = self.reqparse.parse_args()
        # 获取request json 参数
        self.json_args = request.json
        super(NavApi,self).__init__()

    # 查询单个
    def get(self):
        return self.args
        
    
    # 修改一个
    def post(self):
        pass

    # 新增一个
    def put(self):
        # 获取request json 参数
        json_args = self.json_args
        # 获取二级导航栏参数
        sNavs = json_args['sNavs']
        # 查询是否含有相同的菜单名称和url
        exists_fName = Nav.query.filter_by(navTitle=json_args['fNavName']).first()
        exists_fUrl = ''
        if json_args['fNavUrl'] != '':
            exists_fUrl = Nav.query.filter_by(navUrl=json_args['fNavUrl']).first()
        if exists_fUrl or exists_fName:
            current_app.logger.error("查询出错: 已存在相同的一级导航栏信息")
            raise CustomFlaskErr("vAlreadyExistsError1")
        else:
            # 先添加一级菜单,然后关联二级菜单
            firstNav = Nav(json_args['fNavName'],json_args['fNavUrl'],int(json_args['type']),int(json_args['navPris'][0]))
            for secondNav in sNavs:
                # 检查是否含有存在的二级菜单
                exists_sNav = subNav.query.filter_by(title=secondNav['sNavName'],nav_url=secondNav['sNavUrl']).first()
                if exists_sNav:
                    current_app.logger.error("查询出错: 已存在相同的二级导航栏信息")
                    raise CustomFlaskErr("NavAlreadyExistsError2")
                else:
                    sub_nav = subNav(secondNav['sNavName'],secondNav['sNavUrl'])
                    mysql_db.session.add(sub_nav)
                    # 关联二级菜单
                    firstNav.subnavs.append(sub_nav)
            mysql_db.session.add(firstNav)
            mysql_db.session.commit()
        return generate_response()


    # 删除一个
    def delete(self):
        pass


# 导航栏nav 处理列表类
class NavListApi(Resource):
    # 请求参数处理
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('data', type = str, required = True, location='json')
        #self.reqparse.add_argument('action', type = str, required = True, location='json')
        super(NavListApi,self).__init__()

    # 获取(查询)nav 列表
    def get(self):
        pass

    # 修改多个nav列表
    def post(self):
        pass

    # 增加多个列表
    def put(self):
        args = self.reqparse.parse_args()
        return {"data":args}
    # 删除多个列表
    def delete(self):
        pass
