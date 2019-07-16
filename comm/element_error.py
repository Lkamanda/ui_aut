from log.logger import mylogger
from comm.common import screenShot
import time
import sys
import unittest


def element_error(self, e):
    """对定位元素异常的处理：定位元素异常，回归原点,app 首页， 并结束该条测试用例
    :rtype: object
    """
    # 对测试用例名称获取
    api_name = sys._getframe().f_code.co_name
    self.assertEqual(True, get_error_code(self=self, e=e, api_name=api_name))


def element_error_main_chat(self, e):
    test_name = sys._getframe().f_code.co_name
    mylogger.error(test_name, e)
    screenShot(self.driver, test_name)


def get_error_code(self, e, api_name):
    global error_code
    mylogger.error(e)
    screenShot(self, api_name)
    error_code = True

    while True:
        try:
            print("检查是否进入主页")
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element_by_id("com.erlinyou.worldlist:id/chat_img")
            print("检查是否进入主页")
            mylogger.info("返回主页面")
            error_code = False
            print(error_code)
        except Exception as e:
            print(e)
        if error_code == False:
            break
        try:
            print("检查是否弹出退出窗口")
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element_by_id("android:id/button2").click()
            print("检查是否弹出退出窗口结束")
            print(error_code)
            error_code = False
        except Exception as e:
            print(e)
        print(error_code)
        # if error_code == False:
        #     unittest.skipIf(error_code == False, reason='定位元素失败')
        #     break
        self.driver.press_keycode(4)
    mylogger.info("%s执行了测试用例回归原点操作，测试标记失败结束" % api_name)
    return False











