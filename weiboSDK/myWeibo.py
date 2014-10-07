__version__ = '1.0.0'
__author__ = 'Jack Li(britzlieg@gmail.com)'
import urllib.parse
import urllib.request
import json

# 常数定义
CLIENT_ID = '1244782104'  #这个貌似未认证。。。,所以只能用自己的测试账号2390635102@qq.com 19920430
CLIENT_SERCRET ='2482495e4fa525e21153b910c1febaa3'
REDIRECT_URI ='http://www.baidu.com'
BASEURL='https://api.weibo.com/2/'
ACCESSTOKENURL='https://api.weibo.com/oauth2/access_token'
AUTHORIZEURL='https://api.weibo.com/oauth2/authorize'
RMURL='https://rm.api.weibo.com/2/'
CODE = 'd0fad9aa9c8d69174ebcd98fba736136'
access_token_file_path = 'token.txt'

class APIClient:
    def getAUTHORIZE(self):
        postdata = urllib.parse.urlencode({'client_id':CLIENT_ID,'client_secret':CLIENT_SERCRET,'grant_type':'authorization_code','code':CODE,'redirect_uri':REDIRECT_URI})
        postdata = postdata.encode('utf-8')
        request = urllib.request.Request(ACCESSTOKENURL)
        f = urllib.request.urlopen(request,postdata)
        r_data = f.read().decode('utf-8')
        token_data = json.loads(r_data)["access_token"]
        self.saveToken(token_data)
        print(r_data)
    def saveToken(self,token):
        f = open(access_token_file_path, 'w')
        f.write(token)
        f.close()
    def getToken(self):
        f = open(access_token_file_path, 'r')
        token = f.read()
        return token
    # 获取最新的公共微博json字符串
    def getPublicWeibo(self):
        count = '200'
        url = 'https://api.weibo.com/2/statuses/public_timeline.json'
        targetUrl = '%s?%s=%s&&count=%s'%(url,'access_token',self.getToken(),count)
        request = urllib.request.Request(targetUrl)
        try:
            d = urllib.request.urlopen(request)
            data = d.read()
            return data
        except:
            return '获取公共微博失败'
        
a = APIClient()

