import unittest
import requests
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下

from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入

from test.case.token import login_and_get_token

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = login_and_get_token('admin', "123456")   # 为基础类增加一个类属性
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        method = case_data.get('method')
        params = case_data.get('params')
        headers = case_data.get('headers')
        headers.update({"token": self.token})   # 为所有请求的请求头默认添加一个登录后的token

        data = case_data.get('body')
        expect_res = case_data.get('expect_res')
        data_type = case_data.get('data_type')

        if method.upper() == 'GET':
            res = requests.get(url=url, params=params,headers=json.loads(headers))
            log_case_info(case_name, url, params,headers, expect_res ,res,
                          res.json()["msg"])
            self.assertEqual(res.json()["msg"], expect_res,msg="断言成功")
            #self.assertEqual(res.status_code,200,msg="断言成功")

        # elif data_type.upper() == 'FORM':
        #     res = requests.post(url=url, data=json.loads(args))
        #     log_case_info(case_name, url, args, expect_res, res.text)
        #     self.assertEqual(res.text, expect_res)
        else:
            res = requests.post(url=url, params=params,data=data,headers=json.loads(headers))
            log_case_info(case_name, url,params,headers,data,
                          expect_res,res.json()["msg"]
                          )
            self.assertEqual(res.json()["msg"], expect_res,msg="断言成功")
            return res.json()["token"]
            #self.assertEqual(res.status_code,200,msg="断言成功")




if __name__ == "__main__":
    unittest.main()
    print(issubclass(BaseCase,BaseCase))
