#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 16:37
# File    : settings.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/FullFlask?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号;
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass
