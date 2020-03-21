import unittest
import requests
import os
import json
from lib import db, case_log
from config.config import datapath, logger


from lib import readexceldata


class BingdingCard(unittest.TestCase):
    """绑定加油卡"""

    def setUp(self):
        f = os.path.join(datapath, '接口测试用例.xls')
        self.data_list = readexceldata.excel_to_list(f, "BingdingCard")

    def test_no_exist_third_bound(self):
        """不存在第三方编号绑定失败"""
        data = readexceldata.get_test_data('test_no_exist_third_bound', self.data_list)
        case_log.case_log(data)
        url = data['url']
        input_args = data['input_args']
        expire_result = data['expire_result']
        r = requests.post(url,data=input_args)
        logger.info("响应内容:%s" % r.text)
        self.assertEqual( r.json(), json.loads(expire_result))

    def test_no_exist_cardnumber_bound(self):
        """错误卡号绑定失败"""
        data = readexceldata.get_test_data('test_no_exist_cardnumber_bound', self.data_list)
        case_log.case_log(data)
        url = data['url']
        input_args = data['input_args']
        expire_result = data['expire_result']
        r = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % r.text)
        self.assertEqual(r.json(), json.loads(expire_result))

    def tearDown(self):
        pass


class BingdingCardOk(unittest.TestCase):
    """绑定加油卡成功"""

    def setUp(self):
        f = os.path.join(datapath, u'接口测试用例.xls')
        self.data_list = readexceldata.excel_to_list(f, "BingdingCard")

    def test_bingding_card_ok(self):
        """绑定卡号成功"""
        data = readexceldata.get_test_data('test_bingding_card_ok', self.data_list)
        case_log.case_log(data)
        url = data['url']
        input_args = data['input_args']
        expire_result = data['expire_result']
        r = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % r.text)
        #self.assertEqual(json.loads(r.content.decode('utf-8')), json.loads(expire_result))
        self.assertEqual(r.json()['success'], True)

    def tearDown(self):
        sql = 'update cardInfo set cardstatus=NULL, userId=NULL where id=40'
        db.change_db(sql)

if __name__ == '__main__':
    unittest.main(verbosity=2)
