import requests



def login_and_get_token(username, password):   # 辅助方法不以test开头, 数据也不用从excel中读取
    url = "http://192.168.1.171:8083/sys/login"
    data = {"password": password,"username": username}
    res = requests.post(url, json=data)
    token = res.json()["token"]
    return token
