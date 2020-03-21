"""
1.配置email内容(邮件主题，邮件正文，邮件附件)
2. 连接smtp服务器发送email
"""
# 1. 导入3个包
import smtplib  # 建立smtp连接
from email.mime.text import MIMEText # 格式化Email文本(Email正文)
from email.header import Header

import os
import sys
sys.path.append("..")
from util.log import Log
from util.config import Config


def send_email(report_name):
    cf = Config()
    logger = Log.get_logger()

    report_file = os.path.join(cf.get_report_dir(), report_name)
    with open(report_file, encoding='utf-8') as f:
        email_body = f.read()
    # 2. 配置email内容
    msg = MIMEText(email_body, 'html', 'utf-8')

    # 3. 配置email头部信息
    msg['Subject'] = Header(cf.get_email('subject'), 'utf-8')
    msg['From'] = cf.get_email('smtp_user')
    msg['To'] =  cf.get_email('recevier')

    # 4. 连接smtp服务器，发送邮件
    try:
        
        smtp = smtplib.SMTP()
        smtp.connect(cf.get_email('smtp_host'))
        smtp.login(cf.get_email('smtp_user'), cf.get_email('smtp_passwd'))
        smtp.sendmail("test_results@sina.com", "hanzhichao@spicespirit.com", msg.as_string())
        smtp.quit()
        logger.info("测试报告邮件已发送")
    except Exception as ex:
        logger.error(str(ex))


if __name__ == '__main__':
    send_email("report.html")