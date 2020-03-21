import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


db_config = {
    "host": "115.28.108.130",
    "port": 3306,
    "user": "test",
    "password": "***",
    "db": "longtengserver"
}

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler(os.path.join(basedir, 'log', "log.txt"), encoding="utf-8")
                    ])

email_config = {
    "server": "smtp.sina.com",
    "user": "test_results@sina.com",
    "password": "hanzhichao123",
    "subject": "自动化测试报告",
    "body": "hi, 测试报告请查看附件",
    "receiver": "superhin@126.com"
}
