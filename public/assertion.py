from comm.common import *
from element_api.android_element.mine_page_elements import download_map
from log.logger import mylogger
from element_api.android_element.home_page_details_elements import homepage_details_go_home_add, homepage_details_go_home_cancel_element


# 判断微信是否登录成功
def check_wx_login(self, test_name):
    try:
        self.driver.implicitly_wait(5)
        download_map(self)
        # driver.find_element_by_android_uiautomator('new UiSelector().text("离线地图")').click()
        mylogger.info("True")
        return True
    except Exception as e:
        mylogger.debug(e)
        screenShot(self, test_name)
        return False


# 判断微信是否退出成功
def check_wx_logout(self, test_name):
    try:
        mylogger.info("进入退出验证")
        self.driver.implicitly_wait(5)
        # count_visitor = driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[2]"
        #                                              "/android.widget.LinearLayout[5]/android.widget.TextView[1]").text
        count_visitor = self.driver.find_element_by_id("com.erlinyou.worldlist:id/user_name_tv").text
        # mylogger.info("定位成功")
        print(count_visitor)
        # count_visitor = int(count_visitor)
        # mylogger.info('获取访客数成功%s' % count_visitor)
        if count_visitor == "注册/登录":
            mylogger.info("True")
            return True
        else:
            mylogger.info("退出登录失败")
            return False

    except Exception as e:
        mylogger.debug(e)
        screenShot(self, test_name)
        return False


# 验证手机账号密码登录
def check_mobile_login(self, test_name):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('chat_img').click()
        mylogger.info("进入消息界面成功")
        return True
    except Exception as e:
        mylogger.debug(e)
        screenShot(self, test_name)
        return False


# 验证共享位置结束成功
def check_share_location_stop(self, test_name):
    try:
        ele = self.driver.find_element_by_id("stop").text
        if ele == "停止":
            mylogger.info("停止按钮未从页面消失")
            return False
        else:
            return True
    except:
        mylogger.info("停止按钮从页面消失，断言结果为True")
        return True


# def check_home_page_element(driver):
#     """
#     判断主页输入框详情页上 "回家" button状态是什么
#     :param driver:
#     :return: go_home_element , go_home_number
#     """
#     go_home_number = 0
#     try:
#         go_home_element = homepage_details_go_home_add(driver)
#         mylogger.info("当前账号并未添加回家地址")
#         go_home_number = go_home_number
#         return go_home_element, go_home_number
#     except:
#         go_home_element = homepage_details_go_home_cancel_element(driver)
#         mylogger.info("当前账号已经添加了回家地址")
#         go_home_number = go_home_number + 1
#         return go_home_element, go_home_number


def check_direct_go_home(self, test_name):
    """设置回家是否成功"""
    try:
        ele = self.find_element_by_id("com.erlinyou.worldlist:id/top_map_mode_img").text
        if ele == "到这去":
            return True
        else:
            return False
    except Exception as e:
        mylogger.info("%s" % e)
        screenShot(self, test_name)
        return False


def check_cancel_go_home(self, test_name):
    """通过是否能找到住宿这个button来判断取消回家成功"""
    try:
        ele = self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_house").text
        if ele == "住宿":
            return True
        else:
            return False
    except Exception as e:
        mylogger.info("%s" % e)
        screenShot(self, test_name)
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)
        mylogger.error("test2_a_1失败")
        return False


def check_history_search(self):
    """通过对搜索列表下第一条数据指定字段text的获取，校验生成历史数据成功"""
    try:
        ele = self.driver.find_element_by_xpath(
            "//android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]"
            "/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        print(ele)
        if ele == "奥林匹克公园":
            print('pass')
            return True
    except Exception as e:
        mylogger.info("%s" % e)
        self.driver.press_keycode(4)
        return False


def check_collection(self):
    """校验地点收藏是否成功"""
    ele_text = self.driver.find_element_by_id("com.erlinyou.worldlist:id/et").text
    if ele_text == "望京SOHO":
        return "True"
    else:
        return "False"


def check_collection_delete(self):
    """校验删除收藏地点是否成功"""
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("重命名收藏地点")')
        return False
    except:
        return True


def check_add_trip(self):
    """校验新建行程"""
    try:
        # a = "北京一日游"
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("北京一日游")').click()
        return True
    except:
        return False


def check_create_dynamic_just_friend_see(self):
    """校验新建动态仅好友可见"""
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("这是一条测试动态")').click()

        return True
    except Exception as e:
        print("False")
        mylogger.info(e)
        return False


def check_comments_successful(self):
    """校验评论成功"""
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("这是一条评论测试")')
        return True
    except Exception as e:
        mylogger.info(e)
        return False


def check_withdrawn(self):
    """校验撤回"""
    try:
        self.driver.find_element_by_android_uiautomatot('new UiSelector().textContains("撤回测试")')
        return False
    except:
        print(True)
        return True


def check_send_photo_success(self):
    print("运行了一次check")
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/img_more")
        return True
    except Exception as e:
        print(e)
        mylogger.info("发送图片校验失败")
        return False