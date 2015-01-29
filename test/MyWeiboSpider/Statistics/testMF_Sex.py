# encoding: utf-8
__author__ = 'stardust'
import sys
sys.path.append('../')
import MySQLOperator

mop = MySQLOperator.MySQLOP()
man_count = 0
woman_count = 0
sql = """SELECT Gender FROM userinfo group by UserID"""

personGenderArr = mop.fetchArr(sql)

for i in range(0,len(personGenderArr)):
    single_gender = personGenderArr[i][0]
    if single_gender == 'm':
        man_count = man_count + 1
    elif single_gender == 'f':
        woman_count = woman_count + 1
    else:
        print '性别未知'

print 'man:' + str(man_count)
print 'woman:' + str(woman_count)

# import urllib2
#
# proxy = urllib2.ProxyHandler({'http': '211.141.130.245:8118'})
# opener = urllib2.build_opener(proxy)
# urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com')
# print response.read()

