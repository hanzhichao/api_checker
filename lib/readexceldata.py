import xlrd
import os

def excel_to_list(file, tag):
    data_list = []
    book = xlrd.open_workbook(file)
    tag = book.sheet_by_name(tag)
    row_num = tag.nrows
    header = tag.row_values(0)
    for i in range(1, row_num):
        row_data = tag.row_values(i)
        d = dict(zip(header, row_data))
        data_list.append(d)
    return data_list


def get_test_data(test_name, test_list):
    for test_dict in test_list:
        if test_name == test_dict['test_name']:
            return test_dict


if __name__ == '__main__':
    from config.config import datapath
    file = os.path.join(datapath, '接口测试用例.xls')
    tag = 'BingdingCard'
    test_list = excel_to_list(file, tag)
    print(get_test_data('test_no_exist_third_bound',test_list ))

