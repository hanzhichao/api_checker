import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email_config


def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_config["body"], "plain", "utf-8"))  # plain/html

    msg["To"] = email_config["receiver"]
    msg["From"] = email_config["user"]
    msg["Subject"] = email_config["subject"]

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    # 4. 连接smtp服务器并发送邮件
    smtp = smtplib.SMTP_SSL(email_config["server"])  # smtp服务器地址 使用SSL模式
    try:
        smtp.login(email_config["user"], email_config["password"])  # 用户名和密码
    except smtplib.SMTPAuthenticationError:
        logging.error("登录邮箱失败")
    else:
        smtp.sendmail(email_config["user"], email_config["receiver"], msg.as_string())
        logging.info("邮件发送成功")
    finally:
        smtp.quit()

