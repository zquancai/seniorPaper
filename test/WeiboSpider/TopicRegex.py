# encoding: utf-8
# 此文件函数用于筛选话题内容

__author__ = 'stardust'

import re
import common
import Queue


d_titleName = Queue.Queue()
d_rank = Queue.Queue()
d_haveRead = Queue.Queue()
d_classify = Queue.Queue()
d_timestamp = Queue.Queue()
d_postManName = Queue.Queue()
d_postManLink = Queue.Queue()
d_titleLink = Queue.Queue()



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
        # d_titleName.append(res[i])
        d_titleName.put(res[i])
# topic rank
def getTopicRank(data):
    regex = '(<span class=\\\\"DSC_topicon)(' \
            '_red|_orange)?(\\\\">)(TOP)?(.{0,' \
            '5})(<\\\\/span>)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        #d_rank.append(res[i][4])
        d_rank.put(res[i][4])

# topic classify
def getTopicClassify(data):
    regex = '(<\\\\/span>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t)(.{0,20})(\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/div>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<div class=\\\\"subtitle\\\\">)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        # d_classify.append(res[i][1])
        d_classify.put(res[i][1])



# topic time
def getTopicTimestamp():
    for i in range(0,d_titleName.qsize()):
        #d_timestamp.append(common.getCurrentTimeStamp())
        d_timestamp.put(common.getCurrentTimeStamp())


# postman name
def getPostManName(data):
    regex = 'from=faxian_huati\\\\" class=\\\\"tlink S_txt1\\\\"   >\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t(.{0,50})\\\\t\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        #d_postManName.append(res[i])
        d_postManName.put(res[i])

# postman link
def getPostManLink(data):
    regex = '<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/u\\\\/(\d{0,30})'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        # d_postManLink.append('http://weibo.com/u/'+res[i])
        d_postManLink.put('http://weibo.com/u/'+res[i])

# 话题链接
def getTopicLink(data):
    regex = '(<a target=\\\\"_blank\\\\" href=\\\\"http:\\\\/\\\\/weibo.com\\\\/p\\\\/)(.{0,150})(\?)'
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        # d_titleLink.append('http://weibo.com/p/'+res[i][1])
        d_titleLink.put('http://weibo.com/p/'+res[i][1])

# read cout
def getTopicReadCount(data):
    regex = '(<span class=\\\\"number\\\\">)(.{0,20})(万|亿)?'
     #'(<span class=\\"number\\">).{0,20}(万|亿)'  #
     # 不知道为什么这个正确的反而不行，‘\’问题太大，需要注意
    p = re.compile(regex)
    res = p.findall(data)
    for i in range(0,len(res)):
        # d_haveRead.append(res[i][1] + res[i][2])
        d_haveRead.put(res[i][1] + res[i][2])

# rebuild the data
def rebuildData():
    topicList = Queue.Queue()

    couter = 0
    print d_titleName.qsize()
    print d_rank.qsize()
    print d_classify.qsize()
    print d_timestamp.qsize()
    print d_postManName.qsize()
    print d_postManLink.qsize()
    print d_titleLink.qsize()
    print d_haveRead.qsize()

    while not d_titleName.empty():
        a = d_titleName.get()

        aTopicItem = {'d_titleName':a,
              'd_rank':d_rank.get(),
              'd_classify':d_classify.get(),
              'd_timestamp':d_timestamp.get(),
              'd_postManName':d_postManName.get(),
              'd_postManLink':d_postManLink.get(),
              'd_titleLink':d_titleLink.get(),
              'd_haveRead':d_haveRead.get()
              }
        print 'couter:'+str(couter)+' '+a
        # d_titleName.task_done()
        # d_rank.task_done()
        # d_classify.task_done()
        # d_timestamp.task_done()
        # d_postManName.task_done()
        # d_postManLink.task_done()
        # d_titleLink.task_done()
        # d_haveRead.task_done()
        topicList.put(aTopicItem)
        couter = couter + 1
    print topicList.qsize()
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
