# encoding: utf-8
# 主函数
# 整个程序分为三个模块：登陆模块，热门话题模块，转发关系模块
# 1.登陆模块
#     构成文件："Login_"前缀的3个文件,模块的主文件是Login_WeiboLogin.py
#
# 2.热门话题模块
#     构成文件："Topic_"前缀的2个文件
#
# 3.转发关系模块
#     构成文件："Repost_"前缀的三个文件

# 整个操作过程如下：

__author__ = 'stardust'

import Login_WeiboLogin
import Topic_getHotTopic
import Topic_userInfoGetter
import Repost_repostNode
import Repost_repostTable
import Repost_userInfoAndWeiboInfo


def func(val):
    # 热门话题
    # 热门话题主持人信息
    if val == 1:
        Topic_getHotTopic.mainFunc()
        Topic_userInfoGetter.mainFunc()

    # 所有转发用户和微博
    elif val == 2:
        mids = ['3792721146228563','3792863789713311',
                '3793017061814327','3792715437203513',
                '3792732063042123']
        for i in range(0,len(mids)):
            mid = mids[i]     # 微博id
            fromPage = 1 # 从第几页开始
            endPage = -1 # 少于0为全部-1
            betweenPage = 1 #隔页
            Repost_repostTable.mainFunc(mid,fromPage,endPage,betweenPage)

        Repost_repostNode.mainFunc()
        # 先爬所有网页数据  然后再调
        # api
        #Repost_userInfoAndWeiboInfo.mainFunc()
    else:
        return


# 登陆获取cookie
#Login_WeiboLogin.mainFunc()

# 通过不同值调用func函数执行相关功能
func(2)