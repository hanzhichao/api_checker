"""
1. 获取配置文件不同段的值
2. 获取项目绝对路径
"""
import os
import configparser

project_dir = os.path.dirname(os.path.dirname(__file__))

class Config():
    def __init__(self, file_name='default.conf'):
        self.cf = configparser.ConfigParser()
        config_file = os.path.join(project_dir, 'conf', file_name)
        with open(config_file) as f:
            self.cf.read(config_file)
    
    def get_dev(self, option):
        return self.cf.get('DEV', option)

    def get_test(self, option):
        return self.cf.get('TEST', option)

    def get_http(self, option):
        return self.cf.get('HTTP', option)

    def get_db(self, option):
        return self.cf.get('DB', option)

    def get_email(self, option):
        return self.cf.get('EMAIL', option)

    def get_report_dir(self):
        return os.path.join(project_dir, self.cf.get('REPORT', 'report_dir'))

    def get_log_dir(self):
        return os.path.join(project_dir, self.cf.get('LOG', 'log_dir'))

    def get_log_level(self):
        return self.cf.get('LOG', 'log_level')

if __name__ == '__main__':
    conf = Config()
    print(conf.get_test('base_url'))