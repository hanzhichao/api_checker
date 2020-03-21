"""
1. 从config文件读取配置
2. 连接数据库
3. 执行sql并返回结果
"""
import pymysql

import sys
sys.path.append("..")
from util.config import Config

class DB():
    def __init__(self):
        cf = Config()
        self.conn = pymysql.connect(host=cf.get_db('db_host'),
                                    port=int(cf.get_db('db_port')),
                                    db=cf.get_db('db_name'),
                                    user=cf.get_db('db_user'),
                                    passwd=cf.get_db('db_passwd'),
                                    charset='utf8')
        self.cur = self.conn.cursor()
    
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def exec_sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()



if __name__ == '__main__':
    db = DB()
    print(db.exec_sql("select * from user where name='张三'"))