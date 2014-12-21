# encoding: utf-8
# 记录转发关系
# 不知道为什么要将cookie手动放入，路径问题暂时无法解决
__author__ = 'stardust'
import test.WeiboSpider.MySQLOperator
import test.WeiboSpider.common
import urllib2
import cookielib
import re
import json
import threading



import sys
sys.path.append('C:\\Users\\stardust\\Desktop\\project\\seniorPaper\\test\\WeiboSpider')
sys.path.append('../')


cookie_savaPath = 'myLoginCookie.txt'
temp_save = 'temp_repost.html'

def writeData(data):
    file = open(temp_save,'w')
    file.write(data)
    file.close()

def openData():
    file = open(temp_save,'r')
    data = file.read()
    file.close()
    return data

# get the html of repost
def getRepostHtml(w_id,pg):
    url = 'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id='+w_id+'&page='+str(pg)
    request = urllib2.Request(url)
    ckjar = cookielib.MozillaCookieJar(cookie_savaPath)
    ckjar.load(ignore_discard=True, ignore_expires=True)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
    f = opener.open(request)
    htm = f.read()
    f.close()
    writeData(htm)

    # htm = openData()
    return htm

#获取转发的微博id
def test_getMids(data):
    regex = """<div class="list_li S_line1 clearfix" mid="(.\d{0,30})" action-type="feed_list_item" >"""
    p = re.compile(regex)
    res = p.findall(data)
    mid_arr = []
    # 含有热门推荐
    if(len(res)>20):
        for i in range(len(res)-20,len(res)):
            mid_arr.append(res[i])
    else:
        for i in range(0,len(res)):
            mid_arr.append(res[i])
    return mid_arr

# 获取总页数
def test_getTotalPage(data):
    return json.loads(data)['data']['page']['totalpage']

# 解析用户id
def test_getUserId(data):
    regex = 'usercard="id=(.\d{0,30})"><img src="'
    p = re.compile(regex)
    res = p.findall(data)
    uid_arr = []
        # 含有热门推荐
    if(len(res)>20):
        for i in range(len(res)-20,len(res)):
            uid_arr.append(res[i])
    else:
        for i in range(0,len(res)):
            uid_arr.append(res[i])
    return uid_arr

def test_getName(data):
    regex = 'node-type="name">(.{0,50})</a>'
    p = re.compile(regex)
    res = p.findall(data)
    name_arr = []
    # 含有热门推荐
    if(len(res)>20):
        for i in range(len(res)-20,len(res)):
            name_arr.append(res[i])
    else:
        # if len(res) < 20:
        #     print data

        for i in range(0,len(res)):
            name_arr.append(res[i])
    return name_arr

def test_getAddText(data):
    text_regex = """<span node-type="text">([\s\S]*?)</span>"""
    #text_regex = '<span node-type="text">(.{0,20000})</span>'
    text_p = re.compile(text_regex)
    text_res = text_p.findall(data)
    # 过滤热门转发
    text_arr = []
    # 含有热门推荐
    if(len(text_res)>20):
        for i in range(len(text_res)-20,len(text_res)):
            text_arr.append(text_res[i])
    else:
        # if len(text_res) < 20:
        #     print data

        for i in range(0,len(text_res)):
            text_arr.append(text_res[i])
    return text_arr

# 获取转发子节点
def test_getRepostChild(text_arr):
    child_arr = []
    #regex = '>@(.{0,50})</a>'
    regex = '//<a target="_blank" render="ext" extra-data="type=atname" (.{0,120})>@(.{0,50})</a>'
    #regex = '//<a target="_blank" render="ext" extra-data="type=atname" (.{0,120})'
    p = re.compile(regex)
    for i in range(0,len(text_arr)):
        child_res = p.findall(text_arr[i])
        if len(child_res) == 0:
            # 没有匹配项，一级转发
            child_arr.append('')
        elif len(child_res) == 1:
            # 只有一个匹配项,二级转发
            child_arr.append('@' + child_res[0][1] + '@')
        else:
            # 多个匹配项，多级转发
            childs_temp = ''
            for j in range(0,len(child_res)):
                childs_temp = childs_temp + '@' + child_res[j][1] + '@'
            child_arr.append(childs_temp)
    return child_arr





def jsonToHtml(data):
    return json.loads(data)['data']['html']


def _getData(weibo_id,fromPage):
    # 参数
    sleepTime = 0.0

    # page 1
    data = getRepostHtml(weibo_id,1)
    totalPage = test_getTotalPage(data)

    for j in range(fromPage,totalPage+1):
        print '正在抓取第'+str(j) + "页数据"
        temp_data = getRepostHtml(weibo_id,j)
        temp_data = jsonToHtml(temp_data)
        temp_name_arr = test_getName(temp_data)
        temp_uids_arr = test_getUserId(temp_data)
        temp_text_arr = test_getAddText(temp_data)
        temp_childRepost_arr = test_getRepostChild(temp_text_arr)
        temp_mids_arr = test_getMids(temp_data)

        # 每爬一页插入一次
        insertData(temp_name_arr,weibo_id,temp_uids_arr,temp_childRepost_arr,temp_mids_arr)

        threading._sleep(sleepTime)



def insertData(names_arr,weibo_id,uids_arr,childRepost_arr,mid_arr):
    mop = test.WeiboSpider.MySQLOperator.MySQLOP()
    weibo_id = "'"+weibo_id+"'"
    for i in range(len(names_arr)):
        name = "'"+names_arr[i]+"'"
        uid = "'"+uids_arr[i]+"'"
        repost = "'"+childRepost_arr[i]+"'"
        mid = "'"+mid_arr[i]+"'"
        sql = """INSERT INTO testrepostrelation(weibo_id,reposterName,repostRelation,reposterId,mid)
                 VALUES ("""+weibo_id+""","""+name+""","""+repost+""","""+uid+""","""+mid+""")"""
        mop.ExcuteSQL(sql)
    print 'done...'


def mainFunc(weiboId,fromPage):
    _getData(weiboId,fromPage)

mainFunc('3789806842405654',721)