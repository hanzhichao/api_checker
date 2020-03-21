import xlrd

# excel = xlrd.open_workbook("data.xlsx")  # 打开excel
#
# # sheet = excel.sheet_by_index(0)
# sheet = excel.sheet_by_name("TestUserLogin")

# print(sheet.cell(0,0).value)
# print(sheet.cell(1,1).value)
#
# print(sheet.nrows)
# print(sheet.ncols)
#
# 打印excel所有单元格的数据
# for i in range(0,sheet.nrows):
#     for j in range (0,sheet.ncols):
#         print(sheet.cell(i,j).value)

# print(sheet.row_values(0))
# 输出所有行的数据
# for i in range(1,sheet.nrows):
#     if sheet.cell(i,0).value == 'test_user_login_normal':
#         print(sheet.row_values(i))

# # 返回 excel sheet的所有数据
# def excel_to_list(data_file, sheet_name):
#     excel = xlrd.open_workbook(data_file)
#     sheet = excel.sheet_by_name(sheet_name)
#     result = []
#     for i in range(1,sheet.nrows):
#         result.append(sheet.row_values(i))
#     return result
#
# # 从一张工作表中查找一个用例的数据
# def get_test_data(data_list, case_name):
#     for case_data in data_list:
#         if case_data[0] == case_name:
#             return case_data

# 从Excel里读取一条用例的数据 file, sheet_name, case_name
def get_data(file,sheet_name,case_name):
    wb = xlrd.open_workbook(file)
    sh = wb.sheet_by_name(sheet_name)

    for i in range(1, sh.nrows):
        if sh.cell(i,0).value == case_name:
            return sh.row_values(i)

if __name__ == '__main__':
    # data_list = excel_to_list('data.xlsx','TestUserLogin')
    # print(get_test_data(data_list, 'test_user_login_normal'))
    case_data = get_data('data.xlsx','TestUserLogin','test_user_login_normal')
    print(case_data)
    url = case_data[1]
    data = case_data[3]
    expect_res = case_data[4]
    print(url)
    print(data)
    print(expect_res)