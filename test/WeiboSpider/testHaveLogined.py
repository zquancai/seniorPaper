# encoding: utf-8
# 测试微博登陆成功，爬取一个测试网页

import cookielib
import urllib2
import TopicRegex
import common
import threading
import MySQLOperator
import sys

# 保证python默认编码是utf-8
reload(sys)
sys.setdefaultencoding('utf-8')


output_fileName = 'test_Login.html'
login_url = ''
cookie_savaPath = 'myLoginCookie.txt'

# 写文件 包含 测试（test_前缀）
def writeData(data):
    file = open(output_fileName,'w')
    file.write(data)
    file.close()



# 测  试 - get
def getPageList(page,tstamp):
    # 前十位是精确到秒的时间戳
    # 构造时间戳
    timestamp = tstamp + '000001'#'999990'
    # target_url = 'http://d.weibo.com/100803?from=page_100803' \
    #              '&ajaxpagelet=1&__ref=/100803&_t=FM_'+timestamp
    target_url = 'http://d.weibo.com/100803?pids' \
                 '=Pl_Discover_Pt6Rank__5&cfs=920' \
                 '&Pl_Discover_Pt6Rank__5_filter' \
                 '=&Pl_Discover_Pt6Rank__5_page' \
                 '='+ str(page)+'&ajaxpagelet=1&__ref=/100803' \
                              '&_t' \
                          '=FM_' \
                       ''+timestamp
    request = urllib2.Request(target_url)
    ckjar = cookielib.MozillaCookieJar(cookie_savaPath)
    ckjar.load(ignore_discard=True, ignore_expires=True)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
    f = opener.open(request)
    htm = f.read()
    f.close()
    #print target_url
    return htm

def getHotTopic():
    #参数
    CounterTimer = 3600.0
    PagerTimer = 3.0
    couter = 24 #运行小时数
    pageCout = 4
    mop = MySQLOperator.MySQLOP()
    for i in range(0,couter):
        for j in range(0,pageCout):
            print '-----------------------------------------'
            curTimestamp = common.getCurrentTimeStamp()
            htm = getPageList(j+1,curTimestamp)
            writeData(htm)
            print '小时：'+str(i+1)+' pager:'+str(j+1)
            data = TopicRegex.startRegex(htm,curTimestamp)
            print '-----------------------------------------'
            for k in range(0,len(data)):
                d_titleName = "'"+data[k]['d_titleName']+"'"
                d_rank = "'"+data[k]['d_rank']+"'"
                d_classify = "'"+data[k]['d_classify']+"'"
                d_timestamp = "'"+data[k]['d_timestamp']+"'"
                d_postManName = "'"+data[k]['d_postManName']+"'"
                d_postManLink = "'"+data[k]['d_postManLink']+"'"
                d_titleLink = "'"+data[k]['d_titleLink']+"'"
                d_haveRead = "'"+data[k]['d_haveRead']+"'"

                sql = """INSERT INTO testtopiclist(d_titleName,
                     d_rank, d_classify, d_timestamp, d_postManName,d_postManLink,d_titleLink,d_haveRead)
                     VALUES ("""+d_titleName+""", """+d_rank+""", """+d_classify+""", """+d_timestamp+""", """+d_postManName+""", """+d_postManLink+""", """+d_titleLink+""", """+d_haveRead+""")"""

                mop.ExcuteSQL(sql)
            threading._sleep(PagerTimer)
        threading._sleep(CounterTimer)





# # 构造24小时数据
# sleepTime = 3.0
# pageCount = 1
# couterHour = 24
#
# #时间戳
# t_timestamp = common.getTimeStampArrFromTime('2014-12-14 9:00:00',couterHour)
# mop = MySQLOperator.MySQLOP()
# for i in range(0,couterHour):
#     for j in range(0,pageCount):
#         print '-----------------------------------------'
#         htm = getPageList(j+1,t_timestamp[i])
#         print '小时：'+str(i+1)+' pager:'+str(j+1)
#         data = TopicRegex.startRegex(htm,t_timestamp[i])
#         print '-----------------------------------------'
#         for k in range(0,len(data)):
#             d_titleName = "'"+data[k]['d_titleName']+"'"
#             d_rank = "'"+data[k]['d_rank']+"'"
#             d_classify = "'"+data[k]['d_classify']+"'"
#             d_timestamp = "'"+data[k]['d_timestamp']+"'"
#             d_postManName = "'"+data[k]['d_postManName']+"'"
#             d_postManLink = "'"+data[k]['d_postManLink']+"'"
#             d_titleLink = "'"+data[k]['d_titleLink']+"'"
#             d_haveRead = "'"+data[k]['d_haveRead']+"'"
#
#             sql = """INSERT INTO testtopiclist(d_titleName,
#                  d_rank, d_classify, d_timestamp, d_postManName,d_postManLink,d_titleLink,d_haveRead)
#                  VALUES ("""+d_titleName+""", """+d_rank+""", """+d_classify+""", """+d_timestamp+""", """+d_postManName+""", """+d_postManLink+""", """+d_titleLink+""", """+d_haveRead+""")"""
#
#             mop.ExcuteSQL(sql)
#
#         threading._sleep(sleepTime)
