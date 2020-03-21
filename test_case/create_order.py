from base import Base
from Util.data import JsonFile
import json
# from Util.OptionParser import *


class CreateOrder(Base):
    

    def create_order(self):
        # print options.api
        # file = "../API/" + options.api + ".json"
        self.post('../API/create_order.json')

if __name__ == '__main__':
    a = CreateOrder()
    a.create_order()
