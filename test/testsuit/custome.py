# -*- coding: utf-8 -*-
import unittest
from config.config import reportpath
import os.path

from lib import HTMLTestRunner_PY3
from test.testcase.bindingcard.test_bindingcard import BingdingCard

suite = unittest.makeSuite(BingdingCard)
report_file = os.path.join(reportpath,'Report.html')

outfile = open(report_file, "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='apistudy Test Report',
    description=u'龙腾测试实战.'
    )
runner.run(suite)
outfile.close()