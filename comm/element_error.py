from log.logger import mylogger
from comm.common import screenShot
import time
import unittest


def element_error(self, driver, e):
    """对定位元素异常的处理：定位元素异常，回归原点,app 首页， 并结束该条测试用例"""
    self.assertEqual(True, get_error_code(driver=self.driver, e=e))

def element_error_main_chat(driver, e):
    test_name = "main_chat_element定位失败"
    mylogger.error(e)
    screenShot(driver, test_name)



def get_error_code(driver, e):
    global error_code
    mylogger.error(e)
    test_name = "定位失败"
    screenShot(driver, test_name)
    error_code = True

    while True:
        try:
            print("检查是否进入主页")
            driver.implicitly_wait(5)
            time.sleep(1)
            driver.find_element_by_id("com.erlinyou.worldlist:id/chat_img")
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
            driver.implicitly_wait(5)
            time.sleep(1)
            driver.find_element_by_id("android:id/button2").click()
            print("检查是否弹出退出窗口结束")
            print(error_code)
            error_code = False
        except Exception as e:
            print(e)
        print(error_code)
        if error_code == False:
            unittest.skipIf(error_code == False, reason='定位元素失败')
            break
        driver.press_keycode(4)
    mylogger.info("执行了测试用例回归原点操作，测试标记失败结束")
    return False






