# 1. 导入包
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import sys
sys.path.append("..")
from util.config import Config
from util.log import Log

def send_email(report_name):
    cf = Config()
    logger = Log.get_logger()
    report_file = os.path.join(cf.get_report_dir(), report_name)
    # 2. 配置email正文MIMEText
    with open(report_file, 'rb') as f:
        email_body = f.read()
    msg = MIMEText(email_body, 'html', 'utf-8')

    # 3. 配置email头部信息
    msg['Subject'] = Header(cf.get_email('subject'), 'utf-8')
    msg['From'] = cf.get_email('smtp_user')
    msg['To'] = cf.get_email('receiver').replace(",", ";")

    # 4. 连接smtp服务器，发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(cf.get_email('smtp_host'))
        smtp.login(cf.get_email('smtp_user'), cf.get_email('smtp_passwd'))
        for receiver in cf.get_email('receiver').split(","):
            smtp.sendmail(cf.get_email('smtp_user'), receiver.strip(), msg.as_string())
        smtp.quit()
        logger.info("测试报告邮件已发送")
    except Exception as ex:
        logger.error(str(ex))

if __name__ == '__main__':
    send_email('report.html')