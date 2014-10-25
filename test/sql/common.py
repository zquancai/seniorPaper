# 初始化文件,导入pymysql
import sys
# 添加环境路径，便于加载模块
# win8
sys.path.append('D:\\MyCode\\seniorPaper\\sina mining\\seniorPaper\\PyMySQL-master')
# OSX
sys.path.append('/Users/stardust/seniorPaper/PyMySQL-master')

import pymysql
class pySql(object):
    conn = None
    cur = None
    def __init__(self):
        pass
    def close(self):
        if self.conn:
            self.conn.close()
    def connect(self):
        try:
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='test')
            cur = conn.cursor()
            return True
        except:
            return False
    def execute(self,sql):
        try:
            if(self.cur.execute(sql)):
                self.cur.execute("commit")  #这一句这么重要。。。
        except:
            sys.exit("MySQL Query Error_excute:\n"+sql+"\n")
    def insert(self,table,row):
        sqlArr = []
        for key in row.keys():
            sqlArr.append("%s='%s'"%(key,row[key],))
        sql = "INSERT INTO "+table +" SET "+str.join(",",sqlArr)
        return self.execute(sql)

    def update(self,table,row,where):
        sqlArr = []
        for key in row.keys():
            sqlArr.append("%s='%s'"%(key,row[key],))
        sql = "update "+table +" set "+str.join(",",sqlArr)+" where "+where
        return self.execute(sql)
    def quote(self,queryString):
        return pymysql.escape_string(queryString)
    def query(self,sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor
        except:
            sys.exit("MySQL Query Error_query:\n"+sql+"\n")
    def fetch(self,cursor):
        return cursor.fetchone()

    def fetchRow(self,sql):
        return self.query(sql).fetchone()

    def fetchOne(self,sql):
        try:
            return self.query(sql).fetchone()[0]
        except:
            return None

    def fetchAll(self,sql):
        return self.query(sql).fetchall()

a = pySql()
a.connect()
row = {"id":"","name":"jack"}
a.insert('testTable',row)
a.close()
