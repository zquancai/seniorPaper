# encoding: utf-8
# 测试微博登陆成功，爬取一个测试网页

import cookielib
import urllib2
import TopicRegex
import common
import threading
import time
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
def getPageList(page):
    # 前十位是精确到秒的时间戳
    # 构造时间戳
    timestamp = common.getCurrentTimeStamp() + '999990'
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

# 参数
timer = 2.0
couter = 3 #运行小时数
pageCout = 4

mop = MySQLOperator.MySQLOP()
for i in range(0,couter):
    for j in range(0,pageCout):
        print '-----------------------------------------'
        htm = getPageList(j+1)
        writeData(htm)
        print 'couter:'+str(i)+' pager:'+str(j)
        data = TopicRegex.startRegex(htm)
        print '-----------------------------------------'
        # d_titleName = "'哈哈'"
        # d_rank = "'哈哈'"
        # d_classify = "'哈哈'"
        # d_timestamp = "'哈哈'"
        # d_postManName = "'哈哈'"
        # d_postManLink = "'哈哈'"
        # d_titleLink = "'哈哈'"
        # d_haveRead = "'哈哈'"
        #
        # sql = """INSERT INTO testtopiclist(d_titleName,
        #      d_rank, d_classify, d_timestamp, d_postManName,d_postManLink,d_titleLink,d_haveRead)
        #      VALUES ("""+d_titleName+""", """+d_rank+""", """+d_classify+""", """+d_timestamp+""", """+d_postManName+""", """+d_postManLink+""", """+d_titleLink+""", """+d_haveRead+""")"""
        # print sql
        # mop.ExcuteSQL(sql)


        threading._sleep(timer)




