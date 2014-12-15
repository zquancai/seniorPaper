# encoding: utf-8
# 公共函数
__author__ = 'stardust'

import time

def getCurrentTimeStamp():
    return str(int(time.time()))

# 从某个时间返回24小时每小时的时间戳
def getTimeStampArrFromTime(dateAndTime,couterHour):
    aTimestamp = time.mktime(time.strptime(dateAndTime,'%Y-%m-%d %H:%M:%S'))
    timeStampArr = []
    for i in range(0,couterHour):
        timeStampArr.append(str(int(aTimestamp)))
        aTimestamp = aTimestamp + 3600.0
        # print str(i) + ' ' + str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(aTimestamp)))
    return timeStampArr

# getTimeStampArrFromTime_24h('2011-09-28 10:00:00')
