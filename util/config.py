"""
1. 根据不同环境的conf文件返回不同段的数据
2. 返回项目/报告/Log的绝对路径
"""
import configparser
import os

project_path = os.path.dirname(os.path.dirname(__file__))


class Config():
    def __init__(self, file_name='default.conf'):
        self.cf = configparser.ConfigParser()
        path = os.path.join(project_path, 'conf', file_name)
        with open(path) as f:
            self.cf.read(path)

    def get_dev(self, option):
        return self.cf.get("DEV", option)

    def get_test(self, option):
        return self.cf.get("TEST", option)

    def get_stage(self, option):
        return self.cf.get("STAGE", option)

    def get_product(self, option):
        return self.cf.get("PRODUCT", option)

    def get_http(self, option):
        return self.cf.get("HTTP", option)

    def get_db(self, option):
        return self.cf.get("DB", option)

    def get_email(self, option):
        return self.cf.get("EMAIL", option)

    def get_report_dir(self):
        return os.path.join(project_path, self.cf.get("REPORT", 'report_dir'))

    def get_log_dir(self):
        return os.path.join(project_path, self.cf.get("LOG", 'log_dir'))

    def get_log_level(self):
        return self.cf.get("LOG", 'log_level')


if __name__ == '__main__':
    c = Config('default.conf')
    print(c.get_http('base_url'))
    print(c.get_report_dir())
    print(c.get_log_dir())
