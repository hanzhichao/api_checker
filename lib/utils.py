import json
import logging


def json2dict(json_string):
    if json_string:
        try:
            return json.loads(json_string)
        except json.decoder.JSONDecodeError:
            logging.error("JSON格式不合法: {}".format(json_string))
