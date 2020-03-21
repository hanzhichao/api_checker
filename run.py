import os
import time
from util.config import Config
from util.e_mail import send_email
import pytest

def main():
    cf = Config()
    report_dir = cf.get_report_dir()
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_name = os.path.join(report_dir, 'report_' + now + '.html')
    pytest.main(["-q", "case", "--html=" + report_name])
    send_email(report_name)


if __name__ == '__main__':
    main()