# encoding: utf-8
__author__ = 'stardust'
import MySQLOperator

sql = '''TRUNCATE TABLE `testtopiclist`'''
mop = MySQLOperator.MySQLOP()
mop.ExcuteSQL(sql)
print '清除数据表成功！'