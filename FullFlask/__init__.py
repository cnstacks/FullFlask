#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 15:51
# File    : __init__.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 包含了SQLAlchemy相关的所有操作；
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    from .views.accounts import ac
    app.register_blueprint(ac)

    db.init_app(app)
    return app
