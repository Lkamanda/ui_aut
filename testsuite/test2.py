from log.log import mylogger

# from comm.webdriver import webDriver
import unittest


class Test1(unittest.TestCase):
    def test1(self):
        mylogger.info("test2")
        print(1)

    def test2(self):
        print(2)
