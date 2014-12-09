# encoding: utf-8
# 此文件函数用于筛选话题内容

__author__ = 'stardust'

import re
import common

d_titleName = []
d_rank = []
d_haveRead = []
d_classify = []
d_timestamp = []
d_postManName = []
d_postManLink = []
d_titleLink = []

# topic count
def getTopicCount(data):
    regex = '"#(.{0,100})#'
    p = re.compile(regex)
    res = p.findall(data)
    return len(res)

# 话题列表名
def getTitleName(data):
    regex = '"#(.{0,100})#'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_titleName.append(res[i])
        print res[i]

# topic rank
def getTopicRank(data):
    regex = '(<span class=\\\\"DSC_topicon)(' \
            '_red|_orange)?(\\\\">)(TOP)?(.{0,' \
            '5})(<\\\\/span>)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_rank.append(res[i][4])

# topic classify
def getTopicClassify(data):
    regex = '(<\\\\/span>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t)(.{0,20})(\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/div>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<div class=\\\\"subtitle\\\\">)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_classify.append(res[i][1])

# topic time
def getTopicTimestamp():
    for i in range(0,len(d_titleName)):
        d_timestamp.append(common.getCurrentTimeStamp())

# postman name
def getPostManName(data):
    regex = 'from=faxian_huati\\\\" class=\\\\"tlink S_txt1\\\\"   >\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,50})\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_postManName.append(res[i])

# postman link
def getPostManLink(data):
    regex = '<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/u\\\\/(\d{0,30})'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_postManLink.append('http://weibo.com/u/'+res[i])

# 话题链接
def getTopicLink(data):
    regex = '(<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/p\\\\/)(.{0,150})(\?)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_titleLink.append('http://weibo.com/p/'+res[i][1])

# read cout
def getTopicReadCount(data):
    regex = '(<span class=\\\\"number\\\\">)(.{0,20})(万|亿)'
     #'(<span class=\\"number\\">).{0,20}(万|亿)'  #
     # 不知道为什么这个正确的反而不行，‘\’问题太大，需要注意
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        d_haveRead.append(res[i][1] + res[i][2])

# rebuild the data
def rebuildData():
    topicList = []
    for i in range(0,len(d_titleName)):
        aTopicItem = {'d_titleName':d_titleName[i],
                      'd_rank':d_rank[i],
                      'd_classify':d_classify[i],
                      'd_timestamp':d_timestamp[i],
                      'd_postManName':d_postManName[i],
                      'd_postManLink':d_postManLink[i],
                      'd_titleLink':d_titleLink[i],
                      'd_haveRead':d_haveRead
                      }
        topicList.append(aTopicItem)
    return topicList

# the door function
def startRegex(data):
    getTitleName(data)
    getTopicRank(data)
    getTopicClassify(data)
    getTopicTimestamp()
    getPostManName(data)
    getPostManLink(data)
    getTopicLink(data)
    getTopicReadCount(data)
    return rebuildData()

