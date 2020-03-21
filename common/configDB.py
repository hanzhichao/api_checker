"""数据库操作"""

import pymysql
import sys
sys.path.append("..")
import readConfig as readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class MyDB(object):
    global host, username, password, port, database, readConfig
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'db': database
    }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def connectDB(self):
        try:
            self.db = pymsql.connect(**config)
            self.cursor = self.db.cursor()
            print("连接数据库成功")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        self.cursor = excute(sql, params)
        self.db.commit()
        return self.cursor

    def get_all(sefl, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("数据库关闭")
