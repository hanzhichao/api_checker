# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config


def send_mail(title, msg):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 标题
    title = title
    # 内容
    message = msg
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword

    msg = MIMEText(message)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver
    # 建立连接
    # s = smtplib.SMTP(server)
    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(','), msg.as_string())
    s.quit()


def send_mail_report(title):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword
    # print config.basedir
    bodyfp = open(config.basedir + '\\report\\' + 'Report.html', encoding='utf-8')
    body = bodyfp.read()
    msg_root = MIMEMultipart()
    msg_root["subject"] = title
    msg_root["from"] = config.sender
    msg_root["to"] = config.receiver
    msg_html = MIMEText(body, "html", 'utf-8')
    msg_root.attach(msg_html)

    att1 = MIMEText(body, 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="Report.html"'
    msg_root.attach(att1)
    # msg_root.attach()

    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(','), msg_root.as_string())
    s.quit()

if __name__ == "__main__":
    #send_mail('test', 'this is a test')
    send_mail_report('test')
