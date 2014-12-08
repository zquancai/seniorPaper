# encoding: utf-8
# 测试微博登陆成功，爬取一个测试网页
import urllib
import cookielib
import urllib2

target_url = 'http://weibo.com/'
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


# 测  试
postdata = ''
headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'}
request = urllib2.Request(target_url, postdata, headers)

ckjar = cookielib.MozillaCookieJar(cookie_savaPath)
ckjar.load(ignore_discard=True, ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))

f = opener.open(request)
htm = f.read()
f.close()
writeData(htm)

