import openpyxl
import os
class Operate_Excel:

    def __init__(self, filepath, filename):
        self.__file = filepath + '/' + filename
        if os.path.exists(self.__file):
            print('Open excel:', self.__file)
        else:
            raise ('excel file is not exit')

    def getExcelobject(self):
        """返回excel对象"""
        try:
            return openpyxl.load_workbook(self.__file)
        except Exception as e:
            raise e

    def getSheetogjcet(self):
        try:
            return




print('hahah')
file = Operate_Excel('C:/workspace/api_auto_test/api_auto_test/data','api.xlsx')
print(file.getExcelobject())
