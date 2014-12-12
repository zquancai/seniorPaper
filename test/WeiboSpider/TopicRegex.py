# encoding: utf-8
# 此文件函数用于筛选话题内容

__author__ = 'stardust'

import re
import common
import Queue


d_titleName = []
d_rank = []
d_haveRead = []
d_classify = []
d_timestamp = []
d_postManName = []
d_postManLink = []
d_titleLink = []

d_cell = []


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
    _titleName = []
    for i in range(0,len(res)):
        # d_titleName.append(res[i])
        _titleName.append(res[i])
    return _titleName


# topic rank
def getTopicRank(data):
    regex = '(<span class=\\\\"DSC_topicon)(' \
            '_red|_orange)?(\\\\">)(TOP)?(.{0,' \
            '5})(<\\\\/span>)'
    p = re.compile(regex)
    res = p.findall(data)
    _rank = []
    for i in range(0,len(res)):
        #d_rank.append(res[i][4])
        _rank.append(res[i][4])
    return _rank



# topic classify
def getTopicClassify(data,celldata):
    regex = '(<\\\\/span>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t)(.{0,20})(\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/div>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<div class=\\\\"subtitle\\\\">)'
    p = re.compile(regex)
    res = p.findall(data)
    _classify = []
    for i in range(0,len(res)):
        # d_classify.append(res[i][1])
        _classify.append(res[i][1])
    if len(res) < len(celldata):
        # 存在没有分类
        print '--》分类缺失'
        _classify = reGetClassify(celldata,_classify)
    return _classify


# topic time
def getTopicTimestamp(celldata):
    _timestamp = []
    for i in range(0,len(celldata)):
        #d_timestamp.append(common.getCurrentTimeStamp())
        _timestamp.append(common.getCurrentTimeStamp())
    return _timestamp

# postman name
def getPostManName(data,celldata):
    _postManName = []
    regex = 'from=faxian_huati\\\\" class=\\\\"tlink S_txt1\\\\"   >\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,50})\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        _postManName.append(res[i])

    if len(res) < len(celldata):
        # 存在没有主持人的话题
        print '--》主持人缺失'
        _postManName = reGetPostManName(celldata,_postManName)
    return _postManName


# postman link
def getPostManLink(data,celldata):
    regex = '<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/u\\\\/(\d{0,30})'
    _postManLink = []
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        _postManLink.append(res[i])

    if len(res) < len(celldata):
        # 存在没有主持人的话题
        print '--》主持人link缺失'
        _postManLink = reGetPostManLink(celldata,_postManLink)
    return _postManLink

# 话题链接
def getTopicLink(data):
    regex = '(<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/p\\\\/)(.{0,150})(\?)'
    p = re.compile(regex)
    res = p.findall(data)
    _titleLink = []
    for i in range(0,len(res)):
        # d_titleLink.append('http://weibo.com/p/'+res[i][1])
        _titleLink.append('http://weibo.com/p/'+res[i][1])
    return _titleLink

# read cout
def getTopicReadCount(data):
    regex = '(<span class=\\\\"number\\\\">)(.{0,20})(万|亿)?'
     #'(<span class=\\"number\\">).{0,20}(万|亿)'  #
     # 不知道为什么这个正确的反而不行，‘\’问题太大，需要注意
    p = re.compile(regex)
    res = p.findall(data)
    _haveRead = []
    for i in range(0,len(res)):
        # d_haveRead.append(res[i][1] + res[i][2])
        _haveRead.append(res[i][1] + res[i][2])
    return _haveRead

# cell getter
def _getCell(data):
    regex = '<li class=\\\\"pt_li S_line2\\\\" (.{0,5000})<\\\\/li>'
    # regex = '<div class=\\\\"subinfo clearfix\\\\">\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,1000})\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/div>'
    p = re.compile(regex)
    res = p.findall(data)
    t_cell = []
    for i in range(0,len(res)):
        t_cell.append(res[i])
    return t_cell

# rebuild the data
def rebuildData(d_titleName,d_rank,d_classify,d_timestamp,d_postManName,d_postManLink,d_titleLink,d_haveRead):
    topicList = []
    couter = 0

    for i in range(0,len(d_titleName)):
        aTopicItem = {'d_titleName':d_titleName[i],
              'd_rank':d_rank[i],
              'd_classify':d_classify[i],
              'd_timestamp':d_timestamp[i],
              'd_postManName':d_postManName[i],
              'd_postManLink':d_postManLink[i],
              'd_titleLink':d_titleLink[i],
              'd_haveRead':d_haveRead[i]
              }
        topicList.append(aTopicItem)
        couter = couter + 1
    return topicList

# 重新组合 分类
def reGetClassify(cellData,t_classify):
    print '重组-分类'
    for i in range(0,len(cellData)):
        aCelldata = cellData[i]
        regex = 'bpfilter' #'<a bpfilter=\\\\"page(.{0,300})\\\\/a>'
        p = re.compile(regex)
        res = p.findall(aCelldata)
        if len(res)<1:
            t_classify.insert(i,'')
    # for j in range(0,len(cellData)):
    #     print t_classify[j]
    return t_classify

# 重新组合 主持人和主持人链接
def reGetPostManName(cellData,t_postmanName):
    print '重组-主持人Name'
    for i in range(0,len(cellData)):
        aCelldata = cellData[i]
        #regex = 'from=faxian_huati\\\\" class=\\\\"tlink S_txt1\\\\"   >\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,50})\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>'
        regex = '<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/u\\\\/(\d{0,30})'
        p = re.compile(regex)
        res = p.findall(aCelldata)
        if len(res) < 1:
            t_postmanName.insert(i,'')
    # for j in range(0,len(cellData)):
    #     print t_postmanName[j]
    return t_postmanName

def reGetPostManLink(cellData,t_postmanLink):
    print '重组-主持人link'
    for i in range(0,len(cellData)):
        aCelldata = cellData[i]
        #regex = 'from=faxian_huati\\\\" class=\\\\"tlink S_txt1\\\\"   >\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,50})\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>'
        regex = '<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/u\\\\/(\d{0,30})'
        p = re.compile(regex)
        res = p.findall(aCelldata)
        if len(res) < 1:
            t_postmanLink.insert(i,'')
    # for j in range(0,len(cellData)):
    #     print t_postmanLink[j]
    return t_postmanLink

# the door function
def startRegex(data):
    # 获取cell
    d_cell = _getCell(data)

    d_titleName = getTitleName(data)
    d_rank = getTopicRank(data)
    d_classify = getTopicClassify(data,d_cell)
    d_timestamp = getTopicTimestamp(d_cell)
    d_postManName = getPostManName(data,d_cell)
    d_postManLink = getPostManLink(data,d_cell)
    d_titleLink = getTopicLink(data)
    d_haveRead = getTopicReadCount(data)

    return rebuildData(d_titleName,d_rank,d_classify,d_timestamp,d_postManName,d_postManLink,d_titleLink,d_haveRead)
