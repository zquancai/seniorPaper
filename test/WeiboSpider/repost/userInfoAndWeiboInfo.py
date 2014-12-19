# encoding: utf-8
# 获取微博信息表和用户信息表
__author__ = 'stardust'

import test.WeiboSpider.userInfo.weiboClient
import test.WeiboSpider.MySQLOperator

def getWeiboJsonData(mid):
    client = test.WeiboSpider.userInfo.weiboClient.APIClient()
    data = client.getWeiboInfoFromWeiboMid(mid)
    return data

def getWeiboMid():
    sql = '''SELECT distinct selfstatusID FROM relationship '''
    mop = test.WeiboSpider.MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data

def getRootWeiboMid():
    sql = '''SELECT distinct rootstatusID FROM relationship '''    mop = test.WeiboSpider.MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data

# 获取根weibo信息
def getRootWeiboInfo():
    rootmid_arr = getRootWeiboMid()
    for i in range(0,len(rootmid_arr)):
        rootmid = rootmid_arr[i]
        data = getWeiboJsonData(rootmid)
        # deal with the data
        
        # insert into table

def getChildWeiboInfo():
    mid_arr = getWeiboMid()
    for i in range(0,len(mid_arr)):
        mid = mid_arr[i]
        data = getWeiboJsonData(mid)

        # deal with the data

        # insert into table


# root node
getRootWeiboInfo()
# child node
#getChildWeiboInfo()

