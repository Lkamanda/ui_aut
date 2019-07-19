# 设置当前城市elements
import os
from comm.element_error import *


def setting_city_search(self, city_text):
    # adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    adb1 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    os.system(adb1)
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(city_text)
    except Exception as e:
        element_error(self, e)


def current_positioning(self, city_text):
    # 获取当前定位城市
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_locationCity").click()
    except Exception as e:
        element_error(self, e)

def home_page_city(self):
    # 主页面进入当前城市设置入口
    try:
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_city_value").click()
    except Exception as e:
        element_error(self, e)