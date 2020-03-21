from api_test_framework.test.case.basecase import *
from api_test_framework.lib.read_excel import *






class GetData():
    def __init__(self):
        self.data_list =  excel_to_list("test_user_data.xlsx", "TestUserLogin")
        self.case_data = get_test_data(self.data_list, i)
        for i in range(2, sh.nrows):  # 跳过标题行，从第二行开始取数据
            d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
            data.append(d)


