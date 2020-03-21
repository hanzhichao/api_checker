import unittest

from testcase import  test_user_login
from testcase import test_user_reg

# 1. 声明一个测试套件
smoke_suite = unittest.TestSuite()
# 2. 添加用例
smoke_suite.addTest(test_user_login.TestUserLogin("test_user_login_normal"))
smoke_suite.addTest(test_user_reg.TestUserReg("test_user_reg_normal"))

# 3.运行
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(smoke_suite)


