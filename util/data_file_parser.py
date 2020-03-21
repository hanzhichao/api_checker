import json
import ConfigParser
import xlrd


class JsonFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls, path, key):
        with open(path) as f:
            return json.load(f)[key]

    @classmethod
    def load(cls, path):
        with open(path) as f:
            return json.load(f)


class ConfFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls, path, section, option):
        conf = ConfigParser.ConfigParser()
        conf.read(path)
        return conf.get(section, option)

    @classmethod
    def load(cls, path):
        _dict = {}
        conf = ConfigParser.ConfigParser()
        conf.read(path)
        for section in conf.sections():
            _dict[section] = {}
            for option in conf.options(section):
                _dict[section][option] = conf.get(section, option)
        return _dict

    @classmethod
    def load(cls, path, section):
        _dict = {}
        conf = ConfigParser.ConfigParser()
        conf.read(path)
        for option in conf.options(section):
            _dict[option] = conf.get(section, option)
        return _dict


class ExcelFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls, path, sheet, row, col):
        wb = xlrd.open_workbook(path)
        if isinstance(sheet, int):
            sh = wb.sheet_by_index(sheet)
        else:
            sh = wb.sheet_by_name(sheet)
        return sh.cell_value(row, col)

    @classmethod
    def load(cls, path, sheet=0):
        wb = xlrd.open_workbook(path)
        if isinstance(sheet, int):
            sh = wb.sheet_by_index(sheet)
        else:
            sh = wb.sheet_by_name(sheet)
        cols = sh.ncols
        rows = sh.nrows
        data_list = []

        for row in range(1, rows):
            data = {}
            for col in range(0, cols):
                data[sh.cell_value(0, col)] = sh.cell_value(row, col)
            data_list.append(data)
        return data_list


class XMLFile:
    def __init__(self):
        pass

    @classmethod
    def get(cls):
        pass

if __name__ == '__main__':
    a=A
    a.test()

