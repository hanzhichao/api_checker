import unittest,json
from test.case.basecase import BaseCase


class TestUserLogin(BaseCase):
    def test_user_login_normal(self):
        """level1:正常登录"""
        case_data = self.get_case_data("登录接口")
        r = self.send_request(case_data)
        return r.josn

    # def test_user_login_password_wrong(self):
    #     """密码错误登录"""
    #     case_data = self.get_case_data("订单详情")
    #     self.send_request(case_data)

    def test_order_details(self):
        '''订单详情'''
        case_data = self.get_case_data("订单详情")
        headers = json.loads(case_data["headers"])
        headers["token"] = self.test_user_login_normal().josn.token
        case_data["headers"] = json.dumps(headers)
        self.send_request(case_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # t = TestUserLogin()
    # print(t.test_user_login_normal().__tags__)
    # suite = unittest.TestSuite()
    # suite.addTest(TestUserLogin('test_user_login_normal'))
    # for i in suite:
    #     print(i)

    # unittest.TextTestRunner().run(suite)
