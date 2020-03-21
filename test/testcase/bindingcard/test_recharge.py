# -*- coding: utf-8 -*
import unittest
import requests
import os
import logging
import json
from lib import case_log
from config.config import datapath
from lib import readexceldata


class Recharge(unittest.TestCase):
    """加油卡chongzhi"""

    def setUp(self):
        f = os.path.join(datapath, '接口测试用例.xls')
        self.data_list = readexceldata.excel_to_list(f, "Recharge")

    def test_recharge_ok(self):
        """充值成功"""
        data = readexceldata.get_test_data('test_recharge_ok', self.data_list)
        case_log.case_log(data)
        url = data['url']
        input_args = data['input_args']
        expire_result = data['expire_result']
        r = requests.post(url,data=input_args)
        logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    def test_no_exist_cardnumber_recharge(self):
        """加油卡号不存在"""
        data = readexceldata.get_test_data('test_no_exist_cardnumber_recharge', self.data_list)
        case_log.case_log(data)
        url = data['url']
        input_args = data['input_args']
        expire_result = data['expire_result']
        r = requests.post(url,data=input_args)
        logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)