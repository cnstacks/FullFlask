#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 15:51
# File    : manage.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from FullFlask import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    # app.run()
    manager.run()
