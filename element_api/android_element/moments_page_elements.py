from comm.element_error import element_error
import os
from log.logger import mylogger

def create_new_dynamic_element(self):
    """新建动态按钮"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_sead_moment").click()
    except Exception as e:
        element_error(self, e)


def dynamic_input_box(self):
    """新建动态输入框"""
    n = u"这是一条测试动态"
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/text_edit").send_keys(n)
        # adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
        # adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
        # os.system(adb1)
        # driver.implicitly_wait(5)
        # driver.find_element_by_id("com.erlinyou.worldlist:id/text_edit").send_keys(n)
        # os.system(adb3)
    except Exception as e:
        element_error(self, e)


def dynamic_camera_element(self):
    """新建动态 打开相册"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_camera").click()
    except Exception as e:
        element_error(self, e)


def dynamic_send_element(self):
    """发布动态 按钮 ,完成"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/send_btn").click()
    except Exception as e:
        element_error(self, e)


def dynamic_check_box_public_element(self):
    """ 公开"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_public").click()
    except Exception as e:
        element_error(self, e)


def dynamic_check_box_friends(self):
    """仅朋友可见"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_friends").click()
    except Exception as e:
        element_error(self, e)


def dynamic_check_box_specific(self):
    """部分朋友可见"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/checkbox_specific_friends").click()
    except Exception as e:
        element_error(self.driver, e)


def dynamic_travel_shot(self):
    """发布为旅拍"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_switch").click()
    except Exception as e:
        element_error(self, e)


def dynamic_choice_method(self, n):
    """
    选取第几张图片
    :param driver:self.driver
    :param n: n = 1 拍照   n = 2 录像
    """
    try:

        self.driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.GridView/"
                                     "android.widget.RelativeLayout[%s]/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(self, e)


def dynamic_take_picture_taking(self):
    """摄像机拍照按钮"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_camera").click()
    except Exception as e:
        element_error(self, e)


def dynamic_take_picture_ok(self):
    """确定拍照保留到动态里"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/img_done").click()
    except Exception as e:
        element_error(self, e)


def dynamic_recoding_picture(self):
    """录制视频 """
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_record").click()
    except Exception as e:
        element_error(self, e)


def dynamic_choice_picture(self, n):
    """选择第几张图片"""
    try:

        self.driver.find_element_by_xpath(
            "//android.widget.RelativeLayout[%s]/android.widget.RelativeLayout/android.widget.Button" % n).click()
    except Exception as e:
        element_error(self, e)


def dynamic_choice_who_look(self, n):
    """选择添加动态可见的用户"""
    try:

        self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout/android.widget.CheckBox" % n).click()
    except Exception as e:
        element_error(self, e)


def dynamic_delete_place(self):
    """新建动态不添加地点信息"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/imageview_delete").click()
    except Exception as e:
        element_error(self, e)


def dynamic_friend_title(self):
    """动态页 好友标题"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_sMenuFriend").click()
    except Exception as e:
        element_error(self, e)


def dynamic_get_give_like_number(self, n):
    """获取好友列表第一条动态 点赞数"""
    try:

        give_like_number = self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout[2]/"
                                     "android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView" % n).text
        return int(give_like_number)
    except Exception as e:
        element_error(self, e)


def dynamic_details_get_give_like_number(self):
    """动态详情页 获取点赞数"""
    try:

        give_like_number = self.driver.find_element_by_id("com.erlinyou.worldlist:id/tvLikes").text
        return int(give_like_number)
    except Exception as e:
        element_error(self, e)


def dynamic_give_like_element(self):
    """动态详情页 点赞"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/layout_likes").text
    except Exception as e:
        element_error(self, e)


def dynamic_get_browser_number(self, n):
    """获取页面浏览数"""
    try:

        browser_number = self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout[1]" % n).text
        return browser_number
    except Exception as e:
        element_error(self, e)


def dynamic_friend_first_dynamic(self, n):
    """进入页面第一条动态"""
    try:

        self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout[1]/android.widget.LinearLayout" % n).click()
    except Exception as e:
        element_error(self, e)


def dynamic_comments_element(self):
    """点评"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/layout_bottom_review").click()
    except Exception as e:
        element_error(self, e)


def dynamic_comments_input_box(self):
    """评论页面， 内容输入框"""
    try:

        content = u"这是一条评论测试"
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/text_edit").send_keys(content)
    except Exception as e:
        element_error(self, e)