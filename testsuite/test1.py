from log.logger import mylogger
from comm.webdriver import *
import unittest
from comm.comm_api import *
from comm.Assertion import check_login
from public.public_module import login
from element_api.android_element.home_page_elements import *


class Test1(WebDriver, unittest.TestCase):

    # def test1(self):
    #     test_name = "1"
    #     obtain_permission(driver=self.driver)
    #     login_state = get_login_state(driver=self.driver)
    #     login(self=self, driver=self.driver, mode=2, login_state=login_state)
    #     self.driver.implicitly_wait(5)
    #     userAvatar_element(driver=self.driver)
    #     mylogger.info('test1')
    #
    #     print(1)

    def test2(self):
        test_name = "2"
        self.driver.implicitly_wait(5)
        userAvatar_element(driver=self.driver)
        try:
            self.driver.find_element_by_id('x').click()
        except Exception as e:
            element_error(driver=self.driver, e=e, self= self)



        print("即将执行下一步操作")
        # mainChat_element(driver=self.driver)


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