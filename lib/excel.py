import os
import xlrd


from config import basedir


class Excel(object):
    def __init__(self, file_name):
        self.wb = xlrd.open_workbook(os.path.join(basedir, 'data', file_name))

    def get_sheet_data(self, sheet_name):
        sh = self.wb.sheet_by_name(sheet_name)
        return [sh.row_values(i) for i in range(1, sh.nrows)]
