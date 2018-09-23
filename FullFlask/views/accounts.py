#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 15:54
# File    : accounts.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import blueprints
from FullFlask import models

ac = blueprints.Blueprint('ac', __name__)


@ac.route('/login', methods=['GET', 'POST'])
def login():
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/FullFlask?charset=utf8")
    maker = sessionmaker(bind=engine)
    session = maker()
    result = session.query(models.Users).all()
    session.close()
    print(
        result)  # [<FullFlask.models.Users object at 0x106123c88>, <FullFlask.models.Users object at 0x106123dd8>, <FullFlask.models.Users object at 0x106123a90>, <FullFlask.models.Users object at 0x1061239e8>]

    return 'Login it.'
