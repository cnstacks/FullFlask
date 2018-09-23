#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 15:51
# File    : __init__.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask
from .views.accounts import ac


def create_app():
    app = Flask(__name__)
    app.register_blueprint(ac)
    return app
