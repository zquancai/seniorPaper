# encoding: utf-8
# 删除所有数据表（转发）
__author__ = 'stardust'
import test.WeiboSpider.MySQLOperator

sql1 = '''TRUNCATE TABLE `relationship`'''
sql2 = '''TRUNCATE TABLE `testrepostrelation`'''
sql3 = '''TRUNCATE TABLE `statusinfo`'''
sql4 = '''TRUNCATE TABLE `userinfo`'''
mop = test.WeiboSpider.MySQLOperator.MySQLOP()
mop.ExcuteSQL(sql1)
mop.ExcuteSQL(sql2)
mop.ExcuteSQL(sql3)
mop.ExcuteSQL(sql4)
print '清除数据表成功！'