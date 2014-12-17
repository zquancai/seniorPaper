# encoding: utf-8
# 记录转发关系
__author__ = 'stardust'
import test.WeiboSpider.MySQLOperator
import test.WeiboSpider.common
import urllib2
import cookielib
import re
import json

import sys
sys.path.append('C:\\Users\\stardust\\Desktop\\project\\seniorPaper\\test\\WeiboSpider')
reload(sys)


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

# 解析页面的htmlcell
# def getRegexRepostCell(data):
#     regex = """<div class="list_li S_line1 clearfix" mid="(.\d{0,30})" action-type="feed_list_item" >([\s\S]{0,3000})</div>"""
#     p = re.compile(regex)
#     res = p.findall(data)
#
#     cell_arr = []
#     for i in range(0,len(res)):
#         cell_data = res[i][1]
#         cell_arr.append(cell_data)
#     return cell_arr

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
        for i in range(0,len(res)):
            name_arr.append(res[i])
    return name_arr

def test_getAddText(data):
    text_regex = '<span node-type="text">(.{0,4000})</span>'
    text_p = re.compile(text_regex)
    text_res = text_p.findall(data)
    # 过滤热门转发
    text_arr = []
    # 含有热门推荐
    if(len(text_res)>20):
        for i in range(len(text_res)-20,len(text_res)):
            text_arr.append(text_res[i])
    else:
        for i in range(0,len(text_res)):
            text_arr.append(text_res[i])
    return text_arr

# 获取转发子节点
def test_getRepostChild(text_arr):
    child_arr = []
    regex = '>@(.{0,50})</a>'
    p = re.compile(regex)
    for i in range(0,len(text_arr)):
        child_res = p.findall(text_arr[i])
        if len(child_res) == 0:
            # 没有匹配项，一级转发
            child_arr.append('')
        elif len(child_res) == 1:
            # 只有一个匹配项,二级转发
            child_arr.append(child_res[0])
        else:
            # 多个匹配项，多级转发
            childs_temp = ''
            for j in range(0,len(child_res)):
                childs_temp = childs_temp + '@' + child_res[j] + '@'
            child_arr.append(childs_temp)
    return child_arr





def jsonToHtml(data):
    return json.loads(data)['data']['html']

# page 1
weibo_id = '3788546231751806'
data = getRepostHtml(weibo_id,1)
totalPage = test_getTotalPage(data)

htmldata = jsonToHtml(data)
name_arr = test_getName(htmldata)
uids_arr = test_getUserId(htmldata)
text_arr = test_getAddText(htmldata)
childRepost_arr = test_getRepostChild(text_arr)
for t in range(0,len(childRepost_arr)):
    print childRepost_arr[t]

# for j in range(2,totalPage+1):
#     temp_data = getRepostHtml(weibo_id,j)
#     temp_data = jsonToHtml(temp_data)
#     temp_name_arr = test_getName(temp_data)
#     name_arr = name_arr + temp_name_arr
#
# for k in range(0,len(name_arr)):
#     print "第"+str(k+1)+"个 ："+name_arr[k]