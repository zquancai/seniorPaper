# encoding: utf-8
__author__ = 'stardust'
import sys
sys.path.append('../')
import MySQLOperator
import re

mop = MySQLOperator.MySQLOP()
sql = """SELECT Location FROM userinfo group by UserID"""
statusCountArr = mop.fetchArr(sql)

province = [
'北京 '
,
'陕西 '
,
'广东 '
,
'湖南 '
,
'广西 '
,
'上海 '
,
'山东 '
,
'湖北 '
,
'福建 '
,
'辽宁 '
,
'浙江 '
,
'海外 '
,
'河南 '
,
'四川 '
,
'黑龙江 '
,
'河北 '
,
'江苏 '
,
'海南 '
,
'重庆 '
,
'天津 '
,
'宁夏 '
,
'香港 '
,
'安徽 '
,
'内蒙古 '
,
'山西 '
,
'云南 '
,
'澳门 '
,
'新疆 '
,
'贵州 '
,
'甘肃 '
,
'江西 '
,
'吉林 '
,
'青海 '
,
'台湾 '
,
'西藏 '
]
# 初始化数据
mansNum = []
for k in range(0,len(province)):
    mansNum.append(0)

# step 1 生成省份列表，边查边生成
# step 2 生成省份数据

for i in range(0,len(statusCountArr)):
    singleLocation = statusCountArr[i][0]
    regex = '[^\x00-\xff]{1,10} '
    p = re.compile(regex)
    res = p.findall(singleLocation)
    if len(res) > 0:
        data = res[0]
        for j in range(0,len(province)):
            if data == province[j]:
                mansNum[j] = mansNum[j] + 1

# 显示和保存数据
map_data = '['
for t in range(0,len(mansNum)):
    print province[t] + " : " + str(mansNum[t])
    # 生成数据格式
    singleData = "{name:"+"'"+province[t][0:-1]+"'"+",value:"+str(mansNum[t])+"}"
    map_data = map_data + singleData
    if t < len(mansNum) - 1:
        map_data = map_data + ","
map_data = map_data + ']'

# 写入文件
f = open('mapdata.txt','w')
f.write(map_data)
f.close()


# print '['
# for j in range(0,len(province)):
#     print "'"+province[j]+"'"
#     if j < len(province) - 1:
#         print ','
# print ']'
