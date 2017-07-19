#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql

class IzakayaSQLhelper:

    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host='192.168.8.28',
                                     user='root',
                                     password='54152067',
                                     db='crawl',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

    def insert(self,title,phone,address):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 插入语句
        sql = "INSERT INTO Izakaya(title,phone,address) VALUES (%s, %s,%s)"
        param = (title,phone,address)
        try:
           # 执行sql语句
           cursor.execute(sql,param)
           # 提交到数据库执行
           self.db.commit()
        except:
           # 如果发生错误则回滚
           self.db.rollback()

        # 关闭数据库连接
        self.db.close()

    def select(self,title):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 插入语句
        sql = "SELECT * FROM  Izakaya  WHERE title=%s ORDER BY ID DESC LIMIT 5"
        param = (title)


        try:
           # 执行sql语句
           cursor.execute(sql,param)
           results = cursor.fetchone()
           print (results)
           return results
           # 提交到数据库执行
           # self.db.commit()
        except:
           # 如果发生错误则回滚
           self.db.rollback()

        # 关闭数据库连接
        self.db.close()