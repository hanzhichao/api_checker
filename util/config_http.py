"""
1. 组装http请求
"""
import requests

import json
import sys
sys.path.append("..")
from util.config import Config
from util.log import Log


class Http():
    def __init__(self):
        self.cf = Config()
        self.timeout=float(self.cf.get_http('time_out'))
        self.logger = Log.get_logger()
        self.env = self.url=''
        self.headers = self.params = self.data = self.files = {}

    def set_env(self, env):
        self.env = env

    def set_url(self, request_url):
        if self.env.upper() == 'DEV':
            base_url = self.cf.get_dev("base_url")
        elif self.env.upper() == 'TEST':
            base_url = self.cf.get_test("base_url")
        self.url = base_url + request_url

    def set_headers(self, data_type):
        if data_type == 'FORM':
            self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        elif data_type == 'JSON':
            self.headers = {"Content-Type": "application/json"}
    
    def set_params(self, request_params):
        self.params = {}
        for key_value in request_params.split("&"):
            key = key_value.split("=")[0]
            self.params[key] = key_value.split("=")[1]

    def set_data(self, request_data):
        if request_data.startswith('{'):
            self.data = json.dumps(json.loads(request_data))
        else:
            self.data = {}
            for key_value in request_data.split("&"):
                key = key_value.split("=")[0]
                self.data[key] = key_value.split("=")[1]

    def set_files(self, request_file):
        self.files = {request_file.split(":")[0]:request_file.split(":")[1]}


    def get(self):
        try:
            resp = requests.get(url=self.url, headers=self.headers, params=self.params, data=self.data, files=self.files, timeout=self.timeout)
            logger.debug(json.dumps(self.data))
            return resp
        except TimeoutError:
            self.logger.error("Time out!")
        

    def post(self):
        try:
            resp = requests.post(url=self.url, headers=self.headers, params=self.params, data=self.data, files=self.files, timeout=self.timeout)
            self.logger.debug(json.dumps(self.data, ensure_ascii=False))
            return resp
        except TimeoutError:
            self.logger.error("Time out!")
        

if __name__ == '__main__':
    http = Http()
    http.set_env('dev')
    http.set_url('/api/user/login/')
    http.set_headers('FORM')
    http.set_data('name="张三"&passwd="123456"')
    http.post()