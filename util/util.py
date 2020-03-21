# coding=utf-8
import md5 as _md5
#from data_file_parser import *

# 对密码进行md5加密
def md5(password):
    m = _md5.new()
    m.update(password)
    return m.hexdigest()

# 从配置文件env.conf中读取环境信息，返回字典
def get_env(section):
    return ConfFile.load("../Conf/env.conf",section)
# 从配置文件env.conf中读取base_url信息，返回字符串
def get_env_url(section):
    return ConfFile.get("../Conf/env.conf",section,"base_url")
# 从配置文件user.conf读取user信息，返回字典
def get_user(section):
    return ConfFile.load("../Conf/user.conf",section)

def get_api(file_name):
    if '.json' not in file_name:
        file_name += ".json"
    return JsonFile.load("../API/"+file_name)

if __name__ == '__main__':
        a='123456'
        print md5(a)

