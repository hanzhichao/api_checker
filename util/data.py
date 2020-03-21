"""
1. 从excel中读取用例数据
2. 从excel中读取sql数据
"""
import xlrd
import sys
import os
from functools import reduce
sys.path.append("..")
from util.config import project_path

data_path = os.path.join(project_path, 'data')

class Data():
    def __init__(self, file_name):
        path = os.path.join(data_path, file_name)
        self.wb = xlrd.open_workbook(path)
    
    def get_test_case(self, sheet_name, case_name):
        sh = self.wb.sheet_by_name(sheet_name)
        for i in range(1, sh.nrows):
            if sh.cell(i, 0).value == case_name:
                return dict(zip(sh.row_values(0), sh.row_values(i)))
        return None

    def get_sql(self, sql_name):
        sh = self.wb.sheet_by_name('SQL')
        for i in range(1, sh.nrows):
            if sh.cell(i, 0).value == sql_name:
                return sh.cell(i, 1).value
        return None


if __name__ == '__main__':
    t=Data("test_user_data.xlsx")
    print(t.get_test_case('reg','test_user_reg_random_name'))
    print(t.get_sql('delUser'))