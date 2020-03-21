import sys
sys.path.append("..")
from util.log import Log
from util.data import Data
from util.http import HTTP
from util.data import Data


class Base():
     def __init__(self):
        self.cf = Config()
        self.logger = Log.get_logger()
        http = Http()
        data = Data(file_name)
        data.get_test_case(sheet_name, case_name)
        http.set_url