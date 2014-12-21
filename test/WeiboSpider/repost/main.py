# encoding: utf-8
# 主函数
__author__ = 'stardust'
import test.WeiboSpider.repost.translateToTable
import test.WeiboSpider.repost.userInfoAndWeiboInfo
import test.WeiboSpider.repost.repostTable
import test.WeiboSpider.WeiboLogin

# # 先登录
# weiboLogin = test.WeiboSpider.WeiboLogin.WeiboLogin('2390635102@qq.com', '19920430')#邮箱（账号）、密码
# if weiboLogin.Login() == True:
#     print "登陆成功！"

#微博id
v_id = '3789806842405654' # 四六级
test.WeiboSpider.repost.repostTable.mainFunc(v_id)
test.WeiboSpider.repost.translateToTable.mainFunc()
test.WeiboSpider.repost.userInfoAndWeiboInfo.mainFunc()