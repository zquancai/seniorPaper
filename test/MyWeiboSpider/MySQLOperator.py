# encoding: utf-8
# 操作mysql数据库
__author__ = 'stardust'

import MySQLdb
import sys
# 保证python默认编码是utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

def fmt(row):
    return row

def singleRow(aArrary,rowsLen,j):
    rowsStr = "("
    for k in range(0,rowsLen):
        if k == 0:
            rowsStr = rowsStr + fmt(aArrary[j][k])
        else:
            rowsStr = rowsStr + "," + fmt(aArrary[j][k])
    rowsStr = rowsStr + ")"
    return rowsStr

class MySQLOP:

    db = None
    sql = None

    def __init__(self):
        self.OpenDB()

    def __del__(self):
        self.CloseDB()

    def OpenDB(self):
        self.db = MySQLdb.connect('localhost','root','','seniorPaper',charset='utf8')

    def CloseDB(self):
        self.db.close()

    def ExcuteSQL(self,sql):
        cursor = self.db.cursor()
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           self.db.commit()

        except:
           # Rollback in case there is any error
           self.db.rollback()
           print 'error:'+sql

    def fetchArr(self,sql):
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
           print 'error:'
           return None

    def insertWithTableAndArr(self,aTable,aRows,aArrary,aNumLimit):
        sql_tp1_1 = """INSERT INTO """ + aTable
        # 字段
        rowsLen = len(aRows)
        ziduan = ''
        for i in range(0,rowsLen):
            if i == 0:
                ziduan = aRows[0]
            else:
                ziduan = ziduan + ',' + aRows[i]
        sql_tp1_2 = "("+ziduan+")" + "VALUES"
        # 字段值
        rowsStr = ''
        for j in range(0,len(aArrary)):
            if j == 0:  # 第一个
                rowsStr = singleRow(aArrary,rowsLen,j)
            elif (((j % aNumLimit == 0)and(j != 0)) or j==len(aArrary)-1):  # 到达设定的最大值
                sql_tp1_3 = rowsStr
                # 拼接
                sql_tpl = sql_tp1_1 + sql_tp1_2 + sql_tp1_3
                # 执行
                self.ExcuteSQL(sql_tpl)
                rowsStr = singleRow(aArrary,rowsLen,j)
            else:
                rowsStr = rowsStr + "," + singleRow(aArrary,rowsLen,j)




