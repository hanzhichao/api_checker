import unittest
from config.config import *
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib.send_email import send_email

logging.info("="*25+" 测试开始 "+"="*25)
suite = unittest.defaultTestLoader.discover(testcase_path)

with open(report_file,"wb") as f:
    HTMLTestRunner(stream=f,title="ApiTest",description="测试报告").run(suite)

send_email(report_file)
logging.info("邮件已发送")
logging.info("="*25+" 测试结束 "+"="*25)