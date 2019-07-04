# 客户端连接 appium
from log.log import mylogger
from comm.element_error import element_error ,element_error_main_chat


# def get_desired_caps(mobile_config):
#     desired_caps = {'platformName': 'Android',  # 手机类型
#                     'platformVersion': mobile_config[0][1],  # 被测试手机，   baa822b7
#                     'deviceName': mobile_config[0][0],  # baa822b7  a82ccd1d Q8JNNNGUOF8L4PON   设备名称， adb devices
#                     'appPackage': 'com.erlinyou.worldlist',
#                     'appActivity': 'com.erlinyou.map.Erlinyou',
#                     'unicodeKeyboard': True,  # appium 传输中使用自己的输入法，可以传输中文
#                     'resetKeyboard': True,  # 程序结束时重置原来的输入法
#                     'noReset': True,  # 如果app存在则不重新安装
#                     # 'autoGrantPermissions': 'True'
#                     # 'app': r"C:\Users\zhoujialin\PycharmProjects\aut_LT\LT\apps\boobuz.apk"
#                     # desired_caps['autoGrantPermissions'] = 'True'
#                     }
#     return desired_caps


def assert_login(driver):
    """校验当前是否是登录状态"""
    global login_state
    login_state = 0
    try:
        driver.implicity_wait(4)
        driver.find_element_by_id("chat_img").click()
        login_state = 1
        mylogger.info("进入登录校验")
        try:
            driver.implicity_wait(5)
            driver.find_element_by_id("com.erlinyou.worldlist:id/textview_tab_chat")
            mylogger.info("当期是登录状态")
            login_state = 2
        except:
            mylogger.info("当前是未登录状态")
    except Exception as e:
        element_error_main_chat(driver, e)

    print(login_state)
    if login_state == 2 or 1:
        driver.press_keycode(4)
        try:
            driver.implicitly_wait(5)
            driver.find_element_by_id("chat_img")

        except:
            mylogger.error("页面未回到主页面")
    print(login_state)
    return login_state


def get_agree(driver):
    """法律声明同义"""
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_id("com.erlinyou.worldlist:id/check").click()
        driver.implicitly_wait(5)
        driver.find_element_by_id("com.erlinyou.worldlist:id/agree").click()
    except Exception as e:
        mylogger.error(e)


def obtain_permission(driver):
    """得到权限"""
    for i in range(0, 4):
        try:
            driver.implicity_wait(5)
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("允许")').click()
        except:
            pass

