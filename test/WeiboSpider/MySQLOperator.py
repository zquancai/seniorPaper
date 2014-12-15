# encoding: utf-8
# 操作mysql数据库
__author__ = 'stardust'

import MySQLdb
import sys
# 保证python默认编码是utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

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
        self.db = MySQLdb.connect('localhost','root','','seniorPaper',charset='utf8')

    def CloseDB(self):
        self.db.close()

    def ExcuteSQL(self,sql):
        cursor = self.db.cursor()
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           self.db.commit()

        except:
           # Rollback in case there is any error
           self.db.rollback()
           print 'error:'+sql

    def fetchArr(self,sql):
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
           print 'error:'+sql
           return None

