import unittest
from common import HTMLTestRunnerCN
from common.Log import MyLog as Log
import readConfig
import os

localReadConfig = readConfig.ReadConfig()


class Suite(object):
    def __init__(self):
        self.caseListFile = os.path.join(readConfig.proDir, "caseList.txt")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            case_file = os.path.join(readConfig.proDir, "testCase")  # testCase的子文件夹（模块）要有__init__.py文件才会遍历
            # case_file = os.path.join(readConfig.proDir, "testCase","shop")
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(case_file, pattern='test_' + case_name + '.py', top_level_dir=None)  # 

            if discover.countTestCases() >0:
                suite_model.append(discover)


        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            resultPath = os.path.join(self.log.get_result_path(), 'result.html')
            if suit is not None:
                self.logger.info("**********TEST START**********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description', verbosity=2)
                runner.run(suit)
            else:
                self.logger.info("无需要执行的测试用例")
        # except Exception as ex:
        #     self.logger.error(str(ex))
        finally:
            self.logger.info("**********TEST END**********")
            on_off = localReadConfig.get_email("on_off")
            # 是否发送报告开关
            if int(on_off) == 0:
                self.email.send_email()
            elif int(on_off) == 1:
                self.logger.info("请勿发送邮件给开发者")
            else:
                self.logger.info("on_off配置不正确，应为0或1")

if __name__ == '__main__':
    suit = Suite()
    suit.run()