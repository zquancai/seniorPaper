__version__ = '1.0.0'
__author__ = 'Jack Li(britzlieg@gmail.com)'
import urllib.parse
import urllib.request
import json

# 常数定义
CLIENT_ID = '3104686382'
CLIENT_SERCRET ='abf00732481e4bb63b9ea4288249ac29'
REDIRECT_URI ='http://www.baidu.com'
BASEURL='https://api.weibo.com/2/'
ACCESSTOKENURL='https://api.weibo.com/oauth2/access_token'
AUTHORIZEURL='https://api.weibo.com/oauth2/authorize'
RMURL='https://rm.api.weibo.com/2/'
CODE = 'cfd66b9bb56655db80acc57a84a425cc'
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

a = APIClient()
print(a.getToken())
