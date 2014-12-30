# encoding: utf-8
# 获取微博信息表和用户信息表，
__author__ = 'stardust'

import weiboClient
import MySQLOperator
import common
import json
import threading
import re


token2 = '2.009HsraD0vuTD36b3ccb26b1gs4dHE'
token = '2.009HsraDigyO3Bcfc27562c30xrfIr'


# 获取地址数据
def getAddressArr():
    sql = '''SELECT distinct address,longitude,latitude FROM changelocation '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data


# 获取经度
def getJingDu(address_arr,address):
    for i in range(0,len(address_arr)):
        if address == address_arr[i][0]:
            return str(address_arr[i][1])
    return '0'

# 获取纬度
def getWeiDu(address_arr,address):
    for i in range(0,len(address_arr)):
        if address == address_arr[i][0]:
            return str(address_arr[i][2])
    return '0'

# 时间格式转换工具
def timeTranslator(atime):
    return atime

def favorTranlator(fav):
    if fav == True:
        return 'T'
    else:
        return 'F'

def sourceTranslator(source):
    if source != None:
        regex = '>(.*)<'
        p = re.compile(regex)
        res = p.findall(source)
        if len(res) > 0:
            return res[0]
        else:
            return ''
    else:
        return ''


def insertIntoWeiboStatusTable(jdata,address_arr):
    if jdata == '{}':
        print '无法获取微博数据'
        return

    Latitude ="'"+''+"'"
    Longitude ="'"+''+"'"
    Geo = ''#json.loads(jdata)['geo']
    Address ="'"+json.loads(jdata)['user']['location']+"'"
    Province ="'"+json.loads(jdata)['user']['province']+"'"
    City ="'"+json.loads(jdata)['user']['city']+"'"
    if Geo != None:
        Latitude = '1.1'
        Longitude ='1.1'
        Geo = "'"+'geo'+"'"
    else:
        Geo =  "'"+''+"'"
        Latitude = getWeiDu(address_arr,json.loads(jdata)['user']['location'])
        Longitude = getJingDu(address_arr,json.loads(jdata)['user']['location'])

    StatusID = "'"+json.loads(jdata)['mid']+"'"
    UserID ="'"+str(json.loads(jdata)['user']['id'])+"'"
    createdAt = "'"+timeTranslator(json.loads(jdata)['created_at'])+"'" #'2014-12-18 00:00:00'
    text =  "'"+''+"'"#"'"+json.loads(jdata)['text']+"'"
    source =  "'"+sourceTranslator(json.loads(jdata)['source'])+"'"
    favorited = "'"+favorTranlator(json.loads(jdata)['favorited'])+"'"
    retweetedStatusID ="'"+''+"'"
    repostsCount = "'"+str(int(json.loads(jdata)['reposts_count']))+"'"
    commentsCount = "'"+str(int(json.loads(jdata)['comments_count']))+"'"

    createAt_time = "'"+common.sinaTime_to_timestamp(timeTranslator(json.loads(jdata)['created_at']))+"'"

    sql = """INSERT INTO statusinfo(StatusID, Latitude, Longitude,Geo, Address, Province, City, UserID, createdAt, text, source, favorited, retweetedStatusID, repostsCount, commentsCount,createAt_time)
                 VALUES ("""+StatusID+""", """+Latitude+""", """+Longitude+""", """+Geo+""", """+Address+""", """+Province+""", """+City+""", """+UserID+""", """+createdAt+""", """+text+""", """+source+""", """+favorited+""", """+retweetedStatusID+""", """+repostsCount+""", """+commentsCount+""", """+createAt_time+""")"""

    MySQLOperator.MySQLOP().ExcuteSQL(sql)
    print 'status done'

def insertIntoUserTable(jdata,address_arr):
    if jdata == '{}':
        print '无法获取user数据'
        return
    UserID = "'"+str(json.loads(jdata)['user']['id'])+"'"
    Gender = "'"+str(json.loads(jdata)['user']['gender'])+"'"
    createdAt ="'"+common.sinaTime_to_timestamp(str(json.loads(jdata)['user']['created_at']))+"'"
    ScreenName ="'"+str(json.loads(jdata)['user']['screen_name'])+"'"
    Location ="'"+str(json.loads(jdata)['user']['location'])+"'"
    latitude ="'"+getWeiDu(address_arr,str(json.loads(jdata)['user']['location']))+"'"
    longitude ="'"+getJingDu(address_arr,str(json.loads(jdata)['user']['location']))+"'"
    Description ="'"+str(json.loads(jdata)['user']['description'])+"'"
    Url = "'"+str(json.loads(jdata)['user']['url'])+"'"
    profileImageUrl = "'"+str(json.loads(jdata)['user']['profile_image_url'])+"'"
    followersCount ="'"+str(json.loads(jdata)['user']['followers_count'])+"'"
    friendsCount = "'"+str(json.loads(jdata)['user']['friends_count'])+"'"
    statusesCount = "'"+str(json.loads(jdata)['user']['statuses_count'])+"'"
    followMe = "'"+''+"'"
    avatarLarge = "'"+str(json.loads(jdata)['user']['avatar_large'])+"'"
    onlineStatus = "'"+''+"'"
    originalStatusID = "'"+''+"'"
    sql = """INSERT INTO userinfo(UserID, Gender, createdAt, ScreenName, Location, latitude, longitude, Description, Url, profileImageUrl, followersCount, friendsCount, statusesCount, followMe, avatarLarge, onlineStatus, originalStatusID)
                 VALUES ("""+UserID+""", """+Gender+""", """+createdAt+""", """+ScreenName+""", """+Location+""", """+latitude+""", """+longitude+""", """+Description+""", """+Url+""", """+profileImageUrl+""", """+followersCount+""", """+friendsCount+""", """+statusesCount+""", """+followMe+""", """+avatarLarge+""","""+onlineStatus+""", """+originalStatusID+""")"""
    MySQLOperator.MySQLOP().ExcuteSQL(sql)
    print 'user done'

def getWeiboJsonData(mid,token):
    client = weiboClient.APIClient()
    data = client.getWeiboInfoFromWeiboMid(mid[0],token)
    return data

def getWeiboMid():
    sql = '''SELECT distinct selfstatusID FROM relationship '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data

