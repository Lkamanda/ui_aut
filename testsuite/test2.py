from log.logger import mylogger
from config.myconfig import MyConfig
# from comm.webdriver import webDriver
import unittest


class Test1(unittest.TestCase):
    def test1(self):
        A = MyConfig().get_rename_text()
        mylogger.info("test2")
        print(A)

    def test2(self):
        print(2)
