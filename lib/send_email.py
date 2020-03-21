import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
sys.path.append("..")
from config.config import *

# # 1. 编写email正文 MIME
# msg = MIMEText('<h1>这是一封Python发送的邮件</h1><h2>hello</h2>','html','utf-8')
# # 2. 编写email头
# msg['From'] = "ivan-me@163.com"
# msg["To"] = 'superhin@126.com'
# msg['Subject'] = "中文"
# # 3. 连接smtp服务器，发送邮件
# smtp = smtplib.SMTP("smtp.163.com")
# smtp.login("ivan-me@163.com","hanzhichao123")
# # smtp.sendmail("test_results@sina.com",'superhin@foxmail.com',msg.as_string())
# smtp.sendmail("ivan-me@163.com",'superhin@126.com',msg.as_string())
# smtp.quit()
# print("发送完成")
def send_email(report_file):
    msg = MIMEMultipart()

    msg.attach(MIMEText(email_body,'plain','utf-8'))
    msg['From'] = sender
    msg["To"] = receiver
    msg['Subject'] = subject

    with open(report_file,'rb') as f:
        att1_body = f.read()

    att1 = MIMEText(att1_body,'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)
    msg.attach(att1)

    smtp = smtplib.SMTP(smtp_server)
    smtp.login(smtp_user, smtp_password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()