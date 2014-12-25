# encoding: utf-8
# 公共函数
__author__ = 'stardust'

import time
import datetime


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

def sinaTime_to_timestamp(sinatime):
    aTimestamp = time.mktime(time.strptime(sinatime,"%a %b %d %H:%M:%S +0800 %Y"))
    return str(int(aTimestamp))

