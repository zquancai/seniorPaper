# encoding: utf-8
# 测试微博登陆成功，爬取一个测试网页
import urllib
import cookielib
import urllib2
# 前十位是精确到秒的时间戳
target_url = 'http://d.weibo.com/100803?from=page_100803&ajaxpagelet=1&__ref=/100803&_t=FM_141803819287940'
output_fileName = 'test_Login.txt'
login_url = ''
cookie_savaPath = 'myLoginCookie.txt'

# 写文件 包含 测试（test_前缀）
def writeData(data):
    file = open(output_fileName,'w')
    file.write(data)
    file.close()

def test_writeData():
    aStr = 'sdfadsakfjdsalfjldksa'
    writeData(aStr)


# 测  试 - get
request = urllib2.Request(target_url)

ckjar = cookielib.MozillaCookieJar(cookie_savaPath)
ckjar.load(ignore_discard=True, ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))

f = opener.open(request)
htm = f.read()
f.close()
writeData(htm)

