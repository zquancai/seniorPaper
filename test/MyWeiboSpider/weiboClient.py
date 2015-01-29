# encoding: utf-8
# 使用：1、手动输入token到token.txt
#      2、实例化，如a = APIClient()
#      3、调用函数

__version__ = '1.0.0'
__author__ = 'Jack Li(britzlieg@gmail.com)'
import urllib2
import urllib
import json

# 常数定义,使用别人的key和secrect
CLIENT_ID = '1244782104'  #这个貌似未认证。。。,所以只能用自己的测试账号2390635102@qq.com 19920430
CLIENT_SERCRET ='2482495e4fa525e21153b910c1febaa3'
REDIRECT_URI ='http://www.baidu.com'
BASEURL='https://api.weibo.com/2/'
ACCESSTOKENURL='https://api.weibo.com/oauth2/access_token'
AUTHORIZEURL='https://api.weibo.com/oauth2/authorize'
RMURL='https://rm.api.weibo.com/2/'
CODE = 'd0fad9aa9c8d69174ebcd98fba736136'
access_token_file_path = 'token.txt'  #保存的token文件，需要手动输入(方便)

errorDict = {'code':'-1'}
successDict = {'code':'1'}

# 获取代理服务器地址
import MySQLOperator
def getProxyServerList():
    sql = '''SELECT distinct ip,proxy FROM proxylist '''
    mop = MySQLOperator.MySQLOP()
    data = mop.fetchArr(sql)
    return data


class APIClient:
    # 认证函数，暂时不需要
    def getAUTHORIZE(self):
        values = {'client_id':CLIENT_ID,'client_secret':CLIENT_SERCRET,'grant_type':'authorization_code','code':CODE,'redirect_uri':REDIRECT_URI}
        postdata = urllib.urlencode(values)
        postdata = postdata.encode('utf-8')
        request = urllib2.Request(ACCESSTOKENURL)
        f = urllib2.urlopen(request,postdata)
        r_data = f.read().decode('utf-8')
        token_data = json.loads(r_data)["access_token"]
        self.saveToken(token_data)
        #print(r_data)
    def saveToken(self,token):
        f = open(access_token_file_path, 'w')
        f.write(token)
        f.close()
    def getToken(self):
        f = open(access_token_file_path, 'r')
        token = f.read()
        return token

    # 接口访问模板
    def reqTpl(self,url,dict,type):
        theURL = url
        data = None
        codeInfo = None
        resdata = '{}'
        proxyServerArr = getProxyServerList()

        for k in range(0,len(proxyServerArr)):
            proxy = urllib2.ProxyHandler({'http': proxyServerArr[k][0]})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

            if type == 'get':
                length = len(dict.keys())
                counter = 0
                if length > 0:
                    theURL = theURL + '?'
                for key in dict.keys():
                    theURL = theURL + '%s=%s'%(key,dict[key])
                    counter = counter + 1
                    if counter == length:
                        pass
                    else:
                        theURL = theURL + '&&'


                request = urllib2.Request(theURL)
                #print(theURL)
                try:
                    resdata = urllib2.urlopen(request, timeout=5).read().decode('utf-8')
                    codeInfo = successDict
                except:
                    codeInfo = errorDict

            elif type == 'post':
                postdata = None
                for key in dict.keys():
                     postdata = urllib.urlencode({key,dict[key]})
                request = urllib2.Request(theURL)
                try:
                    resdata = urllib2.urlopen(request,postdata).read().decode('utf-8')
                    codeInfo = successDict
                except:
                    codeInfo = errorDict
            # 判断信息是否获取到
            if resdata != '{}':
                break


        data = {'data':resdata}
        data.update(codeInfo)
        return data

    # 获取最新的公共微博json字符串
    def getPublicWeibo(self):
        count = '200'
        url = 'https://api.weibo.com/2/statuses/public_timeline.json'
        dict = {'access_token':self.getToken(),'count':count}
        reposedata = self.reqTpl(url,dict,'get')
        thedata = reposedata['data']
        print(thedata)


    # 获取一小时内热门话题
    def getHourly(self):
        url = 'https://api.weibo.com/2/trends/hourly.json'
        dict = {'access_token':self.getToken()}
        reposedata = self.reqTpl(url,dict,'get')
        thedata = reposedata['data']
        trends = json.loads(thedata)['trends']
        print(trends)
        return trends

    # 获取一天热门话题
    def getDaily(self):
        url = 'https://api.weibo.com/2/trends/daily.json'
        dict = {'access_token':self.getToken()}
        reposedata = self.reqTpl(url,dict,'get')
        thedata = reposedata['data']
        trends = json.loads(thedata)['trends']
        print(trends)
        return trends

    # 获取一周热门话题
    def getWeekly(self):
        url = 'https://api.weibo.com/2/trends/weekly.json'
        dict = {'access_token':self.getToken()}
        reposedata = self.reqTpl(url,dict,'get')
        thedata = reposedata['data']
        trends = json.loads(thedata)['trends']
        print(trends)
        return trends

    def getUserInfo(self,userId):
        url = 'https://api.weibo.com/2/users/show.json'
        dict = {'access_token':self.getToken(),'uid':userId}
        reposedata = self.reqTpl(url,dict,'get')
        thedata = reposedata['data']
        return thedata

    def getWeiboInfoFromWeiboMid(self,mid,token):
        url = 'https://api.weibo.com/2/statuses/show.json'
        dict = {'access_token':token,'id':mid}
        reposedata = self.reqTpl(url,dict,'get')
        return reposedata

