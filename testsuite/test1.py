from log.log import mylogger

from comm.webdriver import *
import unittest


class Test1(webDriver, unittest.TestCase):
    def test1(self):
        self.driver.implicitly_wait(5)
        mylogger.info('test1')
        print(1)

    def test2(self):
        print(2)

    def test3(self):
        print(3)

    def test1_1(self):
        print("1_1")

    def test1_a(self):
        print("1_a")

    def test1_b(self):
        print("1_b")

    def test2_a(self):
        print("2_b")

    def test_a(self):
        print("_a")

    def test_b(self):
        print("_b")
    def test_a_1(self):
        print("_a_1")


if __name__ == '__main__':
    unittest.main(verbosity=2)