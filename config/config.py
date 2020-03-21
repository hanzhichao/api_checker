import os
import logging

# mysql的数据库的配置
host = "115.28.108.130"
user = "test"
password = "***"
database = "longtengserver"
port = 3306

# 邮件配置
sender = '260137162@qq.com'  # 发送方
receiver = "260137162@qq.com"        # 接收方,多个收件人以逗号隔开"xx@qq.com,yy@qq.com"
emailusername = "260137162@qq.com"  # 登录邮箱的用户名
emailpassword = "deynljbeluxqbjhh"             # 登录邮箱的密码,请配置自己的
server = "smtp.qq.com"  # smtp服务器


#  项目目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录
datapath = os.path.join(basedir,'data')

# 报告目录
reportpath = os.path.join(basedir, 'report')

#  日志配置
logdir = os.path.join(basedir, 'log')
logpath =os.path.join(logdir, 'log.txt')


logger = logging.getLogger('apiteststudy')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logpath, encoding='utf-8')
datafmt = "%Y-%m-%d %H:%M:%S"
fm = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)

logging.getLogger("requests").setLevel(logging.WARNING)
if __name__ == "__main__":
    logger.info('this is test')
    #print(basedir)
