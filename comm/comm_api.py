# 客户端连接 appium
from log.logger import mylogger
from comm.element_error import element_error ,element_error_main_chat
from element_api.android_element.setting_city_page_elements import *
from config.myconfig import myconfig
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


def get_login_state(self):
    """校验当前是否是登录状态"""
    login_state = 0
    try:
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_id("chat_img").click()
        login_state += 1
        mylogger.info("进入登录校验")
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.erlinyou.worldlist:id/textview_tab_chat")
            mylogger.info("当前是登录状态")
            login_state += 1
            self.driver.press_keycode(4)
            return login_state
        except:
            mylogger.info("当前是未登录状态")
            self.driver.press_keycode(4)
            return login_state
    except:
        mylogger.info("当前是未登录状态")
        return login_state


def get_agree(self):
    """
    法律声明同义
    :param self:
    :return:
    """
    global first_use
    first_use = None
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/check").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/agree").click()
        first_use = True
        return first_use
    except:
        first_use = False
        return first_use


def obtain_permission(self):
    """得到权限"""
    get_agree(self=self)
    for i in range(0, 4):
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("//*[@text='允许']").click()
            # driver.find_element_by_android_uiautomator('new UiSelector().textContains("允许")').click()
        except:
            pass
    # 对于首次安装的程序
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@text='欢迎开启海外之旅']").click()
        # self.find_element_by_id("com.erlinyou.worldlist:id/btn_start").click()
        print("找到该元素")
    except:
        print("未找到指定的button")
    setting_city(self)

# 整个测试集运行第一次调用
def setting_city(self):
    """ 设置当前所在城市"""
    city_text = myconfig.get_setting_city()
    home_page_city(self=self)
    setting_city_search(self=self, city_text=city_text)
    self.driver.implicitly_wait(5)

    self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[1]"
                                      "/android.widget.LinearLayout").click()
    # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("巴黎")').click()
    # self.driver.find_element_by_xpath("*[@text='北京市']").click()
    self.assertEqual(True, check_setting_city(self=self, city_text=city_text))

def check_setting_city(self, city_text):
    check_element = self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_city_value")
    if city_text == check_element.get_attribute("text"):
        mylogger.info("设置城市成功")
        return True

    else:
        mylogger.info("设置城市失败")
        return False






