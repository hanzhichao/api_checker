import unittest
import requests
import json
from lib import db
from lib import load_data
from lib.case_log import log_case_info
from conf import config


class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "注册")

    def test_user_reg_normal(self):
        if db.check_user("张三丰"):
            db.del_user("张三丰")

        case_data = load_data.get_case(self.sheet, "test_user_reg_normal")

        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])

        res = requests.post(url=url, json=data)
        log_case_info("test_user_reg_normal", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(excepted_res, res.json())

        db.del_user("张三丰")   # 环境清理

    def test_user_reg_use_exist(self):
        case_data = load_data.get_case(self.sheet, "test_user_reg_use_exist")

        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        log_case_info("test_user_reg_use_exist", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(excepted_res, res.json())