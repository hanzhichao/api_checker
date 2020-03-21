# -*- coding: utf-8 -*-
import unittest
from config.config import basedir
from lib import HTMLTestRunner_PY3


suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase')
# unittest.TextTestRunner(verbosity=2).run(suite)
outfile = open(basedir + "/report/WebUIReport.html", "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='apistudy Test Report',
    description='龙腾测试实战.'
    )
runner.run(suite)
outfile.close()
# from lib import send_mail
# send_mail.send_mail_report('test')
