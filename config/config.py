import logging
import os

# 项目路径
prj_path =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_file = os.path.join(prj_path,'data','data.xlsx')
testcase_path = os.path.join(prj_path, 'testcase')


report_file = os.path.join(prj_path, 'report','report.html')
log_file = os.path.join(prj_path,'log','log.txt')


# 全局log配置
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a")


# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '****'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password = '****'

sender = smtp_user
receiver = 'superhin@126.com'
subject = "接口测试报告"
email_body = "hi,all\n测试完成，请查看附件"


if __name__ == '__main__':
    logging.info("hello")
