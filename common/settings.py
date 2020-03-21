"""项目配置"""

# 环境配置
DEV = "http://dev.spicespirit.com" 
TEST = "http://test.spicespirit.com"
STAGE = "http://stage.spicespirit.com"
PRODUCT = "http://www.spicespirit.com"


# 数据库配置
DB_DEV = { "HOST": "192.168.100.219",
            "PORT": 3306,
            "DB": "spicespirit_dev",
            "USER": "spice",
            "PASSWORD": "1234qwer" }

DB_TEST= { "HOST": "192.168.100.198",
                "PORT": 3306,
                "DB": "spicespirit_test",
                "USER": "spice",
                "PASSWORD": "1234qwer" }

TIMEOUT = 10
RETRY_TIME = 3
REPORT_PATH = "report"
LOG_PATH = "report"
LOG_LEVEL = "debug"

# 请求头headers设置
HEADERS_FORM = { "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
HEADERS_JSON = { "Content-Type": "application/json;charset=utf-8"}
HEADERS_SOAP = { "Content-Type": "application/soap+xml; charset=utf-8" }
HEADERS_MULTI = { "Content-Type": "multipart/form-data; charset=utf-8" }

COOKIES = {}

# 登录配置
LOGIN_USER = "hanzhichao"
LOGIN_PASSWORD = "hanzhichao"

# 邮件配置
SMTP_SERVER = ""
SMTP_PORT = ""
SMTP_USER = ""
SMTP_PASSWORD = ""

EMAIL_SUBJECT = "api自动化测试报告"
RECEIVE_LIST = ['superhin@163.com', 'hanzhichao@spicespirit.com']


