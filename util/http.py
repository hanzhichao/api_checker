import requests

import sys
sys.path.append("..")
from util.config import Config
from util.log import Log


class Http():
    def __init__(self):
        self.cf = Config()
        self.logger = Log.get_logger()
        self.timeout = float(self.cf.get_http("time_out"))

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers = self.headers, timeout=self.timeout)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,timeout=self.timeout)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

        