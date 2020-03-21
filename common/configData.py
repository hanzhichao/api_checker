"""从tesFile目录下的excel文件中读取测试用例，从DB.xml中读取sql"""
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree

import sys
sys.path.append("..")
from common.Log import MyLog as Log
from common import configHttp
from readConfig import proDir

localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()


#从excel中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    file = open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# 从xml中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sqlPath = os.path.join(proDir, 'testFile', "SQL.xml")
        tree = ElementTree.parse(sqlPath)
        for db in tree.findall("database"):
            db_name = db.get("name")
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql


if __name__ == "__main__":
    print(get_xls("shopCase.xlsx", 'matchStation'))