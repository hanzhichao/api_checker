import requests
import sys
sys.path.append("..")

from common import settings
from common import session
from common import api


class Base(object):
    """测试用例基准类"""

    def __init__(self, env, api_file, data=None):
        self.api = api.load(api_file)
        self.env = env
        self.data = data
        # self.session = session.login()

    def get(self, params):
        rep = self.session
        
    def post(self):
        res = requests

if __name__ == "__main__":
    b = Base("TEST", "shop/matchStation")
    print(b.api)