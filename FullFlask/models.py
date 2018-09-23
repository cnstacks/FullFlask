#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FullFlask 
# Software: PyCharm
# Time    : 2018-09-23 16:11
# File    : models.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index, DateTime, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=True, unique=True)


def init_db():
    # 数据库连接相关;
    engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/FullFlask?charset=utf8")
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine("mysql+pymysql://root:Tqtl911!@%*)@mysql.cuixiaozhao.com:3306/FullFlask?charset=utf8")
    # 删除表;
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # drop_db()
    init_db()
