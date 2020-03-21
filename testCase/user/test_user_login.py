import json
import unittest
import requests
import sys
sys.path.append("../..")

from config.config import *
from lib.read_excel import get_data


class TestUserLogin(unittest.TestCase):

    def test_user_login_normal(self):
        # 用例数据
        case_data = get_data(data_file,'TestUserLogin','test_user_login_normal')
        url = case_data[1]
        data = case_data[3]  # json格式的字符串 -》 字典
        expect_res = case_data[4]

        logging.info("测试用例：{}".format("test_user_login_normal"))
        logging.info("url: {}".format(url))
        logging.info("请求数据：{}".format(data))
        logging.info("期望结果：{}".format(expect_res))

        # 发送请求
        res = requests.post(url=url, data=json.loads(data))

        # 断言
        self.assertEqual(res.text, expect_res)

    def test_user_login_password_wrong(self):
        # 用例数据
        case_data = get_data(data_file,'TestUserLogin','test_user_login_password_wrong')
        url = case_data[1]
        data = json.loads(case_data[3])
        expect_res = case_data[4]

        logging.info("测试用例：{}".format("test_user_login_password_wrong"))
        logging.info("url: {}".format(url))
        logging.info("请求数据：{}".format(data))
        logging.info("期望结果：{}".format(expect_res))
        # 发送请求
        res = requests.post(url=url, data=data)

        # 断言
        self.assertEqual(res.text, expect_res)
