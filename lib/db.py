import logging
import pymysql


class DB(object):
    def __init__(self, db_config):
        self.conn = pymysql.connect(**db_config, autocommit=True)
        self.cur = self.conn.cursor()

    def execute(self, sql):
        if sql:
            logging.debug("执行SQL: {}".format(sql))
            try:
                self.cur.execute(sql)
            except pymysql.err.ProgrammingError as ex:
                logging.error("SQL语法错误: 执行SQL-{} 错误信息-{}".format(sql, ex))
            except pymysql.err.InternalError as ex:
                logging.error("SQL执行错误: 执行SQL-{} 错误信息-{}".format(sql, ex))
            result = self.cur.fetchall()
            logging.debug("数据结果: {}".format(result))
            return result

    def close(self):
        self.conn.close()
