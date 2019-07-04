from log.log import mylogger
from comm.common import screenShot


def element_error(driver, e):
    """对定位元素异常的处理"""
    mylogger.error(e)
    test_name = "定位失败"
    screenShot(driver, test_name)
    while True:
        try:
            driver.implicity_wait(5)
            driver.find_element_by_id("chat_img")
            mylogger.info("返回主页面")
            break
        except:
            driver.press_keycode(4)
            mylogger.info("执行了一次退出，未回到主页面")


def element_error_main_chat(driver, e):
    test_name = "main_chat_element定位失败"
    mylogger.error(e)
    screenShot(driver, test_name)

