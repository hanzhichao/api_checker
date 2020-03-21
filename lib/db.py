import pymysql

from conf import config


def get_conn():
    conn = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db,
                           charset='utf8')
    return conn

def db_query(sql):
    config.logging.debug(sql)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    config.logging.debug(result)  # todo 使用logging方法
    cur.close()
    conn.close()
    return result


def db_change(sql):
    config.logging.debug(sql)  # todo 使用logging方法
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()  # 提交修改
    except Exception as e:
        config.logging.error(repr(e))  # 打印错误信息 todo logging
        conn.rollback()  # 回滚修改
    finally:
        cur.close()
        conn.close()

def check_user(name):
    result = db_query("select * from user where name='%s'" % name)
    return True if result else False

def del_user(name):
    db_change("delete from user where name = '{}'".format(name))


if __name__ == "__main__": # 用来判断是不是从当前模块执行的
    # print(check_user("张三"))
    get_conn()
