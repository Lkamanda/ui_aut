"""
登录页面 相关
"""
from comm.element_error import element_error
from config.myconfig import MyConfig
import os

myconfig = MyConfig()


# 点击个人中心 登录/注册 button
def dL_element(self):
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/user_name_tv").click()
    except Exception as e:
        element_error(self.driver, e)


# 点击登录页面微信入口
def wX_element(self):
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/iv_other_login").click()
    except Exception as e:
        element_error(self=self, e=e)


# 微信登录页面 输入账号
def wxUser_element(self, wx_username):
    try:
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[1]"
                                          "/android.widget.EditText").send_keys(wx_username)
    except Exception as e:
        element_error(self, e)


# 微信登录页面 输入密码
def wxPassword_element(self, wx_password):
    try:
        self.driver.find_element_by_xpath(
            "//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys(
            wx_password)
    except Exception as e:
        element_error(self, e)


def wxDl_element(self):
    """微信登录页面 点击登录buttton"""
    try:
        self.driver.find_element_by_id("com.tencent.mm:id/cqc").click()
    except Exception as e:
        element_error(self, e)


# 登录页面 账号密码登录title 点击
def mobile_title_element(self):
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登录") ').click()
    # driver.find_element_by_id("com.erlinyou.worldlist:id/account_login").click()
    except Exception as e:
        element_error(self, e)


# 账号密码登录：输入手机号登陆   mobile_number = "18612463553"
def mobile_user_element(self):
    adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    os.system(adb1)
    print(myconfig.get_mobile_number())
    self.driver.implicitly_wait(5)
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_username").send_keys(myconfig.get_mobile_number())
    except Exception as e:
        element_error(self, e)
    os.system(adb3)


# 账号密码登录 ：输入密码
def mobile_password_element(self):
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_pwd").send_keys(myconfig.get_mobile_password())
    except Exception as e:
        element_error(self, e)


#  账号密码登录，立即登录
def mobile_login_element(self):
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/submit").click()
    except Exception as e:
        element_error(self, e)
