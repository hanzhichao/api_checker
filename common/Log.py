import logging
from datetime import datetime
import threading
import os
import sys
sys.path.append("..")
import readConfig


class Log(object):
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")

        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        self.logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(self.logPath, "output.log"))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def get_result_path(self):
        return self.logPath

    def get_logger(self):
        return self.logger
        

class MyLog(object):
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == '__main__':
    MyLog.get_log()