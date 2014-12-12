# encoding: utf-8
# 操作mysql数据库
__author__ = 'stardust'

import MySQLdb

class MySQLOP:

    db = None

    def __init__(self):
        print 'initial...'
        self.OpenDB()

    def __del__(self):
        print 'deleting....'
        self.CloseDB()

    def OpenDB(self):
        print 'opening db'
        self.db = MySQLdb.connect('localhost','root','','seniorPaper')

    def CloseDB(self):
        self.db.close()

    def ExcuteSQL(self,sql):
        cursor = self.db.cursor()
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           self.db.commit()
           print 'success'
        except:
           # Rollback in case there is any error
           self.db.rollback()
           print 'error'





