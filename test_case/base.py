# coding=utf-8
import sys
sys.path.append("..")
from Util.models import *
from Util.data_file_parser import *

class Base:
    """用例原型"""
    def __init__(self):
        env = Env("http://w-beta-1000.chemanman.com:7502")
        user = User()
        user.login(env)
        user.post(env,"priceOpV2")


a = Base()