import unittest
import json
import sys
sys.path.append("../..")

from common import configData
from common.configHttp import ConfigHttp

class TestMatchStation(unittest.TestCase):
    def setUp(self):
        print("**********CASE START**********")

    def tearDown(self):
        print("**********CASE END**********")

    data_list = configData.get_xls('shopCase.xlsx', 'matchStation')

    def test_matchStation_error(self):
        
        request = ConfigHttp()

        data = self.data_list[1]

        if data[1].lower() == 'post':
            request.set_url(data[2])
            request.set_headers({"content-type": "application/x-www-form-urlencoded;charset=utf-8"})
            request.set_data({"lng": data[3], "lat": data[4]})
            response = request.post()
            response_json = response.json()
            code = response_json.get('code')
            message = response_json.get('message')
            print(code, message)
            self.assertEqual(code, int(data[5]))
            self.assertEqual(message, data[6])

if __name__ == '__main__':
    unittest.main()