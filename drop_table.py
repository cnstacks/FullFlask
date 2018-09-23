#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 17:08
# File    : drop_table.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
1、Web运行时候，flask程序运行起来，用户通过浏览器访问；
2、离线脚本，即自定义的一个py文件+使用flask中定义好的功能；
"""
from FullFlask import db
from FullFlask import create_app
from FullFlask import models

app = create_app()
with app.app_context():
    # db.drop_all()
    # db.create_all()
    data = db.session.query(models.Users).all()
    print(data)
