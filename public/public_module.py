from element_api.android_element.login_page_elements import *
from element_api.android_element.home_page_elements import mainChat_element,userAvatar_element
from comm.comm_api import get_login_state
from log.logger import mylogger
import time
from public.assertion import check_mobile_login, check_wx_login, check_wx_logout
from comm.common import *
from element_api.android_element.mine_page_elements import mine_setting

def login(self, mode, login_state):
    """
    账号登录
    :param login_state: 登录状态 2 的时候表示已经登录
    :param self:
    :param driver:
    :param mode:1：账号密码登录
                2：微信登录
    """
    test_name = "登录"
    if login_state == 2:
        pass
    else:
        if mode == 1:
            # 账号密码登录
            self.driver.implicitly_wait(5)
            mainChat_element(self)
            test_name = "mobile账号密码登录"
            mylogger.debug(test_name)  # 返回测试用例名称
            self.driver.implicitly_wait(5)
            mainChat_element(self)
            mylogger.info("进入登录页面成功")
            self.driver.implicitly_wait(5)
            mobile_title_element(self)
            mylogger.info("切换成账号密码登录")
            time.sleep(4)
            # driver.implicitly_wait(10)
            mobile_user_element(self)
            mylogger.info("输入账号成功")
            self.driver.implicitly_wait(10)
            mobile_password_element(self)
            mylogger.info("输如密码成功")
            self.driver.implicitly_wait(5)
            mobile_login_element(self)

            mylogger.info("触发登录")
            self.assertEqual(True, check_mobile_login(self, test_name))
            mylogger.info("mobile 登录成功")

        elif mode == 2:
            # 微信登录
            self.driver.implicitly_wait(5)
            userAvatar_element(self)
            mylogger.info("进入我的页面")
            self.driver.implicitly_wait(5)
            dL_element(self)
            mylogger.info('点击注册/登录 进入登录页面')
            self.driver.implicitly_wait(10)

            wX_element(self)
            time.sleep(2)
            mylogger.info('点击微信图标进行登录')
            self.driver.implicitly_wait(4)

            self.assertEqual(True, check_wx_login(self=self, test_name=test_name))


def logout(self, login_state):
    # 账号退出
    test_name = "mobile quit"
    if login_state == 2:
        self.driver.implicitly_wait(5)
        userAvatar_element(self)
        mylogger.info("get into mine home page")
        time.sleep(3)
        swipeUp(self=self, t=6000)
        mylogger.info("向上滑动屏幕")
        self.driver.implicitly_wait(10)
        mine_setting(self)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_logout").click()
        mylogger.info("触发退出登录按钮")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("android:id/button1").click()
        mylogger.info("确认退出登录退出")
        time.sleep(3)
        self.driver.press_keycode(4)
        mylogger.info("返回我的页面")
        # self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        self.assertEqual(True, check_wx_logout(self=self, test_name=test_name))
        mylogger.info("登录退出成功")
    else:
        mylogger.bug("未执行退出操作")


# 返回主页
def return_home(self, test_name):
    while True:
        try:
            print("检查是否进入主页")
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element_by_id("com.erlinyou.worldlist:id/chat_img")
            mylogger.info("返回主页面")
            break
        except:
            mylogger.info("并未返回主页")

        try:
            print("检查是否弹出退出窗口")
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element_by_id("android:id/button2").click()
            print("检查是否弹出退出窗口结束")
            break
        except:
            mylogger.info("并未返回主页面")
        self.driver.press_keycode(4)
    mylogger.info("{}回归原点".format(test_name))

