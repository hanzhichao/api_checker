import sys
import random
import pytest
sys.path.append("../..")
from util.case import Case

case = Case()

def setup_module(module):
    case.http.set_env('dev')
    case.load_data('test_user_data.xlsx')


def test_user_login_normal():
    case.run()

def test_user_reg_random_name():
    random_name=random.choice(['赵','钱','孙','李','周','吴','郑','王'])+chr(random.randint(0x4e00, 0x9fbf))
    case.run({"random_name": random_name})
    case.check_db('checkUserPasswd', {"name": random_name, "passwd": "123456"})

if __name__ == '__main__':
    pytest.main(["-q", "test_user.py"])