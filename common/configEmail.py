import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import sys
sys.path.append("..")
import readConfig as readConfig
from common.Log import MyLog
import zipfile
import glob  # 文件搜索

localReadConfig = readConfig.ReadConfig()

class Email(object):
    def __init__(self):
        global host, user, password, port, sender, title, content
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
        content = localReadConfig.get_email("content")
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        for n in str(self.value).split("/"):
            self.receiver.append(n)

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + ""  + date
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def config_file(self):
        if self.check_file():
            reportPath = self.log.get_result_path()
            zipPath = os.path.join(readConfig.proDir, "result", "test.zip")
            files = glob.glob(reportPath + "\*")
            f = zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED)
            for file in files:
                f.write(file)
            f.close()

    def check_file(self):
        reportPath = self.log.get_result_path()
        if os.path.isdir(reportPath) and not os.stat(reportPath) == 0: # 是否应该用isdir
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()

        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self,msg.as_string())
            smtp.quit()
            self.logger.info("已发送测试报告邮件")
        except Exception as ex:
            self.logger.error(str(ex))


class MyEmail(object):
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == "__main__":
    email = MyEmail.get_email()