from conf import config

def log_case_info(case_name, url, data, excepted_res, actual_res):
    config.logging.info("-"*50)
    config.logging.info("执行用例: {}".format(case_name))
    config.logging.info("接口地址: {}".format(url))
    config.logging.info("请求数据: {}".format(data))
    config.logging.info("期望结果: {}".format(excepted_res))
    config.logging.info("实际结果: {}".format(actual_res))