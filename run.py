import os
import logging
import unittest
import click
from config import basedir
from lib.htmlrunner import HTMLTestRunner
from lib.mail import send_email


@click.command()
@click.option("--send", help='是否发送邮件')
def run_all(send):
    logging.info("====================================== 测试开始 ======================================")
    suite = unittest.defaultTestLoader.discover(os.path.join(basedir, "testcase"))
    report_file = os.path.join(basedir, 'report', "report.html")
    with open(report_file, "wb") as f:
        HTMLTestRunner(stream=f, title="自动化测试报告", description="龙腾15期加油卡接口测试").run(suite)
    logging.info("====================================== 测试结束 ======================================")
    if send == "true":
        send_email(report_file)


if __name__ == '__main__':
    run_all()
