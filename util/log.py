"""
1. 配置输出到文件和输出到屏幕的loghandler和log level
2. 配置log输出格式
3. 获取logger
"""
import logging
import time
import os
import sys
sys.path.append("..")
from util.config import Config

class Log():

    @classmethod
    def _config_logger(cls):
        # 第一步，确定log的路径和名称
        cf = Config()
        log_dir = cf.get_log_dir()
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        log_file = os.path.join(log_dir, date + '.log')

        # 第二步，创建一个logger
        cls.logger = logging.getLogger()
        cls.logger.setLevel(eval("logging."+cf.get_log_level().upper()))    # Log等级总开关

        # 第三步，创建两个个handler，一个写入文件，一个输出到控制台
        fh = logging.FileHandler(log_file, mode='a')  # 用于写入日志文件
        ch = logging.StreamHandler()  # 用于输出到控制台

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将cls.logger添加到handler里面
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)


    @classmethod
    def get_logger(cls):
        cls._config_logger()
        return cls.logger


if __name__ == '__main__':
    logger = Log.get_logger()
    logger.debug("hello")