def getRootWeiboMid():
    sql = '''SELECT distinct rootstatusID FROM relationship '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data

# 获取根weibo信息
def getRootWeiboInfo(address_arr):
    rootmid_arr = getRootWeiboMid()
    for i in range(0,len(rootmid_arr)):
        rootmid = rootmid_arr[i]
        # 判断根微博id是否已经存在微博表中
        db_data = getAllWeiboFromDB()
        if rootmid in db_data:
            continue

        data = getWeiboJsonData(rootmid,token)
        if data['code'] == '1':
            jdata = data['data']
            insertIntoWeiboStatusTable(jdata,address_arr)
            insertIntoUserTable(jdata,address_arr)
        else:
            print 'root weibo have been deleted!!!!!'
            return


def getChildWeiboInfo(start,address_arr):
    mid_arr = getWeiboMid()
    for i in range(start,len(mid_arr)):
        mid = mid_arr[i]
        # 判断根微博id是否已经存在微博表中
        db_data = getAllWeiboFromDB()
        if mid in db_data:
            continue

        data = getWeiboJsonData(mid,token)
        if data['code'] == '1':
            jdata = data['data']
            insertIntoWeiboStatusTable(jdata,address_arr)
            insertIntoUserTable(jdata,address_arr)
        else:
            data2 = getWeiboJsonData(mid,token2)
            if data2['code'] == '1':
                jdata = data['data']
                insertIntoWeiboStatusTable(jdata,address_arr)
                insertIntoUserTable(jdata,address_arr)
            else:
                print "第 "+str(i+1)+" 个失败！"


        threading._sleep(0.5)
        print "--->第 "+str(i+1)+" 个！"

# 从数据库中读取所有用户信息
def getAllUsersFromDB():
    print '获取All用户信息...'
    sql = '''SELECT distinct UserID FROM userinfo '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data

# 从数据库中读取所有微博信息
def getAllWeiboFromDB():
    print '获取All微博信息。。。'
    sql = '''SELECT distinct StatusID FROM statusinfo '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data


def mainFunc():
    address_arr = getAddressArr()
    getRootWeiboInfo(address_arr)
    # 从第几个用户开始
    getChildWeiboInfo(0,address_arr)

