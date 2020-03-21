import logging
import unittest
import ddt
import requests
from config import  db_config
from lib.db import DB
from lib.excel import Excel
from lib.utils import json2dict


excel = Excel("data.xls")
case_list = excel.get_sheet_data("添加加油卡")


@ddt.ddt
class TestAddFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DB(db_config)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    @ddt.data(*case_list)
    def test_add_fuel_card(self, case_data):
        case_id, title = int(case_data[0]), case_data[1]
        logging.info("执行第{}条用例: {}".format(case_id, title))

        method,  url, headers, data = case_data[2], case_data[3], json2dict(case_data[4]), json2dict(case_data[5])
        logging.info("method: {}, url: {}, headers: {}, data: {}".format(method, url, headers, data))

        setup_sql, expect = case_data[6], json2dict(case_data[7])

        self.db.execute(setup_sql)

        res = requests.request(method, url, headers=headers, json=data)
        self.assertEqual(expect, res.json())


if __name__ == '__main__':
    unittest.main()
