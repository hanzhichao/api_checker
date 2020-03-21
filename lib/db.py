import pymysql
import sys
sys.path.append("..")

from config.config import *

def get_db_conn():
    conn = pymysql.connect(host=db_host,port=db_port,user=db_user,password=db_password, db=db)
    return conn

def query_db(sql):
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    logging.debug(result)
    return result

def change_db(sql):
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def add_user(name, password):
    sql = "insert into user (name,passwd) values ('{}','{}')".format(name,password)
    change_db(sql)

def check_user(name):
    sql = "select * from user where name = '{}'".format(name)
    return query_db(sql)

def del_user(name):
    sql = 'delete from user where name = "{}"'.format(name)
    change_db(sql)

if __name__ == "__main__":
    # add_user('abc','123456')
    del_user('abc')
    print(check_user('abc'))

