# encoding: utf-8
__author__ = 'stardust'
import sys
sys.path.append('../')
import MySQLOperator

mop = MySQLOperator.MySQLOP()
sql = """SELECT statusesCount,favourites_count FROM userinfo group by UserID"""
statusCountArr = mop.fetchArr(sql)

# 微博数
w_less50 = 0
w_50_100 = 0
w_101_500 = 0
w_501_2000 = 0
w_2001_5000 = 0
w_more5001 = 0
for i in range(0,len(statusCountArr)):
    single_statusCount = int(statusCountArr[i][0])
    if single_statusCount < 50:
        w_less50 = w_less50 + 1
    elif single_statusCount < 101:
        w_50_100 = w_50_100 + 1
    elif single_statusCount < 501:
        w_101_500 = w_101_500 + 1
    elif single_statusCount < 2001:
        w_501_2000 = w_501_2000 + 1
    elif single_statusCount < 5001:
        w_2001_5000 = w_2001_5000 + 1
    else:
        w_more5001 = w_more5001 + 1
print '------------------------微博数-------------------------'
print '少于50 : ' + str(w_less50)
print '50~100 : ' + str(w_50_100)
print '101~500 : ' + str(w_101_500)
print '501~2000 : ' + str(w_501_2000)
print '2001~5000 : ' + str(w_2001_5000)
print '超过5000 : ' + str(w_more5001)
print '------------------------------------------------------'

# 收藏数
w_less50 = 0
w_50_100 = 0
w_101_500 = 0
w_501_2000 = 0
w_2001_5000 = 0
w_more5001 = 0
for i in range(0,len(statusCountArr)):
    single_statusCount = int(statusCountArr[i][1])
    if single_statusCount < 50:
        w_less50 = w_less50 + 1
    elif single_statusCount < 101:
        w_50_100 = w_50_100 + 1
    elif single_statusCount < 501:
        w_101_500 = w_101_500 + 1
    elif single_statusCount < 2001:
        w_501_2000 = w_501_2000 + 1
    elif single_statusCount < 5001:
        w_2001_5000 = w_2001_5000 + 1
    else:
        w_more5001 = w_more5001 + 1

print '------------------------收藏数-------------------------'
print '少于50 : ' + str(w_less50)
print '50~100 : ' + str(w_50_100)
print '101~500 : ' + str(w_101_500)
print '501~2000 : ' + str(w_501_2000)
print '2001~5000 : ' + str(w_2001_5000)
print '超过5000 : ' + str(w_more5001)
print '------------------------------------------------------'