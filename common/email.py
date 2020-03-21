import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib



def send_mail(file_new=null):
    
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'test_results@sina.com'
    msg['To'] = 'hanzhichao@spicespirit.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sina.com")
    smtp.login("test_results@sina.com", "hanzhichao123")
    smtp.sendmail("test_results@sina.com", "hanzhichao@spicespirit.com", msg.as_string())
    smtp.quit()
    print('email has send out!')
