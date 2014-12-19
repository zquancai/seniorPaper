# encoding: utf-8
# 转换成合适的用户表数据
__author__ = 'stardust'
import test.WeiboSpider.MySQLOperator
import re
import json

def getDataFromDB():
    sql = """SELECT * FROM testrepostrelation"""
    mop = test.WeiboSpider.MySQLOperator.MySQLOP()
    data_arr = mop.fetchArr(sql)
    data_list = []
    for i in range(0,len(data_arr)):
        data_item = []
        for j in range(0,len(data_arr[i])):
            data_item.append(data_arr[i][j])
        data_item.append("@"+data_arr[i][2]+"@"+data_arr[i][3])
        data_list.append(data_item)
    return data_list


def buildWeiboPath(data_list):
    new_data_list = []
    for t in range(0,len(data_list)):
        item = data_list[t]
        mother_path = item[3]
        for i in range(0,len(data_list)):
            father_path = data_list[i][6]
            if mother_path == father_path:
                item.append(data_list[i][5])
                break
            else:
                if i == len(data_list) - 1:
                    item.append('')
        new_data_list.append(item)
        print '已经生成第'+str(t)+"个father转发id..." #7
    return new_data_list

def insertIntoSQLDB(rName,data_list):
    for i in range(0,len(data_list)):
        rootstatusID ="'" + data_list[i][1] + "'"
        rootUserName = "'" + rName +"'"
        parentstatusID = data_list[i][7]
        if parentstatusID == '':
            # 一重转发，父微博id为根微博id
            parentstatusID = rootstatusID
        else:
            parentstatusID = "'"+parentstatusID+"'"
        parentuserName = data_list[i][3]
        if parentuserName == '':
            #一重转发,父用户名为根用户名
            parentuserName = rootUserName
        else:
            # 多重转发
            regex = '@([^@]{0,30})@'
            p = re.compile(regex)
            res = p.findall(parentuserName)
            if len(res)>0:
                parentuserName = "'"+res[0]+"'"
            else:
                parentuserName = '。。。。。。。。。。。。。。。。没有用户名。。。。。。。。。。。。'

        selfstatusID = "'"+data_list[i][5]+"'"
        selfuserName = "'"+data_list[i][2]+"'"

        #sql
        sql = """INSERT INTO relationship(rootstatusID,rootuserName,parentstatusID,parentuserName,selfstatusID,selfuserName)
                 VALUES ("""+rootstatusID+""","""+rootUserName+""","""+parentstatusID+""","""+parentuserName+""","""+selfstatusID+""","""+selfuserName+""")"""
        MySQLOperator = test.WeiboSpider.MySQLOperator
        mop = MySQLOperator.MySQLOP()
        mop.ExcuteSQL(sql)

def getRootWeiboName(mid):
    token = '2.009HsraD0vuTD36b3ccb26b1gs4dHE'
    client = test.WeiboSpider.userInfo.weiboClient.APIClient()
    data = client.getWeiboInfoFromWeiboMid(mid,token)
    jdata = data['data']
    name = str(json.loads(jdata)['user']['screen_name'])
    return name

def mainFunc():
    # 生成转发表
    data_list = getDataFromDB()
    data_clean_list = buildWeiboPath(data_list)
    rootUserName = getRootWeiboName(data_clean_list[0][1])
    insertIntoSQLDB(rootUserName,data_clean_list)


# # 生成转发表
# data_list = getDataFromDB()
# data_clean_list = buildWeiboPath(data_list)
# rootUserName = getRootWeiboName(data_clean_list[0][1])
# insertIntoSQLDB(rootUserName,data_clean_list)