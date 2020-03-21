
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '*****'
db = 'api_test'

# 路径配置
import os
config_path = os.path.abspath(__file__)  # __file__当前文件  os.path.abspath() 绝对路径
conf_path = os.path.dirname(config_path)  # os.path.dirname() 所在文件夹的路径
project_path = os.path.dirname(conf_path) # 项目的绝对路径

# project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)
# 数据文件目录
# data_path = os.path.join(project_path, 'data')
data_file = os.path.join(project_path, 'data', 'data.xlsx')
# 日志文件
log_file = os.path.join(project_path, 'log', 'log.txt')
report_file = os.path.join(project_path, 'report', 'report.html')
# 邮件配置

# log配置
import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    )


if  __name__ == "__main__":
    # logging.info("hello, world")
    # logging.info("中文日志")
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
