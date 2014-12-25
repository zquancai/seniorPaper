# encoding: utf-8
__author__ = 'stardust'
__function__ = '获取用户数据'

import weiboClient
import test.WeiboSpider.MySQLOperator
import test.WeiboSpider.common
import threading
import unicodedata

# 获取最新数据库中已存在的用户id
def getExitUserIds():
    sql = '''SELECT u_userId FROM testuserinfo '''
    MySQLOperator = test.WeiboSpider.MySQLOperator
    mop = MySQLOperator.MySQLOP()
    exitUserId_Arr = mop.fetchArr(sql)
    return exitUserId_Arr

# 获取话题注册人id
def getTopicUserIds():
    sql = """SELECT d_postManLink FROM testtopiclist"""
    MySQLOperator = test.WeiboSpider.MySQLOperator
    mop = MySQLOperator.MySQLOP()
    topicUserId_Arr = mop.fetchArr(sql)
    return topicUserId_Arr

# 插入用户信息
def insertUserInfo(uid,userJson):
    uid = "'"+uid+"'"
    userJson = "'"+userJson+"'"
    timestamp = "'"+test.WeiboSpider.common.getCurrentTimeStamp()+"'"
    sql = """INSERT INTO testuserinfo(u_userId,u_userJson,u_timestamp)
                 VALUES ("""+uid+""","""+userJson+""","""+timestamp+""")"""
    MySQLOperator = test.WeiboSpider.MySQLOperator
    mop = MySQLOperator.MySQLOP()
    mop.ExcuteSQL(sql)

# 转化成字符串
def transIntoStr(unicode_Arr):
    arr = []
    for row in unicode_Arr:
        aStr = row[0]
        aStr = aStr.encode('ascii', 'ignore')
        arr.append(aStr)
    return arr


def getUserInfo():
    # 获取用户数据
    topicUserList = transIntoStr(list(set(getTopicUserIds())))
    defaultUserList = transIntoStr(list(set(getExitUserIds())))
    counter = 0
    sleepTime = 0.1  # 调用sdk的不用设置睡眠时间
    for row in topicUserList:
        counter = counter + 1
        topic_uid = row
        print "总共有"+str(len(topicUserList))+"个用户数据---->正在刷新第"+str(counter+1)+"个用户"
        topic_uid = topic_uid.encode('ascii', 'ignore')
        if topic_uid in defaultUserList:
            print '---------------------------->'
            continue
        else:
            aWeiboClient = weiboClient.APIClient()
            u_info = aWeiboClient.getUserInfo(topic_uid)
            insertUserInfo(topic_uid,u_info)
            defaultUserList = getExitUserIds()
        threading._sleep(sleepTime)

getUserInfo()


