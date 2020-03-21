"""解析api文件"""

import json
import os


def load(api_file):
    api_file = api_file if api_file.endswith(".json") else api_file + ".json"
    api_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "api", api_file)
    with open(api_file, encoding='utf-8') as f:
        return json.load(f)



if __name__ == "__main__":
    api = load("shop/matchStation")
    print(api, type(api))