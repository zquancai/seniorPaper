# encoding: utf-8
__author__ = 'stardust'
import sys
sys.path.append('../')
import MySQLOperator

def matchRegisterTime(rtime):
    t_time = int(rtime)
    t_2010 = 1262275200
    t_2011 = 1293811200
    t_2012 = 1325347200
    t_2013 = 1356969600
    t_2014 = 1388505600
    t_2015 = 1420041600
    if t_time < t_2010:
        return 2009
    elif t_time < t_2011:
        return 2010
    elif t_time < t_2012:
        return 2011
    elif t_time < t_2013:
        return 2012
    elif t_time < t_2014:
        return 2013
    elif t_time < t_2015:
        return 2014
    else:
        return 2015

mop = MySQLOperator.MySQLOP()
w_2009 = 0
w_2010 = 0
w_2011 = 0
w_2012 = 0
w_2013 = 0
w_2014 = 0
w_2015 = 0
sql = """SELECT createdAt FROM userinfo group by UserID"""
registerTimeArr = mop.fetchArr(sql)
for i in range(0,len(registerTimeArr)):
    singleTime = matchRegisterTime(registerTimeArr[i][0])
    if singleTime == 2009:
        w_2009 = w_2009 + 1
    elif singleTime == 2010:
        w_2010 = w_2010 + 1
    elif singleTime == 2011:
        w_2011 = w_2011 + 1
    elif singleTime == 2012:
        w_2012 = w_2012 + 1
    elif singleTime == 2013:
        w_2013 = w_2013 + 1
    elif singleTime == 2014:
        w_2014 = w_2014 + 1
    else:
        w_2015 = w_2015 + 1

print '2009 :' + str(w_2009)
print '2010 :' + str(w_2010)
print '2011 :' + str(w_2011)
print '2012 :' + str(w_2012)
print '2013 :' + str(w_2013)
print '2014 :' + str(w_2014)
print '2015 :' + str(w_2015)