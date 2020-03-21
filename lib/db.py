import logging
import pymysql
from config import config


def get_db_con():
    con = pymysql.connect(host=config.host, port=config.port,
                        user=config.user, passwd=config.password,
                        db=config.database)

    return con


def query_db(sql):
    con = get_db_con()
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data


def change_db(sql):
    con = get_db_con()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        logging.info(sql)
        con.commit()
    except Exception as e:
        con.rollback()
        logging.error(e.message)

if __name__ == "__main__":
    sql = "show tables"
    print(change_db(sql))
    #print(query_db(sql))




