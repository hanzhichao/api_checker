import sys
import inspect
sys.path.append("..")
from util.log import Log
from util.data import Data
from util.config_http import Http
from util.db import DB


class Case():
    def __init__(self):
        self.logger = Log.get_logger()
        self.http = Http()
        self.db = DB()

    def load_data(self, data_file):
        self.data = Data(data_file)

    def run_case(self, sheet_name, case_name, vars={}):
        self.case_data = self.data.get_test_case(sheet_name, case_name)
        self.http.set_url(self.case_data.get('Request Url')) 
        self.http.set_headers(self.case_data.get('Request Data Type')) 
        self.http.set_data(self.case_data.get('Request Data') % vars)
        if self.case_data.get('Request Method').lower() == 'get':
            self.resp = self.http.get()
        else:
            self.resp = self.http.post()
        return self.resp

    def run(self, vars={}):
        case_name = inspect.stack()[1][3].strip()
        sheet_name = case_name.split("_")[2]
        self.run_case(sheet_name, case_name, vars)
        try:
            assert self.http_code_200
        except AssertionError:
            self.logger.debug(self.resp.status_code)

        if self.case_data.get('Response Contains'):
            try:
                assert self.response_content
            except AssertionError:
                self.logger.debug(self.resp.text)

        if self.case_data.get('Response Code'):
            try:
                assert self.response_code
            except AssertionError:
                self.logger.debug(self.resp.json().get('code'))

        if self.case_data.get('Response Msg'):
            try:
                assert self.response_msg
            except AssertionError:
                self.logger.debug(self.resp.json().get('code'))

    @property
    def http_code_200(self):
        return True if self.resp.status_code == 200 else False

    @property
    def response_content(self):
        return True if self.case_data.get('Response Contains') in self.resp.text else False

    @property
    def response_code(self):
        return True if self.resp.json().get('code') == self.case_data.get('Response Code') else False

    @property
    def response_msg(self):
        return True if self.resp.json().get('msg') == self.case_data.get('Response Msg') else False

    def check_db(self, sql_name, vars={}):
        sql = self.data.get_sql(sql_name) % vars
        result = self.db.exec_sql(sql)
        return True if result else False



if __name__ == '__main__':
    case = Case()
    case.http.set_env('dev')
    case.load_data('test_user_data.xlsx')
    case.run_case('reg', 'test_user_reg_random_name', {"random_name": "柳柳"})