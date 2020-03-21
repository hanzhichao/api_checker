"""
1. 配置logger的输出格式
2. 支持输出到文件，也支持屏幕输出
3. 获取logger
"""
import sys
sys.path.append("..")
from util.config import Config
import time
import os
import logging


class Log(): # 类方法
    @classmethod
    def _config_logger(cls):
        # 1. 确定日志dir和名称
        cf = Config()
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_file = os.path.join(cf.get_log_dir(), date + '.log')

        # 2. 创建一个logger
        cls.logger = logging.getLogger()
        cls.logger.setLevel(eval('logging.'+cf.get_log_level().upper()))

        # 3. 建立不同的handler
        fh = logging.FileHandler(log_file, mode='a')
        ch = logging.StreamHandler()

        # 4. 定义输出格式
        fromatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(fromatter)
        ch.setFormatter(fromatter)

        # 5. 将两个handler添加到logger
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)

    @classmethod
    def get_logger(cls):
        cls._config_logger()
        return cls.logger

if __name__ == '__main__':
    logger = Log.get_logger()
    logger.info("abc")
    logger.debug("abd")