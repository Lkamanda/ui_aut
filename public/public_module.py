from element_api.android_element.login_page_elements import *
from element_api.android_element.home_page_elements import mainChat_element,userAvatar_element
from comm.comm_api import get_login_state
from log.logger import mylogger
import time
from comm.Assertion import check_login


def login(self, driver, mode, login_state):
    """
    账号登录
    :param login_state: 登录状态
    :param self:
    :param driver:
    :param mode:1：账号密码登录
                2：微信登录
    """
    test_name = "登录"
    if login_state == 2:
        pass
    else:
        driver.implicitly_wait(5)
        if mode == 1:
            # 账号密码登录
            mainChat_element(driver)
        elif mode == 2:
            # 微信登录
            driver.implicitly_wait(5)
            userAvatar_element(driver)
            mylogger.info("进入我的页面")
            driver.implicitly_wait(5)
            dL_element(driver)
            mylogger.info('点击注册/登录 进入登录页面')
            driver.implicitly_wait(10)
            wX_element(driver)
            time.sleep(2)
            mylogger.info('点击微信图标进行登录')
            driver.implicitly_wait(4)
            mylogger.info("执行回退")
            driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()
        login_state = get_login_state(driver)
        self.assertEqual(True, check_login(driver=driver, test_name=test_name, login_state=login_state))


# def x():
#     if check_login(driver=self.driver, login_state=login_state, test_name=test_name) is True:
#         pass
#     else:
#         login(self=self, driver=self.driver, mode=2)
#         self.assertEqual(True, check_login(driver=self.driver, login_state=login_state, test_name=test_name))