# encoding: utf-8
# 主函数
__author__ = 'stardust'
import test.WeiboSpider.repost.translateToTable
import test.WeiboSpider.repost.userInfoAndWeiboInfo
import test.WeiboSpider.repost.repostTable

# 微博id
v_id = '3789191009547348'
test.WeiboSpider.repost.repostTable.mainFunc(v_id)
test.WeiboSpider.repost.translateToTable.mainFunc()
test.WeiboSpider.repost.userInfoAndWeiboInfo.mainFunc()