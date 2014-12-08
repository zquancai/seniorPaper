# encoding: utf-8
__author__ = 'stardust'

import WeiboEncode
import WeiboSearch
import urllib2
import cookielib

# cookie 保存路径
cookie_savaPath = 'myLoginCookie.txt'

def writeData(data,output_fileName):
    file = open(output_fileName,'w')
    file.write(data)
    file.close()



class WeiboLogin:
    def __init__(self, user, pwd, enableProxy = False):
        print "Initializing WeiboLogin..."
        self.userName = user
        self.passWord = pwd
        self.enableProxy = enableProxy

        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}

        self.getCookieUrl = ''

    def Login(self):
        self.EnableCookie(self.enableProxy)#cookie或代理服务器配置
        serverTime, nonce, pubkey, rsakv = self.GetServerTime()#登陆的第一步
        postData = WeiboEncode.PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#加密用户和密码
        print "Post data length:\n", len(postData)

        req = urllib2.Request(self.loginUrl, postData, self.postHeader)
        print "Posting request..."
        result = urllib2.urlopen(req)#登陆的第二步——解析新浪微博的登录过程中3
        text = result.read()
        try:
            loginUrl = WeiboSearch.sRedirectData(text)#解析重定位结果
            # ff = urllib2.urlopen(loginUrl).read().decode('utf-8')

            # save cookie
            postdata = ''
            headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'}
            request = urllib2.Request(loginUrl, postdata, headers)
            ckjar = cookielib.MozillaCookieJar(cookie_savaPath)
            ckproc = urllib2.HTTPCookieProcessor(ckjar)
            opener = urllib2.build_opener(ckproc)
            f = opener.open(request)
            htm = f.read().decode('utf-8')
            f.close()
            ckjar.save(ignore_discard=True, ignore_expires=True)
        except:
            print 'Login error!'
            return False

        print 'Login sucess!'
        return True

    def EnableCookie(self, enableProxy):
        cookiejar = cookielib.LWPCookieJar()#建立cookie
        cookie_support = urllib2.HTTPCookieProcessor(cookiejar)

        if enableProxy:
            proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})#使用代理
            opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
            print "Proxy enabled"
        else:
            opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

        urllib2.install_opener(opener)#构建cookie对应的opener

    def GetServerTime(self):
        print "Getting server time and nonce..."
        serverData = urllib2.urlopen(self.serverUrl).read()#得到网页内容
        print serverData
        try:
            serverTime, nonce, pubkey, rsakv = WeiboSearch.sServerData(serverData)#解析得到serverTime，nonce等
            return serverTime, nonce, pubkey, rsakv
        except:
            print 'Get server time & nonce error!'
            return None



if __name__ == '__main__':
    weiboLogin = WeiboLogin('2390635102@qq.com', '19920430')#邮箱（账号）、密码
    if weiboLogin.Login() == True:
        print "登陆成功！"