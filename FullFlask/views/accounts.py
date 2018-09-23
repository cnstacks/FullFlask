#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 15:54
# File    : accounts.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import blueprints

ac = blueprints.Blueprint('ac', __name__)


@ac.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login it.'
